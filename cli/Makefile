# Registry where you want store your Docker images
DOCKER_REGISTRY = gcr.io/${GCLOUD-PROJECT-ID}
PORTS = 8080:8080
TAG = latest
PROJECT_NAME = cs-education
GCLOUD-PROJECT-ID = home-260209
ENV = dev
MEMORY_LIMIT = 50M
ENV_VARIABLES = $(shell ./utils/convert_env.py $(shell pwd)/.env)
PYTHONPATH=$(shell pwd)/education

makemigrations:
	PYTHONPATH=${PYTHONPATH} poetry run alembic revision --autogenerate

migrate:
	PYTHONPATH=${PYTHONPATH} poetry run alembic upgrade head

progress:
	PYTHONPATH=${PYTHONPATH} jupyter notebook education/apps/progress/status.ipynb

test:
	PYTHONPATH=${PYTHONPATH} poetry run pytest -vv ${TEST_CASE}

lock:
	poetry lock 

linter:
	poetry run black --line-length 160 education

build: test linter lock
	docker build -t ${DOCKER_REGISTRY}/${PROJECT_NAME}:${TAG} .

run: build
	docker run -it ${DOCKER_REGISTRY}/${PROJECT_NAME}:${TAG}

push: build
	docker push ${DOCKER_REGISTRY}/${PROJECT_NAME}:${TAG}

# deploy
gcloud-deploy: push
	gcloud run deploy ${PROJECT_NAME} --image ${DOCKER_REGISTRY}/${PROJECT_NAME}:${TAG} --memory ${MEMORY_LIMIT} --platform managed --set-env-vars ${ENV_VARIABLES}

gcloud-remove:
	gcloud run service delete ${PROJECT_NAME}
