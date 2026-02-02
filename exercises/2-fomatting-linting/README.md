# Code formatting & linting

## 2.1 Using ruff for linting

0. Install the ruff extension for your IDE, e.g. [for vscode](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)

1. Open `unused-import.py` and you should see the unused import highlighted.

2. Install `ruff` (e.g. `pip install ruff`)

3. Run `ruff`

```sh
ruff check unused-import.py
```

4. Fix the unused import

```sh
ruff check --fix unused-import.py
```

5. The unused import should now be gone
