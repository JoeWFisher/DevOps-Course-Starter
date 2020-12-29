FROM python:3.8.2-buster as base

RUN pip install gunicorn
RUN pip install poetry

WORKDIR /DevOps-Course-Starter
COPY poetry.lock pyproject.toml /DevOps-Course-Starter/

RUN poetry config virtualenvs.create false

COPY . /DevOps-Course-Starter/

EXPOSE 5000

FROM base as production
ENV FLASK_ENV=production
RUN poetry install --no-dev
ENTRYPOINT ["gunicorn", "--config", "gunicorn.conf.py", "wsgi:app"]

FROM base as development
RUN poetry install
ENTRYPOINT ["poetry", "run", "flask", "run", "-h", "0.0.0.0", "-p", "5000"]


