## corepy

- this document is not about the python package
- read the sources and tests to know how it works

### how to publish a python package to pypi

```shell
uv build

#export UV_PUBLISH_URL="https://pypi.example.com/simple/"
#export UV_PUBLISH_USERNAME="myuser"
#export UV_PUBLISH_PASSWORD="mypass"
uv publish

uv publish --index=pypiserver
```

**or the old way**

```shell
pyenv active pypiserver
# pip3 install build twine
python3 -m build

# twine upload -r pypiserver dist/*
twine upload dist/*
```
