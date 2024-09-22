.PHONY: run install
install:
	poetry install

run: install
	poetry run python dashboard/app.py