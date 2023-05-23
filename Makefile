test:
	pytest tests

debug:
	pytest -m "debug"

codegen:
	playwright codegen https://practicetestautomation.com/practice-test-login/

activate:
	source venv/bin/activate

docker-run: 
	docker-compose run tests

docker-build:
	docker-compose build --no-cache setup

make docker-test:
	docker run -it --rm --ipc=host mcr.microsoft.com/playwright/python:v1.27.0-focal /bin/bash