# Installing dependencies

> For all the commands, make sure you are in this folder when running them.

## 1.1 `pip`

Install a specific version of `pandas` from `requirements.txt`

```sh
pip install -r requirements.txt
```

## 1.2 Virtual environments

1. Create virtual environment

```sh
python -m venv my_virtual_env
```

2. Activate enironment (Linux/Mac)

```sh
source my_virtual_env/bin/activate
```

2. Activate enironment (Windows)

```cmd
my_virtual_env\Scripts\activate
```

3. Install `black` as an example

```
pip install black
```

4. Check that it was installed

```sh
black --version
```

5. Deactivate environment

```sh
deactivate
```

6. Check for `black` again

```sh
black --version
```

## 1.3 `pyproject.toml`

0. (Optional) Activate your virtual environment again

1. Install from `pyproject.toml`

```sh
pip install .
```

## 1.4 `uv`

Install `uv`

```sh
pip install uv
```

```sh
uv run my_script.py
```

Wait, what just happened? Everything ran but we didn't install any dependencies?

Yes, that's cause `uv` installs any dependencies from `pyproject.toml` automatically when run a Python script with it.

## 1.5 Python versions

1. Install Python 3.12 an 3.14

```
uv python install 3.12
uv python install 3.14
```

2. Run the different Python versions and look at the output

```
uvx python@3.12 --version
uvx python@3.14 --version
```

## 1.6 Embedded dependencies

1. Look at `embedded_dependencies.py` and specifically the header comment

2. Run the Python script with `uv` and observe the output

```sh
uv run embedded_dependencies.py
```
