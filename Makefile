debug-test:
	pytest tests

codegen:
	playwright codegen https://practicetestautomation.com/practice-test-login/

test: 
	docker-compose run tests

build:
	docker-compose build --no-cache setup
