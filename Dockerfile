FROM tiangolo/uvicorn-gunicorn:python3.9-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 7844

CMD ["uvicorn", "app:api", "--host", "0.0.0.0", "--port", "7844"]
