# Article Search App

This is a Flask-based web application that allows users to search for live news articles using NewsAPI.org. It is containerized with Docker and deployed behind an HAProxy load balancer to ensure high availability and scalability.

---

## 🎯 Purpose

Provide a meaningful, real-world news search tool rather than a random data generator.

---

## 🚀 Key Features

- Search and filter news articles  
- Clean, user-friendly interface  
- Secure API integration  
- Dockerized deployment with HAProxy load balancing

---

## 📺 Demo Video

[Watch the Demo](https://youtu.be/7XKJjjH8fxQ)

## 📡 API Credits

- Uses [NewsAPI.org](https://newsapi.org) for article data

## 🧑‍💻 Features

- Search for articles by keyword  
- Filter by publish date  
- User-friendly, clear interface  
- Handles errors gracefully  
- Secure API key storage using environment variables  
- Dockerized for consistent deployment  
- Load balancing with HAProxy

---

## 🧪 How to Use

1. Open the app in your browser at `http://localhost`
2. Enter a keyword (e.g., `climate change`)
3. Pick a date from the dropdown
4. Click **Search**
5. Results will appear below with article titles, summaries, and dates
6. If no articles are found, a message confirms the search completed

---

## ⚙️ Running Locally

### 1️⃣ Prerequisites

- Python 3.x  
- Docker  
- Docker Compose  
- NewsAPI key from [newsapi.org](https://newsapi.org)

---

### 2️⃣ Clone the repository

```bash
git clone https://github.com/agmbabazi/article.git
cd article
````

### 3️⃣ Set your environment variable

Create a `.env` file:

```bash
NEWS_API_KEY=your_api_key_here
```

Or export it directly:

```bash
export NEWS_API_KEY="your_api_key_here"
```

### 4️⃣ Build and run with Docker

```bash
docker build -t yourdockerhubusername/news-search-app:v1 .
docker run -p 8080:8080 -e NEWS_API_KEY=$NEWS_API_KEY yourdockerhubusername/news-search-app:v1
```

Visit in browser:

```
http://localhost:8080
```

## 🧵 Deployment with HAProxy Load Balancer

> 🔔 **N.B.** My image is deployed on both `web01` and `web02` servers.
> Follow the steps below to set up both app servers and the load balancer.


### 🖥 Step 1: Clone and Build on `web01` and `web02`

```bash
git clone https://github.com/agmbabazi/article.git
cd article
sudo docker compose build --no-cache
sudo docker compose up -d
```

This sets up the Flask app containers.


### 🌐 Step 2: Set up HAProxy on `lb01`

Clone the lab setup repo:

```bash
git clone https://github.com/waka-man/web_infra_lab.git
cd web_infra_lab
sudo docker compose up -d
```

HAProxy will now be accessible at:

```
http://localhost
```

### ⚙️ HAProxy Configuration Snippet

Edit the HAProxy config (`haproxy.cfg`):

```haproxy
backend webapps
    balance roundrobin
    server web01 172.20.0.11:8080 check
    server web02 172.20.0.12:8080 check
```

### 🔁 Reload HAProxy

```bash
docker exec -it lb-01 sh -c 'haproxy -sf $(pidof haproxy) -f /etc/haproxy/haproxy.cfg'
```

### ✅ Test Your Deployment

* `http://localhost:8081` → web01
* `http://localhost:8082` → web02
* `http://localhost` → load-balanced via HAProxy

Refresh `http://localhost` several times to verify round-robin behavior.


## 🔐 Security

* ✅ API keys stored using environment variables
* ✅ Keys never pushed to the repository


## 🙌 Credits

* 🔗 Powered by [NewsAPI.org](https://newsapi.org)
* 🐍 Built with Flask
* 🐳 Docker & HAProxy for scalable deployment
* 🧪 Lab environment from [waka-man/web\_infra\_lab](https://github.com/waka-man/web_infra_lab)
