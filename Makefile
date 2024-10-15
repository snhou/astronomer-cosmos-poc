VENV=venv/bin

.PHONY: venv
venv: venv/bin/activate
venv/bin/activate: requirements.txt
	@test -d venv || python3 -m venv venv
	@$(VENV)/python -m pip install --upgrade pip
	@$(VENV)/pip install -Ur requirements.txt

.PHONY: lint
lint: venv
	@$(VENV)/python -m ruff check dags/*.py
	@$(VENV)/python -m ruff check plugins
	@$(VENV)/python -m ruff check tests
	@$(VENV)/sqlfluff fix dbt/*/models/*/*.sql

.PHONY: test
test: venv
	@$(VENV)/python -m pytest tests/dags/test_*.py


create_test_folder:
	mkdir test_folder