import os
from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv

# Load environment variables from config.env
load_dotenv()


app = Flask(__name__)

NEWS_API_KEY = os.getenv('NEWS_API_KEY')

@app.route('/', methods=['GET', 'POST'])
def index():
    articles = []
    error = None
    query = ''
    sort_by = 'publishedAt'
    if request.method == 'POST':
        query = request.form.get('query', '')
        sort_by = request.form.get('sort', 'publishedAt')
        url = (
            f'https://newsapi.org/v2/everything?q={query}'
            f'&sortBy={sort_by}&apiKey={NEWS_API_KEY}'
        )
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()
            if data.get('status') == 'ok':
                articles = data.get('articles', [])
            else:
                error = data.get('message', 'Unknown error')
        except Exception as e:
            error = str(e)
    return render_template('index.html', articles=articles, error=error, query=query, sort_by=sort_by)

if __name__ == '__main__':
    app.run(debug=True)