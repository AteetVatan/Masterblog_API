# Masterblog API

A Flask-based API using the Repository Pattern and Service Layer, with JSON files as a mock database.

## 📂 Folder Structure
```
/masterblog_api
│── app.py                # Main entry point
│── /controllers          # API route handlers (controllers)
│    ├── post_controller.py
│── /services             # Business logic (service layer)
│    ├── post_service.py
│── /repositories         # Database interaction (repository layer)
│    ├── post_repository.py
│── /data                 # JSON storage
│    ├── data.json
│── README.md             # Project guide
```

## 🚀 Endpoints
| Method | Endpoint         | Description |
|--------|----------------|-------------|
| GET    | `/posts`       | Retrieve all posts |
| GET    | `/posts/<id>`  | Retrieve a single post |
| POST   | `/posts`       | Add a new post |
| DELETE | `/posts/<id>`  | Delete a post |

🔥 What’s Inside?
Controllers (post_controller.py): Handles HTTP requests and responses.
Services (post_service.py): Implements business logic.
Repositories (post_repository.py): Manages JSON file operations.
README.md: Explains setup, API endpoints, and future enhancements.

## 🛠 Setup & Run
```sh
pip install flask
python app.py
```
