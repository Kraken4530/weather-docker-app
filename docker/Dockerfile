FROM python:3.12

WORKDIR /app

COPY ./src/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt


COPY ./src /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
