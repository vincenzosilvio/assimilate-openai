install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_quickstart.py

format:
	black *.py

lint:
	pylint --disable=R,C quickstart.py

all: install lint test