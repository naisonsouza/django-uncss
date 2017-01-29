testenv:
	pip install -e .
	pip install -r requirements-tests.txt
	pip install Django

flake8:
	flake8 uncss

runtests:
	coverage run --branch --source=uncss `which django-admin.py` test --settings=uncss.tests.settings uncss

coveragereport:
	coverage xml --omit=uncss/test*
	python-codacy-coverage -r coverage.xml

test: flake8 runtests coveragereport

.PHONY: test runtests flake8 coveragereport
