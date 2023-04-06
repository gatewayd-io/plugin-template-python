run:
	@poetry run python main.py

lint:
	@buf lint

gen:
	@buf generate
