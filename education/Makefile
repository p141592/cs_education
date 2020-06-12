makemigrations:
	PYTHONPATH=$(shell pwd) poetry run alembic revision --autogenerate

migrate:
	PYTHONPATH=$(shell pwd) poetry run alembic upgrade head

merge_db:
	# Смерджить базу с текущей
