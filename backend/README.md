# 🧬 Masterblog API

A modular, extensible **Flask-based REST API** for managing blog posts, built with:

- 🔁 **CRUD operations**
- 🧱 **Repository pattern + Service Layer architecture**
- 📝 **JSON-based mock database**
- 📘 **Swagger UI for API documentation**

---

## 📁 Folder Structure

```
backend/
├── backend_app.py            # Main Flask app entry point
├── config.py                 # Configuration file
├── requirements.txt          # Python dependencies
├── README.md                 # Read Me file
├── /controllers              # HTTP route handlers
│   └── app_controller.py     # The main APP API endpoint controller
│   └── post_controller.py    # The blog posts API endpoint controller  
├── /services                 # Business logic
│   └── post_service.py       # The blog posts Business Logic   
├── /repositories             # Data access layer
│   └── post_repository.py    # The blog posts Data access layer
├── /models                   # Data models
│   └── post_model.py         # The blog posts Data model
├── /helpers                  # The helper classes
│   └── json_file_helper.py   # The Json file operation helpers
│   └── logs_helper.py        # The log generation helpers
├── /enums                    # The application enumerations
│   └── direction.py     
│   └── sort.py     
├── /data                     # Mock JSON database
│   └── posts.json            # Mock blog posts JSON data
├── /static
│   └── masterblog.json       # Swagger documentation config
└── README.md                 # Project guide
```

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

- ✅ Add PUT support for updating blog posts
- 🔐 Integrate JWT authentication
- 🔎 Full-text search support
- 🧪 Add unit & integration tests
- 🗂️ Paginate and filter posts more efficiently
- 💾 Move from JSON to SQLite or PostgreSQL backend

---

## 🧠 Author

Built by Ateet — Devoted to code, tradition, and clean design. 🚀

---

## 📜 License

This project is licensed under the MIT License. Free to use, share, and build on.

