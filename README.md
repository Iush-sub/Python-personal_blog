# PERSONAL BLOG (FLASK PROJECT)

A simple personal blog website application built using python Flask,where users can view blog posts and an admin can create,edit and manage post using json-based storage system.
---

## Features

- Home page
- Blog listing page
- Individual blog post pages
- Simple admin panel (no authentication yet)
- Create new blog posts
- Edit existing posts
- JSON-based data storage
---

## Tech Stack

- Python 
- Flask 
- HTML (Jinja templates)
- JSON (data storage)
---

## Project Structure
personal_blog/
│
├── app.py
├── posts.json
│
├── templates/
│ ├── home.html
│ ├── about.html
│ ├── blog.html
│ ├── post.html
│ ├── admin.html
│ └── edit.html
│
└── .venv/
---

##  How It Works

- Blog posts are stored in `posts.json`
- Flask reads data from JSON and passes it to templates
- `/blog` shows all posts
- `/blog/<id>` shows individual post
- Admin panel allows creating and editing posts
---

##  How to Run

### 1. Create virtual environment
python -m venv .venv
### 2. Activate it
.venv\Scripts\activate (for windows)
### 3. Install Flask
.venv\Scripts\activate 
### 4. Run the app
python app.py
### 5. Open in browser
http://localhost:8000

---

## Future Improvements
- Add login system for admin
- Add delete post feature
- Use database instead of JSON
- Improve UI with CSS
- Add categories and tags

---

## Project Roadmap
This project is based on the Personal Blog webapp project roadmap:

https://roadmap.sh/projects/personal-blog

---
## Author
Aayush Subedi








