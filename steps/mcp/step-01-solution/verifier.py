"""Vérifications du lab MCP : lancez ce fichier pour voir vos résultats.

uv run python steps/mcp/step-01-solution/verifier.py
"""

import ast
import asyncio
import contextlib
import json
import logging
import sys
import tempfile
import traceback
from datetime import datetime, timedelta
from pathlib import Path

import server
from fastmcp import Client
from fastmcp.exceptions import ToolError
from sqlalchemy import create_engine

MARQUEUR = "_" * 3  # les trous à compléter

# Les erreurs attendues (ToolError) ne doivent pas polluer l'affichage.
logging.getLogger("fastmcp").setLevel(logging.CRITICAL)


def lancer(verifications):
    """Exécute chaque vérification et affiche ✅ ou ❌ (sans s'arrêter au premier échec)."""
    echecs = 0
    for numero, verifier in enumerate(verifications, start=1):
        try:
            verifier()
        except Exception as erreur:
            echecs += 1
            if MARQUEUR in str(erreur):
                detail = "il reste des trous à compléter"
            elif isinstance(erreur, AssertionError):
                detail = traceback.extract_tb(erreur.__traceback__)[-1].line
            else:
                detail = f"{type(erreur).__name__} : {erreur}"
            print(f"❌ exo {numero} : {detail}")
        else:
            print(f"✅ exo {numero}")
    reussis = len(verifications) - echecs
    print(f"\n{reussis}/{len(verifications)} exercices réussis")
    sys.exit(1 if echecs else 0)


def sans_trous(*noms):
    """Échoue s'il reste des trous dans le code de ces fonctions."""
    source = Path(server.__file__).read_text(encoding="utf-8")
    for noeud in ast.walk(ast.parse(source)):
        if isinstance(noeud, ast.FunctionDef) and noeud.name in noms:
            if MARQUEUR in (ast.get_source_segment(source, noeud) or ""):
                raise RuntimeError(f"trous dans {noeud.name} ({MARQUEUR})")


@contextlib.contextmanager
def base_temporaire():
    """Remplace la base du serveur par une base temporaire : messages.db n'est jamais touché."""
    with tempfile.TemporaryDirectory() as dossier:
        moteur = create_engine(
            f"sqlite:///{dossier}/test.db", connect_args={"check_same_thread": False}
        )
        server.engine = moteur
        server.init_db(moteur)
        try:
            yield
        finally:
            moteur.dispose()


def verifier_1():
    sans_trous("count_words", "now")

    async def scenario():
        async with Client(server.mcp) as client:
            outils = {outil.name: outil for outil in await client.list_tools()}
            assert "count_words" in outils, "count_words n'est pas déclaré comme tool"
            assert "now" in outils, "now n'est pas déclaré comme tool"
            for nom in ("count_words", "now"):
                description = (outils[nom].description or "").strip()
                assert len(description) > 20, f"la docstring de {nom} est trop courte"
            texte = {"text": "Bonjour SFEIR School"}
            assert (await client.call_tool("count_words", texte)).data == 3
            assert (await client.call_tool("count_words", {"text": ""})).data == 0
            utc = (await client.call_tool("now", {"timezone": "UTC"})).data
            assert datetime.fromisoformat(utc).utcoffset() == timedelta(0)
            paris = (await client.call_tool("now", {})).data
            assert datetime.fromisoformat(paris).utcoffset() != timedelta(0)

    asyncio.run(scenario())


def verifier_2():
    sans_trous("get_message", "post_message", "search_messages")

    async def scenario():
        async with Client(server.mcp) as client:
            ada = (
                await client.call_tool("post_message", {"author": "Ada", "message": "Bonjour"})
            ).data
            await client.call_tool("post_message", {"author": "Bob", "message": "Salut SFEIR"})
            trouve = (await client.call_tool("get_message", {"message_id": ada["id"]})).data
            assert trouve["author"] == "Ada"
            resultats = (await client.call_tool("search_messages", {"query": "SFEIR"})).data
            assert [m["author"] for m in resultats] == ["Bob"]
            try:
                await client.call_tool("get_message", {"message_id": 999})
            except ToolError as erreur:
                assert "999" in str(erreur), "le message d'erreur doit citer l'identifiant"
            else:
                raise AssertionError("get_message(999) doit lever une ToolError")
            try:
                await client.call_tool("post_message", {"author": "", "message": "Bonjour"})
            except ToolError:
                pass
            else:
                raise AssertionError("post_message avec un auteur vide doit échouer")

    with base_temporaire():
        asyncio.run(scenario())


def verifier_3():
    sans_trous("latest_messages_resource", "summarize_messages")

    async def scenario():
        async with Client(server.mcp) as client:
            await client.call_tool("post_message", {"author": "Ada", "message": "Bonjour"})
            contenu = await client.read_resource("messages://latest")
            assert [m["author"] for m in json.loads(contenu[0].text)] == ["Ada"]
            prompt = await client.get_prompt("summarize_messages", {"limit": 5})
            texte = prompt.messages[0].content.text
            assert "list_messages" in texte
            assert "5" in texte

    with base_temporaire():
        asyncio.run(scenario())


if __name__ == "__main__":
    lancer([verifier_1, verifier_2, verifier_3])
