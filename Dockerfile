FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt /app/
RUN apt-get update && apt-get install -y ca-certificates && update-ca-certificates
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /app/
EXPOSE 8000
CMD ["gunicorn", "cafee_new.wsgi:application", "--bind", "0.0.0.0:8000"]