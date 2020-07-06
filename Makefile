.DEFAULT_GOAL := all
uvicorn_root = backend.src.app.main
api_name = delfin_api
dev_port = 8000
src_root = backend/src
app_root = $(src_root)/app
tests_root = $(src_root)/tests

isort = isort -rc $(app_root) $(tests_root)
autoflake = autoflake -r --remove-all-unused-imports --ignore-init-module-imports $(app_root) $(tests_root)
black = black $(app_root) $(tests_root)
mypy_base = mypy --show-error-codes
mypy = $(mypy_base) $(app_root)
mypy_tests = $(mypy_base) $(app_root) $(tests_root)

.PHONY: all ## Run the most common rules used during development
all: format mypy-tests tests

.PHONY: run-dev  ## Run the development server
run-dev:
	uvicorn $(uvicorn_root):$(api_name) --reload --port $(dev_port)

.PHONY: format  ## Auto-format the source code (isort, autoflake, black)
format:
	$(isort)
	$(autoflake) -i
	$(black)

.PHONY: check-format  ## Check the source code format without changes
check-format:
	$(isort) --check-only
	@echo $(autoflake) --check
	@( set -o pipefail; $(autoflake) --check | (grep -v "No issues detected!" || true) )
	$(black) --check

.PHONY: mypy  ## Run mypy over the application source
mypy:
	$(mypy)

.PHONY: mypy-tests  ## Run mypy over the application source *and* tests
mypy-tests:
	$(mypy_tests)

.PHONY: clean  ## Remove temporary and cache files/directories
clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]'`
	rm -f `find . -type f -name '*~'`
	rm -f `find . -type f -name '.*~'`
	rm -f `find . -type f -name '.coverage.*'`
	rm -rf `find . -type d -name '*.egg-info'`
	rm -rf `find . -type d -name 'pip-wheel-metadata'`
	rm -rf `find . -type d -name '.pytest_cache'`
	rm -rf `find . -type d -name '.coverage'`
	rm -rf `find . -type d -name '.mypy_cache'`
	rm -rf `find . -type d -name 'htmlcov'`
	rm -rf `find . -type d -name '.cache'`
	rm -rf *.egg-info
	rm -rf build

# .PHONY: test  ## Run tests
# test:
# 	docker-compose up -d backend-tests
# 	docker-compose exec backend-tests /tests-start.sh

# .PHONY: testcov  ## Run tests, generate a coverage report, and open in browser (macos)
# testcov:
# 	docker-compose up -d backend-tests
# 	docker-compose exec backend-tests /bin/bash -c "/tests-start.sh && echo \"building coverage html\" && coverage html"
# 	@echo "opening coverage html in browser"
# 	@open backend/app/htmlcov/index.html

# .PHONY: static  ## Perform all static checks (format, lint, mypy)
# static: format lint mypy

# .PHONY: ci  ## Run all CI validation steps
# ci: test lint mypy check-format
