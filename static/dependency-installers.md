# Part 1: Dependencies

--

## Dependency management

--

You need `numpy` and `pandas` in your Python script.
What do you do?

→ `pip install numpy pandas`

--

The most basic approach:

```
pip install <dependency>
```

--

What if you share your code?

How do you make it easy for someone to install the same dependencies?

→ `pip install -r requirements.txt`

--

Fun fact: `requirements.txt` is not a standard!

It's merely a convention

--

Anyway

--

Everything works fine 👍

Then, `pandas` releases an update ➡ your code breaks ❌

--

You don't have time to fix it.

You just want to use the older version of `pandas`

--

**Q:** What do you do?

--

**A:** Specify the version in `requirements.txt`

```requirements.txt
pandas=2.2.3
```

--

**Exercise 1.1**

- Open `exercises/1-dependencies/README.md`
- Install dependencies via `requirements.txt`

--

So far we only used `pip`
