# 🎬 Movie Hub

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/) 
[![Django](https://img.shields.io/badge/Django-5.x-green)](https://www.djangoproject.com/) 
[![Render](https://img.shields.io/badge/Live%20Demo-Render-brightgreen)](https://movie-hub-a4gn.onrender.com)

**Live Demo:** [https://movie-hub-a4gn.onrender.com](https://movie-hub-a4gn.onrender.com)

A Django web application that allows users to **discover, track, and interact with movies and TV shows**. Users can search for any movie or show, check IMDb ratings, view trailers, and manage their watch lists, favorites, and watched content. Admins, editors, and moderators have special permissions to manage content, while all users can explore what others are watching. 
It combines content discovery with **gamification**, **quizzes**, **badges**, and **asynchronous notifications** to keep users engaged.

---

## ✨ Motivation

This project was inspired by my love for movies and my desire to track:
- What I've watched  
- What I want to watch  
- What others are enjoying

Beyond entertainment, Movie Hub was built as a **learning-driven project** to apply real-world backend concepts such as:
- Distributed architecture
- Asynchronous background processing
- Scheduled tasks
- Production containerization
- Email notifications
- Production deployment and scaling

---

## 🛠 Features

- **🔍 Search and Discovery**  
  Search for any movie or show and view detailed information including IMDb ratings and trailers.

- **📌 Watchlist & Favorites**  
  Add movies/shows to your watchlist, mark them as watched, or save them as favorites — all without page reloads using AJAX.

- **🎲 Pick Tonight's Movie**  
  Can't decide what to watch? Hit the **"Pick Tonight's Movie/Show"** button and get a random pick straight from your watchlist. No more endless scrolling.

- **🔥 Trending & Popular Content**  
  Home page displays trending, popular, and user-added content dynamically. Switch between movies and shows easily.

- **📜 Infinite Scroll**  
  Smooth, endless browsing experience across home, search, and grid views — no more clicking through pages.

- **🧠 Quizzes & Gamification**
  - Weekly rotating quizzes
  - Earn **badges** by interacting with content
  - Encourages consistent user engagement

- **🏅 Badges System**
  - Users earn badges based on activity
  - Tracks latest badge achievements
  - Inactivity is detected automatically

- **🔔 Notifications System**
  - **In-app notifications** for:
    - Weekly quiz updates
    - System announcements
    - **Community activity** — get notified when other users add highly rated movies/shows (6.0+) to their watchlist or watched list
  - **Email notifications (async)** for:
    - Inactive users
    - Users who haven't earned a badge in a while
    - Welcome emails on signup

- **🌍 Community Activity Feed**  
  See what other users are watching and adding in real time. Activity notifications include anti-spam filtering (rate limiting and 25% sampling) to keep the feed relevant and clean. Notifications link directly to the user's list.

- **⚡ Asynchronous Background Tasks**
  - Built using **Celery + Redis**
  - Tasks include:
    - Weekly quiz rotation
    - Scheduled notifications
    - Async email delivery with retries
    - Community activity event processing
  - Managed via **django-celery-beat**

- **👥 User Interaction**  
  Discover other users, see their watched content, and interact through reviews and ratings.

- **🛡 Admin & Moderator Panel**  
  - Admins, editors, and moderators have specific permissions.  
  - Moderators can view user media, check ratings/reviews, and manage content efficiently.

- **🔎 Advanced Searching & Filtering**  
  Extensive search, filtering, and ordering options for fast content discovery.

- **💻 Responsive & Intuitive UI**  
  Modernized layouts across home, search, grid, and favorites views. Designed for usability and clean presentation of movies and shows.

---

## ⚙️ Tech Stack

### Backend
- Python 3.x  
- Django 5.x  
- Django REST Framework (optional for APIs)   
- Celery (background tasks)
- Redis (message broker & result backend)
- django-celery-beat
- django-celery-results

### Infrastructure
- Docker
- Gunicorn
- Redis (TLS supported)
- Whitenoise
- Cloudinary

### Email
- Brevo API (Transactional Email API)
- Async email delivery with retry logic

### Database
- MySQL (local development)
- PostgreSQL / Neon (production)

### Other
- Bootstrap / CSS
- Git & GitHub

---

## 🚀 Deployment

- **Web App:** Render  
- **Database:** Neon  
- **Async Tasks:** Celery + Redis (Upstash, production-ready with TLS)

The project is live on Render: [https://movie-hub-a4gn.onrender.com](https://movie-hub-a4gn.onrender.com)

---

## 🐳 Docker Setup

This project is fully containerized using:

- `Dockerfile`
- `docker-compose.yml`

### Services Defined in docker-compose

- **web** → Django + Gunicorn
- **worker** → Celery worker
- **beat** → Celery Beat scheduler

---

## 🔐 Environment Configuration

This project uses environment variables.

1️⃣ Copy the example file:

```bash
cp .env.example .env
```
2️⃣ Fill in your own values in the .env file

---

## Steps to run locally:
This project is containerized using Docker. To run the project locally, you will need to have Docker installed on your machine.

```bash
docker-compose build
```
### Run all services
```bash
docker-compose up
```
### This will start:
- Web server on http://localhost:8000
- Celery worker
- Celery Beat scheduler

### To stop:
```bash
docker-compose down
```

---

### 🩺 Health Check
A /health/ endpoint is included for container monitoring.

Dockerfile includes:
- Non-root user execution
- Production Gunicorn server
- Static file collection
- HEALTHCHECK configuration

---

## 🎯 Learning Outcomes

- Building a full-stack web application with Django
- Handling user authentication and permissions
- Advanced search, filtering, and ordering of content
- Managing static files and media in production
- CRUD operations for user-generated content and admin moderation
- Working with APIs (TMDB) for movie data and trailers
- Asynchronous task processing with Celery & Redis
- Scheduled background jobs with django-celery-beat
- Clean separation of concerns and scalable architecture
- Distributed Django architecture
- Production-ready Docker containerization
- Identifying and resolving N+1 query problems using `select_related` and `prefetch_related`
- Building real-time community features with anti-spam logic
- AJAX-driven interactions for seamless UX without page reloads
- Infinite scroll implementation for content-heavy views

---

## 👩‍💻 About the Developer

Hi! I'm Sofi, a Software Engineering student at **AASTU** and an **ALX Backend Program participant**.  
I'm passionate about Python, web development, and creating full-stack applications that are both functional and user-friendly.

### 🤳 Connect with me:

<p align="center">
  <a href="https://linkedin.com/in/sofoniyas-alebachew-bb876b33b">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  &nbsp;&nbsp;
  <a href="https://github.com/Sofi391">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
  </a>
</p>

---
