run:
	@poetry run python main.py

lint:
	@poetry run buf lint

gen:
	@poetry run buf generate
