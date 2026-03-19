# 📝 Flask Blog

A lightweight blog application built with Python and Flask. This project demonstrates core Flask concepts such as routing, templates (Jinja2), forms, and in-memory data management.

---

## 🚀 Features

- **List posts** — home page displays all published posts with excerpt and metadata
- **Read post** — dedicated page for each post with full content
- **Create post** — form to write and publish new posts (title, author, content)
- **Delete post** — remove any post from the home page or detail page
- **Responsive layout** — clean dark-themed interface using HTML & CSS

---

## 🛠 Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.x | Programming language |
| Flask | Web framework (routing, templates, forms) |
| Jinja2 | HTML templating engine (included with Flask) |
| HTML + CSS | Frontend interface |

---

## 📁 Project Structure

```
flask-blog/
├── app.py               # Main application — routes and logic
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation
└── templates/
    ├── base.html        # Base layout (header, footer, styles)
    ├── index.html       # Home page — list of posts
    ├── post.html        # Post detail page
    └── new_post.html    # Form to create a new post
```

---

## ⚙️ How to Run

**1. Clone or download the project**

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the application**
```bash
python app.py
```

**4. Open in your browser**
```
http://localhost:5000
```

---

## 📌 Routes

| Method | Route | Description |
|---|---|---|
| GET | `/` | Lists all posts |
| GET | `/post/<id>` | Displays a single post |
| GET/POST | `/new` | Form to create a new post |
| POST | `/delete/<id>` | Deletes a post by ID |

---

## 🗒 Notes

- Posts are stored **in memory** (no database). Data resets when the server restarts.
- This project is intentionally simple to serve as an educational example for beginner Python students.
- Can be extended with: SQLite database, user authentication, image uploads, etc.

---

## 👩‍💻 Author

Developed as a practical task for the Kodland Python Pro tutor selection process.
