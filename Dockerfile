FROM python:3.14-alpine
WORKDIR /app

RUN pip install --root-user-action ignore --upgrade --no-cache-dir pip && \
    pip install --root-user-action ignore --no-cache-dir pipenv && \
    pipenv sync --clear

COPY . /app/
EXPOSE 5000
CMD ["python3", "app.py"]
