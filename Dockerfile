FROM python:3.12-slim

WORKDIR /article_Search

# Copy requirements first for caching
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY article_Search ./article_Search

ENV PORT=8080
EXPOSE $PORT

ENV FLASK_APP=article_Search/main.py


CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
