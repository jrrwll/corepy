## corepy

- this document is not about the python package
- read the sources and tests to know how it works

### how to publish a python package to pypi

```bash
pip3 install build twine

python3 -m build
twine upload dist/*
```
