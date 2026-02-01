## Virtual environments 🪄📦

--

Premise:

You work on two projects. One requires `pandas` version `2.2` and one requires version `2.3`

**Q:** What do you do?

--

**A:** Virtual environments ✨

--

- Virtual environments give you an isolated place for packages for a project.
- Install different versions of a package for each project

--

### Usage

Create environment

```bash
python -m venv my_virtual_env
```

Activate

Linux/Mac

```bash
source my_virtual_env/bin/activate
```

Windows

```powershell
my_virtual_env\Scripts\activate
```

--

- [ ] TODO Exercise

--

All of this is kinda pain. What can help us?

--

## Tools 🧰

--

Some tools that exist:

- **conda**
- poetry
- pipenv
- uv <- more on that one later

--

### conda

Create environment

```sh
conda create --name my_virtual_env python=3.11
```

(Can even specify Python version)

Activate it

```bash
conda activate my_virtual_env
```

And then either

```bash
conda install pandas
```

or

```
pip install pandas
```

--
Install dependencies with

```
pip install -r requirements.txt
```

or

```
conda env create -f environment.yml
```

(even creates the virtual environment)

--

But!

- `requirements.txt` is not a standard
- and `environment.yml` only exists for `conda`

Can we do better?

--

Yes!

### [PEP621](https://peps.python.org/pep-0621/) - Storing project metadata in pyproject.toml

--

[PEP621](https://peps.python.org/pep-0621/) - Storing project metadata in pyproject.toml

- Python standard released in 2020
- Defines `pyproject.toml` file for specifying dependencies

```toml
[project]
name = "my-package"
version = "0.1.0"
description = "A short description"
dependencies = [
    "pandas>=2.3.3",
    "numpy",
]
```

Goodbye

```
pip install -r requirements.txt
```

Hello

```
pip install .
```

--

Supported by

- `pip`
- `poetry`
- `uv` 👀

--

- [ ] TODO: Exercise

--

However we didn't fix the virtual environments part yet

---

Introducing ✨ **[uv](https://docs.astral.sh/uv/)** ✨

- Created in 2024
- Fastest Python dependency installer
- Handles virtual environments
- Handles different Python versions

https://docs.astral.sh/uv/

--

Usage

Create a new project:

```
uv init my-project
```

(Creates `pyproject.toml` and sample Python file)

Run file in an existing project

```bash
uv run hello-world.py
```

(Handles virtual environment creation, installs dependencies if missing, and finally runs the code. All of that in <10ms)

--

Basically replace

```bash
python hello-world.py
```

with

```bash
uv run hello-world.py
```

--

- [ ] ## TODO exercise

### Bonus: [PEP723](https://peps.python.org/pep-0723/) - Inline script metadata

You only have a single Python script? You don't want to create `pyproject.toml`

```python
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "requests<3",
#   "rich",
# ]
# ///

import requests
from rich.pretty import pprint

resp = requests.get("https://peps.python.org/api/peps.json")
data = resp.json()
pprint([(k, v["title"]) for k, v in data.items()][:10])
```

--

- [ ] TODO exercise
