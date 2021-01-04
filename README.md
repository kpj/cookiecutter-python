# cookiecutter-python

Opinionated cookiecutter template for Python packages.
Cool features:
* Package management using [poetry](https://github.com/python-poetry/poetry)
* GitHub Actions workflows for automated CI/CD
* Testing using [pytest](https://github.com/pytest-dev/pytest)
* Semantic versioning using [bump2version](https://github.com/c4urself/bump2version)

## Usage

Install cookiecutter:

```bash
$ pip install cookiecutter
```

Generate your Python package:

```bash
$ cookiecutter https://github.com/kpj/cookiecutter-python
```

Setup additional requirements:

* [Add a new API token](https://pypi.org/manage/account/token/) on PyPi and call it `GitHub Actions CI/CD — <username>/<project>`
* Add API token on `https://github.com/<username>/<project>/settings/secrets/actions` and call it `PYPI_API_TOKEN`
