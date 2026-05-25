# Contributing

Thanks for checking this out. This is mainly a personal learning repo, but useful improvements are welcome.

## Good Contributions

- clearer notebook explanations
- small fixes to tracker scripts
- better setup instructions
- lightweight examples that do not require huge files
- docs improvements

## Before Opening A PR

1. Keep changes small and focused.
2. Do not commit datasets, model weights, virtual environments, or generated cache files.
3. Run the checks:

```bash
python -m compileall tracking
python -m unittest discover -s tests
```

## Style

Prefer simple Python and readable notebooks. Fancy code is nice, but future-me has to understand it after one cup of tea.

