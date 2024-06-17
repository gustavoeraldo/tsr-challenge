test:
	coverage run --source=app -m pytest 
	coverage report -m
	coverage html -d ../htmlcov
	rm -rf .coverage

	