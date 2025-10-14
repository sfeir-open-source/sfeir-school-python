# How to improve exercices

* Use uv and asdf/mise
* Verify dependencies still work
* Generate requirements.txt for users without asdf/uv installed :

```bash
uv pip compile pyproject.toml -o requirements.txt
```
