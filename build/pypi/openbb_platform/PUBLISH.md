# Publishing to PyPI

Publishing checklist:

> Note: you need to have the appropriate credentials and permissions to publish to PyPI

1. Ensure all unit tests pass: `pytest openbb_platform -m "not integration"`
2. Ensure all integration tests pass: `pytest openbb_platform -m integration`
3. Run the publishing script: `python build/pypi/openbb_platform/publish.py`
4. Update poetry files: `python build/pypi/openbb_platform/poetry_update.py`
5. Open a PR so that changes are reflected on the main branch

Finally, check if everything works:

1. Install and test the package from Pypi on a clean environment.
2. Check if all the `pyproject.toml` files are correct, including the `openbb_platform` one.
3. Double check if there is any new extension or provider that needs to be added to [integration tests GitHub Action workflow](/.github/workflows/platform-api-integration-test.yml).
