<!-- .slide: class="with-code" -->

# Installation de l’environnement

**mise : plusieurs versions d'outils, par projet**

* Gestionnaire de versions pour de nombreux outils : Python, Node.js, Terraform…
* Chaque projet fixe ses versions, `mise` active les bonnes en entrant dans le dossier.

```toml
# mise.toml
[tools]
python = "3.14"
uv = "latest"
```

<!-- .element: class="big-code" -->

* `.python-version` : fichier lu par uv, pyenv et d'autres outils (`3.14`).

Notes:
mise (successeur moderne de asdf) est utile pour passer d'un projet en Python 3.10 à un autre en 3.14 sans rien réinstaller à la main. `mise use python@3.14` écrit le `mise.toml` ci-dessus et installe la version si besoin. Les commandes `mise install` et `mise ls` complètent.

`.python-version` est le fichier le plus répandu pour fixer la version de Python : uv le crée avec `uv init` et le lit. mise, lui, ne lit pas `.python-version` par défaut : il faut l'activer avec `mise settings idiomatic_version_file_enable_tools=python` (testé avec mise 2026.10). Sinon, mettre la version dans `mise.toml`. L'ancien `.tool-versions` d'asdf est aussi accepté par mise.

Dans ce dépôt : `.python-version` (3.14) pour uv, et `.tool-versions` pour mise.
