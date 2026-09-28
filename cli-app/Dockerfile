FROM python:3.12-slim

WORKDIR /app

COPY cli.py .

RUN useradd --create-home appuser

USER appuser

ENTRYPOINT ["python", "cli.py"]