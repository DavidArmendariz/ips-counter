FROM python:3.9.0

WORKDIR /app

ENV FLASK_APP=src/app.py
ENV FLASK_RUN_HOST=0.0.0.0

RUN pip install poetry

COPY poetry.lock pyproject.toml ./

RUN poetry export -o requirements.txt

RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .

CMD ["flask", "run"]