test:
	pytest tests

codegen:
	playwright codegen https://practicetestautomation.com/practice-test-login/

docker-run: 
	docker-compose run tests

docker-build:
	docker-compose build --no-cache setup
