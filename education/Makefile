makemigrations:
	PYTHONPATH=$(shell pwd) poetry run alembic revision --autogenerate

migrate:
	PYTHONPATH=$(shell pwd) poetry run alembic upgrade head

create_engine:
	PYTHONPATH=$(shell pwd) poetry run python -c "from core.db import engine, Base; Base.metadata.create_all(engine)"