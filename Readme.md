# ✅ Flask To-Do Web Application

## 📌 Overview

This is a simple yet powerful **Flask-based To-Do web application** that allows users to create, update, and delete tasks efficiently. The project demonstrates CRUD operations using Flask, SQLite database, and a clean HTML/CSS frontend.

---

## 🚀 Features

* ➕ Add new tasks
* ✏️ Update existing tasks
* ❌ Delete tasks
* 📋 View all tasks in a list
* 💾 SQLite database integration
* 🎨 Simple and clean UI using HTML/CSS

---

## 🛠️ Tech Stack

* Python
* Flask
* SQLite
* HTML
* CSS

---

## 📁 Project Structure

```
TO_DO/
│
├── app.py
├── instance/
│     └── To_Do.db
│
├── static/
│     └── style.css
│
├── templates/
│     ├── base.html
│     ├── index.html
│     └── update.html
│
├── __pycache__/
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/flask-todo-app.git
```

### 2. Navigate to project folder

```bash
cd TO_DO
```

### 3. Install dependencies

```bash
pip install flask
```

### 4. Run the application

```bash
python app.py
```

### 5. Open in browser

```
http://127.0.0.1:5000
```

---

## 🧠 How It Works

1. User opens the web app
2. Tasks are stored in SQLite database
3. Flask handles routing and CRUD operations
4. Templates render data dynamically
5. User can add/update/delete tasks in real-time

---

## 🗄️ Database

* Database used: SQLite (`To_Do.db`)
* Table stores task information (ID, title, status)

---

## 🎯 Future Improvements

* User authentication (login/signup)
* Due dates & reminders
* Priority-based tasks
* REST API version
* React frontend integration
* Deployment on cloud (Render/Heroku)

---

## 👨‍💻 Author

Developed by **Khushi Agarwal**

---

## ⭐ Note

This project is a beginner-friendly Flask CRUD application to understand backend development and database integration.
