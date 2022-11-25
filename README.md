# WORD CHAIN

This is Python repo template.

## GitHub Workflow

Defined in [workflow.yaml](.github/workflow/workflow.yaml)

Just change the name of the `<image name>`

## pyenv?

If you use `pyenv`, create a virtualenv

```bash
pyenv virtualenv 3.10 <venv name>
```

or load existing one

```bash
pyenv local <venv name>
```

Get `<ven name>` with:

```bash
pyenv which python
```

## Requirements.txt

### first install

```bash
pip install -r requirements.txt
```

### Add packages

Packages should be added to the [`requirements.in`](requirements.in) or to the [`dev-requirements.in`](dev-requirements.in).

After this, use `pip-compile` to translate these to [`requirements.txt`](requirements.txt) and [`dev-requirements.txt`](dev-requirements.txt).

```bash
pip-compile requirements.in
pip-compile dev-requirements.in
```

### Install and Uninstall packages

Packages can be installed with

```bash
pip-sync requirements.txt dev-requirements.txt
```

This will install all the packages specified in the requirement files and will uninstall the ones that are not.


## Docker Image

The image gets built and pushed automatically to the ACR when pushed to GitHub, but for local testing, continue reading.


### Build Image

In order to build the image manually, run

```bash
IMAGE_NAME=<image name>
TAG=1
docker build -t $IMAGE_NAME:$TAG .
```

### Run Image

```bash
docker run $IMAGE_NAME:$TAG hello
```
