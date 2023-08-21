help:
	@echo
	@grep -E '^[ .a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
	@echo

build:  ## Initial build
	python3.11 -m venv .venv
	poetry install

clean:  ## Clear any cache files and test files
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	rm -rf test_output
	rm -rf site/
	rm -rf dist/

run:  ## Run the server
	python server.py run

lint:  ## Run linting on the project
	ruff src/ --fix
	black src/

mypy:  ## Check typing
	mypy src/

.PHONY: serve
