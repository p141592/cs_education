makemigrations:
	PYTHONPATH=$(shell pwd) poetry run alembic revision --autogenerate

migrate:
	PYTHONPATH=$(shell pwd) poetry run alembic upgrade head

merge_db:
	# Смерджить базу с текущей

progress:
	jupyter notebook education/apps/plan/progress.ipynb

notes:
	jupyter notebook education/apps/materials/
