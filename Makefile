.PHONY: install virtualenv ipython clean test pflake8

install:
	@echo "Installing for dev environment"
	@.venv/bin/python -m pip install -e '.[dev]'

virtualenv:
	@.venv/bin/python -m pip -m venv .venv

ipython:
	@.venv/bin/ipython

lint:
	@.venv/bin/pflake8

fmt:
	@.venv/bin/black dundie tests integration

test:
	@.venv/bin/pytest -s

watch:
	# @.venv/bin/ptw
	@ls **/*.py | entr pytest