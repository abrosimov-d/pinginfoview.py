FROM python:3.12-slim

RUN pip install --no-cache-dir ping3 seaborn

COPY main.py .
COPY app app
COPY ui ui

RUN mkdir -p ui/images

CMD ["python", "main.py"]
