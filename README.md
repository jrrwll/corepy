# corepy

- this document is not about the python package
- read the sources and tests to know how it works

### how to publish a python package to pypi

```bash
python3 setup.py sdist
pip3 install twine
twine upload dist/*
```
