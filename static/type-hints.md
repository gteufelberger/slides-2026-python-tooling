# Part 3: Type hints

--

Python supports type hinting

```python
def my_function(input: int) -> str
    #                   ^       ^
    #
    # `int` and `str` are hints at what
    #  type input and output may be

    return f"The number is {input}"



print(my_function(123))
```

--

There's libraries to check whether the hints are correct

e.g.

```python
def my_function(input: int) -> int:
    # Note the hinted `int` return value
    # while the actual return is a string
    return f"The number is {input}"
```

would throw an error

--

Tools that do static type checking:

- `mypy`
- `Pyrefly`
- `Pyright`
- `ty` <- ✨

--

`ty` is the newest of the tools and

![Shows a bar chart with benchmark results.](https://docs.astral.sh/ty/assets/ty-benchmark-cli.svg)

ty was secretly soft released [end of November 2025](https://github.com/astral-sh/ty/commit/7a6b79d37e165f2e731893bde05f6a548babc006) with [a beta announcement mid December 2025](https://astral.sh/blog/ty).

--

Try for yourself online: https://play.ty.dev/

<iframe src="https://play.ty.dev/" title="ty playground" style="width: 100%; height: 70vh; border: none;"></iframe>

--

vscode extension

https://marketplace.visualstudio.com/items?itemName=astral-sh.ty

<iframe src="https://marketplace.visualstudio.com/items?itemName=astral-sh.ty" />
