install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py

lint:
	ruff check *.py mylib/*.py test_*.py *.ipynb

test:
	python -m pytest -vv --nbval -cov=mylib -cov=main test_*.py *.ipynb

all: install format lint test

generate:
	python main.py

	@if [ -n "$$(git status --porcelain)" ]; then \
		git config --local user.email "action@github.com"; \
		git config --local user.name "GitHub Action"; \
		git add .; \
		git commit -m "Add generated content."; \
		git push; \
	else \
		echo "No changes to commit. Skipping commit and push."; \
	fi