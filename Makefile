default:
	@echo "Must call a specific subcommand"
	@exit 1

lint:
	@echo "--> Linting python"
	flake8
	@echo ""

test-python:
	@echo "--> Running Python tests"
	sh tests/runtests.sh
	@echo ""

coverage:
	@echo "--> Running Python tests coverage"
	sh tests/runtests.sh --cov-report html --cov-report term:skip-covered --cov={{project_name}}
	@echo ""

test: lint test-python

locales:
	{{project_name}} django makemessages -i static -a
	{{project_name}} django compilemessages

load_dev_data:
	@echo "--> Migrating DB..."
	{{project_name}} django migrate
	@echo "--> Loading dev data..."
	{{project_name}} django loaddata dev

clear_dev_data:
	@echo "--> Dropping database..."
	docker-compose exec postgres dropdb -U dev dev
	@echo "--> Creating database..."
	docker-compose exec postgres createdb -U dev dev

reset_dev_data: clear_dev_data load_dev_data

.PHONY: lint test test-python locales load_dev_data clear_dev_data reset_dev_data
