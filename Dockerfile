FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install Flask

EXPOSE 5006

CMD ["python", "app.py"]