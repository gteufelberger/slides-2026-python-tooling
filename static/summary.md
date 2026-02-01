# Summary

- In general use the best tool for the job
- **But!** Don't get stuck using what you're used to

--

If your tech stack looks like

- pip
- conda
- flake8
- black
- isort
- pyupgrade

Maybe consider changing it to

- uv
- ruff

--

- My recommendation:
  If you create a new Python project in 2026, use
  - uv (with `pyproject.toml`)
  - ruff (handles formatting and linting)
  - (maybe) ty

Not cause I told you so but because _currently_ they are the best.
Whenever something better comes around, switch again
