"""Tests du serveur MCP généré avec from_fastapi (bonus).

Le serveur est chargé depuis le dossier de ce fichier (importlib).
On vérifie seulement que des tools ont bien été générés : les appels passent par l'API
FastAPI et sont couverts par les tests du lab FastAPI.
"""

import importlib.util
import sys
from pathlib import Path

import pytest
from fastmcp import Client

SERVER_PATH = Path(__file__).resolve().parent / "server.py"


def load_server():
    name = f"mcp_{SERVER_PATH.parent.name.replace('-', '_')}_server"
    spec = importlib.util.spec_from_file_location(name, SERVER_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


mcp = load_server().mcp


@pytest.fixture
def anyio_backend():
    return "asyncio"


@pytest.mark.anyio
async def test_from_fastapi_generates_tools():
    async with Client(mcp) as client:
        tools = await client.list_tools()
    assert len(tools) > 0
