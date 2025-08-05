# Article Search App

A simple Flask web app to search news articles using [NewsAPI](https://newsapi.org/).

## Features
- Search for news articles by keyword.
- Sort results by date, relevancy, or popularity.
- Error handling for API/network issues.
- User-friendly web interface.

## API Used
- [NewsAPI](https://newsapi.org/docs/endpoints/everything)
- Credit: NewsAPI.org

## Setup

1. Clone the repo.
2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Add your NewsAPI key to `config.env`:
    ```
    NEWS_API_KEY=your_actual_newsapi_key_here
    ```
4. Run the app:
    ```
    python main.py
    ```
5. Open [http://localhost:5000](http://localhost:5000) in your browser.

## Security
- API key loaded from environment, not committed to repo.

## Attribution
- NewsAPI.org for news data.

## video link 
 - https://youtu.be/7XKJjjH8fxQ

##
