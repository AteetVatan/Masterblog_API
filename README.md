# 🧬🌐 Masterblog – Fullstack Blog Application

A complete, modular, and extensible **Flask-based fullstack blog platform** featuring:

- 🔁 **CRUD operations** with a clean RESTful API
- 🧱 **Repository + Service Layer architecture**
- 🧾 **Frontend powered by Flask, JS, CSS, and Jinja**
- 📝 **Mock JSON database** with a path to real DB migration
- 📘 **Swagger UI for seamless API exploration**

---

## 🧩 Project Overview

The Masterblog Project is split into two tightly integrated layers:

### 1️⃣ **Backend – Masterblog API**
A robust REST API with clean architecture and layered logic.

### 2️⃣ **Frontend – Masterblog UI**
A Flask-based UI layer rendering data dynamically and elegantly.

---

## ⚙️ Tech Stack

| Layer    | Tech Components |
|----------|------------------|
| Backend  | Flask, JSON, Swagger UI |
| Frontend | Flask, HTML, CSS, JS, Jinja2 |
| Design   | MVC-inspired, Repository Pattern, Service Layer |
| Docs     | Swagger (OpenAPI 2.0) |

---

## 📁 Project Structure

```
masterblog/
├── backend/
│    ├── backend_app.py            # Main Flask app entry point
│    ├── config.py                 # Configuration file
│    ├── requirements.txt          # Python dependencies
│    ├── README.md                 # Read Me file
│    ├── /controllers              # HTTP route handlers
│    │   └── app_controller.py     # The main APP API endpoint controller
│    │   └── post_controller.py    # The blog posts API endpoint controller  
│    ├── /services                 # Business logic
│    │   └── post_service.py       # The blog posts Business Logic   
│    ├── /repositories             # Data access layer
│    │   └── post_repository.py    # The blog posts Data access layer
│    ├── /models                   # Data models
│    │   └── post_model.py         # The blog posts Data model
│    ├── /helpers                  # The helper classes
│    │   └── json_file_helper.py   # The Json file operation helpers
│    │   └── logs_helper.py        # The log generation helpers
│    ├── /enums                    # The application enumerations
│    │   └── direction.py     
│    │   └── sort.py     
│    ├── /data                     # Mock JSON database
│    │   └── posts.json            # Mock blog posts JSON data
│    ├── /static
│    │   └── masterblog.json       # Swagger documentation config
│    └── README.md                 # Project guide
├── frontend/                      # UI rendering and interactions
│    ├── frontend_app.py           # Flask app entry point
│    ├── config.py                 # Configuration for frontend
│    ├── requirements.txt          # Python dependencies
│    ├── /templates
│    │   └── index.html            # UI layout using Jinja2 templating
│    ├── /static
│       ├── main.js                # Handles dynamic rendering, likes, edits
│       └── styles.css             # Core frontend styling
```

---

# 🚀 Backend – Masterblog API

A modular, extensible **Flask-based REST API** for managing blog posts, built with:

- 🔁 **CRUD operations**
- 🧱 **Repository pattern + Service Layer architecture**
- 📝 **JSON-based mock database**
- 📘 **Swagger UI for API documentation**

---
## 🚀 API Endpoints

Base URL: `http://localhost:5002`

### 📄 `/api/posts`

| Method | Description                                             |
|--------|---------------------------------------------------------|
| GET    | Get all blog posts with optional sorting and pagination |
| POST   | Create a new blog post                                  |

**Query Parameters for GET**:

- `sort`: `title` or `content`
- `direction`: `asc` or `desc`
- `page`: Page number (default: 1)
- `per_page`: Number of posts per page (default: 10)

---

### 🔍 `/api/posts/search`

| Method | Description                      |
|--------|----------------------------------|
| GET    | Search posts by title or content |

---

### ✏️ `/api/posts/{id}`

| Method | Description         |
|--------|---------------------|
| PUT    | Update a post by ID |
| DELETE | Delete a post by ID |

---

### ❤️ `/api/posts/update_likes`

| Method | Description                 |
|--------|-----------------------------|
| POST   | Update like count for a post |

**Request Body:**

```json
{
  "post_id": 1
}
```

---

## 🧩 Architecture

This project follows a clean, layered CRUD Repository pattern:

- **Controllers** – Flask routes that process requests and responses.
- **Services** – Implements core logic and validation (PostService).
- **Repositories** – JSON file I/O, separated from logic.
- **Models** – Defines data structure with validation (PostModel).

---

## 📘 Swagger API Docs

Once the app is running, view interactive docs at:

```
http://localhost:5002/api/docs
```

Documentation is powered by `flask-swagger-ui`, configured via `/static/masterblog.json`.

---

## 📦 Requirements

Installed via `requirements.txt`:

```
Flask
flask-cors
flask-limiter
flask-swagger-ui
```

---

## 🛠️ Running the App

```bash
# 1. Navigate into the backend folder
cd backend

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python backend_app.py
```

App runs on `http://localhost:5002`

---

## 📌 To Do / Future Enhancements

- 🔐 Integrate JWT authentication
- 🔎 Full-text search support
- 🧪 Add unit & integration tests
- 🗂️ Filter posts more efficiently
- 💾 Move from JSON to SQLite or PostgreSQL backend

---

# 🌐 Frontend – Masterblog UI

A lightweight, responsive **Flask-based frontend** built to interface with the [Masterblog API](../backend/README.md). This layer focuses on rendering and interacting with blog posts using HTML, JavaScript, and CSS — the traditional trio.

---

## ⚙️ Tech Stack

- 🐍 **Flask** – Python web framework for serving HTML templates
- 🧾 **Jinja2** – Template engine for dynamic rendering
- 🎨 **CSS** – Basic styling with a clean layout
- 📜 **JavaScript** – Frontend interactivity (fetch API)

---

## 📁 Folder Structure

```
frontend/
├── frontend_app.py           # Flask app entry point
├── config.py                 # Configuration for frontend
├── requirements.txt          # Python dependencies
├── /templates
│   └── index.html            # UI layout using Jinja2 templating
├── /static
│   ├── main.js               # Handles dynamic rendering, likes, edits
│   └── styles.css            # Core frontend styling
```

---

## 🚀 Features

- 📄 **Render all blog posts** from Masterblog API
- ✍️ **Create and edit posts** via forms
- 🔍 **Search bar** for filtering posts
- 🔄 **Dynamic content loading** using JS Fetch API

---

## 🔗 Integration with Backend

Make sure the [Masterblog API backend](../backend/README.md) is running at:

```
http://localhost:5002
```

The frontend fetches blog post data from this endpoint and renders it on the fly.

---

## 🛠️ Running the Frontend

```bash
# 1. Navigate to the frontend folder
cd frontend

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the frontend server
python frontend_app.py
```

App runs at `http://localhost:5000` and connects to the backend on `http://localhost:5002`.

---

## 📦 Requirements

Install via `requirements.txt`:

```
Flask
```

(Add any additional modules you use in the future.)

---

## 🔮 To Do / Enhancements

- ✅ Initial render and dynamic content loading
- 🔐 Form validation (client + server-side)
- 🎨 Improved responsive styling (mobile support)
- 🔧 Add post filtering & tag system
- 📡 Error handling for API failures
- 🌍 Deploy to a web server (e.g., Gunicorn + Nginx)

---

## 🧠 Author

Crafted by **Ateet – The AI Expert**  
Devoted to **clean code, ancient values, and modern engineering**. 🚀

---

## 📜 License

MIT License – Build, modify, deploy, and share freely.
