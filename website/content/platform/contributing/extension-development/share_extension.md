---
title: Share your extension
sidebar_position: 4
description: A guide on how to publish, release and install an extension on PyPI using
  commands like poetry build and poetry publish. Part of the developer setup includes
  generating an API token.
keywords:
- extension
- publish
- PyPI
- API token
- poetry
- pyproject.toml
- pip install
- release
- .whl
- tar.gz
- poetry build
- poetry publish
- dist
- openbb
---

import HeadTitle from '@site/src/components/General/HeadTitle.tsx';

<HeadTitle title="Share your extension - Extension Development - Contributing | OpenBB Platform Docs" />

We encourage you to share your extension with the community. You can do that by publishing it to PyPI.

## Publish your extension to PyPI

To publish your extension to PyPI, you'll need to have a PyPI account and a PyPI API token.

### Setup

Create an account and get an API token from <https://pypi.org/manage/account/token/>
Store the token with

```bash
poetry config pypi-token.pypi pypi-YYYYYYYY
```

### Release

`cd` into the directory where your extension `pyproject.toml` lives and make sure that the `pyproject.toml` specifies the version tag you want to release and run.

```bash
poetry build
```

This will create a `/dist` folder in the directory, which will contain the `.whl` and `tar.gz` files matching the version to release.

If you want to test your package locally you can do it with

```bash
pip install dist/openbb_[FILE_NAME].whl
```

### Publish

To publish your package to PyPI run:

```bash
poetry publish
```

Now, you can pip install your package from PyPI with:

```bash
pip install openbb-some_ext
```
