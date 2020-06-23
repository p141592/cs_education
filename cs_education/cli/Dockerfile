  
FROM python:3.8
ENV PYTHONPATH /opt/application/
ENV PATH /opt/application/:$PATH

WORKDIR /opt/application/

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
COPY poetry.lock .
COPY pyproject.toml  .
RUN poetry install --no-dev --no-root

COPY education /opt/application/

CMD python __main__.py quiz bot start
