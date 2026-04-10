# Productivity Manager

A web application built with Flask that allows you to manage productivity on a task-by-task basis — add notes, sub-tasks, and related files to stay organised. Currently a work in progress, building on a tutorial foundation.

---

## Table of Contents

- [Features](#features)
- [Currently Working On](#currently-working-on)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Inspiration & Credits](#inspiration--credits)

---

## Features

- **Task Management** — Create, edit, and delete tasks
- **Notes** — Attach notes to individual tasks *(coming soon)*
- **Sub-tasks** — Break tasks into smaller actionable items *(coming soon)*
- **File Attachments** — Link related files to tasks *(coming soon)*

> ⚠️ This project is still a work in progress. Some features listed above are planned and not yet implemented.

---

## Currently Working On

The project is undergoing a significant architectural upgrade. Here's what's actively in progress:

### 🔄 Flask → FastAPI Migration

Migrating the backend from Flask to [FastAPI](https://fastapi.tiangolo.com/) to take advantage of:

- **Automatic API docs** — Swagger UI and ReDoc out of the box at `/docs` and `/redoc`
- **Async support** — non-blocking request handling for better performance
- **Type safety** — Pydantic models for request/response validation
- **Modern Python** — native support for Python type hints throughout

> The Jinja2 HTML templates will be replaced with a proper API layer, decoupling the frontend from the backend.

### 🗄️ SQLite → PostgreSQL Migration

Moving from SQLite to [PostgreSQL](https://www.postgresql.org/) to support:

- **Concurrent connections** — better suited for multi-user access
- **Production readiness** — robust, scalable storage beyond local development
- **Richer querying** — advanced SQL features and indexing
- **Cloud deployment** — compatibility with hosted DB services (e.g. Supabase, Railway, Render)

The `SQLALCHEMY_DATABASE_URI` will be updated from `sqlite:///database.db` to a PostgreSQL connection string:

```python
# New connection format
DATABASE_URL = "postgresql://user:password@localhost:5432/productivity_manager"
```

### 🎨 UI Overhaul

The current minimal interface is being redesigned with a focus on:

- **Improved layout** — cleaner task list and dashboard view
- **Responsive design** — mobile-friendly across all screen sizes
- **Component-based styling** — refactoring the existing SCSS into reusable, modular components
- **Better UX** — inline editing, drag-and-drop task ordering, and visual status indicators

---

## Tech Stack

| Technology | Purpose |
|---|---|
| [Flask](https://flask.palletsprojects.com/) | Web framework & routing |
| [Django](https://www.djangoproject.com/) | *(planned integration)* |
| SQLite | Local development database (`instance/database.db`) |
| SCSS / CSS | Styling (`static/styles.scss`, `static/styles.css`) |
| Jinja2 | HTML templating |

---

## Project Structure

```
Flask test/
├── env/                    # Virtual environment
│   ├── AUTHORS
│   ├── LICENSE.txt
│   ├── pyvenv.cfg
│   ├── README.rst
│   └── tox.ini
├── instance/
│   └── database.db         # SQLite database
├── static/
│   ├── styles.css          # Compiled CSS
│   ├── styles.css.map      # Source map
│   └── styles.scss         # SCSS source
├── templates/
│   ├── base.html           # Base layout template
│   ├── edit.html           # Task edit page
│   └── index.html          # Main task list page
├── app.py                  # Main Flask application
├── README.md               # This file
└── requirements.txt        # Python dependencies
```

---

## Installation

### Prerequisites

- Python 3.x ([Download](https://www.python.org/downloads/))
- pip (comes bundled with Python)
- Git

### Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/productivity-manager.git
   cd productivity-manager
   ```

2. **Create and activate a virtual environment**

   ```bash
   # Windows
   python -m venv env
   env\Scripts\activate

   # macOS / Linux
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Initialise the database**

   The database is created automatically on first run. If you need to initialise it manually, open a Python shell:

   ```python
   from app import db
   db.create_all()
   ```

5. **Run the application**

   ```bash
   python app.py
   ```

6. **Open in your browser**

   Navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Configuration

Configuration is managed directly in `app.py`. Key settings to customise:

| Setting | Description | Default |
|---|---|---|
| `SECRET_KEY` | Session security key — **change this in production** | `'dev'` |
| `SQLALCHEMY_DATABASE_URI` | Database connection string | `sqlite:///database.db` |
| `DEBUG` | Enable/disable Flask debug mode | `True` |

Example configuration block in `app.py`:

```python
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['DEBUG'] = True
```

> 🔒 **Important:** Never commit a real `SECRET_KEY` to version control. Use environment variables for production deployments.

---

## Usage

### Creating a Task

1. Open the app at [http://127.0.0.1:5000](http://127.0.0.1:5000)
2. Fill in the task form on the main page
3. Click **Submit** to save

### Editing a Task

1. Click the **Edit** button next to any task
2. Modify the details on the edit page (`/edit/<id>`)
3. Click **Save** to apply changes

### Deleting a Task

1. Click the **Delete** button next to the task you want to remove
2. The task will be permanently deleted

---

## Troubleshooting

### The app won't start

- Make sure your virtual environment is activated
- Confirm all dependencies are installed: `pip install -r requirements.txt`
- Check that port 5000 is not already in use. If it is, run on a different port:
  ```bash
  flask run --port 5001
  ```

### Database errors

- Delete `instance/database.db` and restart the app to reset the database
- Ensure the `instance/` folder exists and has write permissions

### SCSS styles not updating

- Recompile the SCSS manually. If you have Sass installed:
  ```bash
  sass static/styles.scss static/styles.css
  ```
- Or use the VS Code **Watch Sass** extension (visible in the status bar)

### Changes not reflecting in the browser

- Hard refresh your browser: `Ctrl + Shift + R` (Windows/Linux) or `Cmd + Shift + R` (macOS)
- Ensure Flask's debug mode is enabled so the server reloads on file changes

---

## Contributing

Contributions are welcome! Since this is a learning project, feel free to suggest improvements or fixes.

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit: `git commit -m "Add your feature"`
4. Push to your branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

Please keep pull requests focused — one feature or fix per PR.

---

## License

This project is licensed under the terms found in `env/LICENSE.txt`. See that file for full details.


Big thanks to Josh for the clear and beginner-friendly walkthrough!

---

*Built by Sihle Dlamini
