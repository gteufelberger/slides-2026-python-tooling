# Installing dependencies

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
