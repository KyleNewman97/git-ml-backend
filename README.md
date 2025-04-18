# git-ml-backend

Backend for `git-ml`. The backend uses Python and FastAPI.

`git-ml` is an open source tool that seeks to improve the way machine learning engineers source control their projects. Think DVC but simpler.

## Setup

PDM is used for dependency management. To install PDM please follow the instructions [here](https://pdm-project.org/en/latest/#recommended-installation-method). Once PDM is installed, the project's dependencies can be installed with:

```bash
pdm install
```

The project requires Python >=3.11

## Development

### Activate virtual environment

To activate the virtual environment run:

```bash
source .venv/bin/activate
```

### Starting development server

The development server can be started by running:

```bash
fastapi run src/main.py
```

### Create dummy repo

During development it is commonly useful to have a dummy repo that the backend can serve information from. As a result, a script has been made to create a dummy repo:

```bash
python create_dev_repos.py
```

### Running tests

Tests can be run with:

```bash
pytest tests/
```

### Static code analysis

This repo uses trunk for static code analysis. To install trunk follow the instructions [here](https://docs.trunk.io/code-quality/setup-and-installation/initialize-trunk). To perform static code analysis run:

```bash
trunk check
```
