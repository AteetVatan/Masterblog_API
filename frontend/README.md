# 🌐 Masterblog Frontend

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
python app.py
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

Crafted with simplicity and tradition by Ateet The AI Expert. Merging backend structure with frontend finesse. 🚀

---

## 📜 License

MIT License – Free to use, modify, and distribute.

