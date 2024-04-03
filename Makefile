.PHONY: help dev clean update test lint pre-commit

VENV_NAME?=venv
VENV_ACTIVATE=. $(VENV_NAME)/bin/activate
PYTHON=${VENV_NAME}/bin/python3

.DEFAULT: help
help:
	@echo "make dev"
	@echo "       prepare development environment, use only once"
	@echo "make clean"
	@echo "       delete development environment"
	@echo "make update"
	@echo "       update dependencies"
	@echo "make test"
	@echo "       run tests"
	@echo "make lint"
	@echo "       run black"
	@echo "make pre-commit"
	@echo "       run pre-commit hooks"

dev:
	make venv

venv: $(VENV_NAME)/bin/activate
$(VENV_NAME)/bin/activate:
	test -d $(VENV_NAME) || virtualenv -p python3 $(VENV_NAME)
	${PYTHON} -m pip install -U pip
	${PYTHON} -m pip install -r dev_requirements.txt
	$(VENV_NAME)/bin/pre-commit install
	touch $(VENV_NAME)/bin/activate

clean:
	rm -rf venv

update:
	${PYTHON} -m pip install -U -r dev_requirements.txt
	$(VENV_NAME)/bin/pre-commit install

test: venv
	${PYTHON} -m pytest

lint: venv
	$(VENV_NAME)/bin/black -t py310 --exclude $(VENV_NAME) .

pre-commit: venv
	$(VENV_NAME)/bin/pre-commit
