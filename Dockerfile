FROM python:3.10.6

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
CMD ["uvicorn", "API.server:app", "--host", "0.0.0.0", "--port", "8000"]