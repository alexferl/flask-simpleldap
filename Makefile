.PHONY: help dev test lint pre-commit

.DEFAULT: help
help:
	@echo "make dev"
	@echo "	prepare development environment"
	@echo "make test"
	@echo "	run tests"
	@echo "make lint"
	@echo "	run black"
	@echo "make pre-commit"
	@echo "	run pre-commit hooks"

dev:
	pipenv install --dev

test:
	pipenv run pytest

lint:
	pipenv run black .

pre-commit:
	pipenv run pre-commit
