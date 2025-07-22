# Role-Based Login System in Django with MySQL

A secure, scalable **Django web application** that implements **role-based login authentication** using **MySQL as the database backend**. This project supports user roles like **Counsellor**, **HOD**, **Accountant**, and **Principal**, and redirects each to a custom dashboard after login.
Perfect for college or institutional **admission workflows**, internal panels, or any system requiring controlled role access.


## Key Features

- **Role-based authentication** using Django’s built-in `User` model
- Extend user data with a custom `UserProfile` model
- Secure login with role detection and dashboard redirection
- Role & user management via the Django Admin Panel
- MySQL integration for production-ready relational storage
- Environment variables for configuration using `python-decouple`
- Clean, modular app structure for easy scalability


## Screenshots

<img width="1875" height="708" alt="image" src="https://github.com/user-attachments/assets/482131ad-d5df-4af4-9fba-ff75b94c3135" />
<img width="362" height="223" alt="image" src="https://github.com/user-attachments/assets/cfb8c2ef-892e-419d-8415-2bd0364e173d" />
<img width="592" height="223" alt="image" src="https://github.com/user-attachments/assets/58a13168-94c3-427a-803a-0097a01f769f" />


## Project Structure

<img width="442" height="398" alt="image" src="https://github.com/user-attachments/assets/6eccea7f-5ea0-4663-9fbf-9a003c448cf0" />

### Project Root (rolebasedlogin/)
| File         | Purpose                                                                                                    |
| ------------ | ---------------------------------------------------------------------------------------------------------- |
| `.env`       | Stores environment variables like `DB_NAME`, `DB_USER`, `SECRET_KEY`. Not tracked by Git (sensitive info). |
| `.gitignore` | Tells Git which files/folders to ignore (e.g. `__pycache__`, `.env`, `*.pyc`).                             |
| `manage.py`  | Command-line utility to run/manage your Django project (e.g. `runserver`, `migrate`, `createsuperuser`).   |
| `README.md`  | Markdown file for project documentation on GitHub.                                                         |

### rolebasedlogin/ (project folder)
| File                  | Purpose                                                                                         |
| --------------------- | ----------------------------------------------------------------------------------------------- |
| `__init__.py`         | Marks the folder as a Python package.                                                           |
| `settings.py`         | Django project settings (installed apps, DB config, middleware, etc).                           |
| `urls.py`             | Root URL routing configuration. Includes URLs from the `users` app.                             |
| `asgi.py` / `wsgi.py` | Entry points for serving the app with ASGI/WSGI servers in production. Leave untouched for now. |


### users/ (your app)
| File            | Purpose                                                                              |
| --------------- | ------------------------------------------------------------------------------------ |
| `__init__.py`   | Marks the `users` folder as a Python package.                                        |
| `admin.py`      | Registers `UserProfile` in Django Admin to assign roles to users.                    |
| `apps.py`       | Django app config. Auto-generated. Rarely changed.                                   |
| `decorators.py` | Custom decorators like `@role_required` to restrict access by user role.             |
| `forms.py`      | Contains `LoginForm` or any future custom forms.                                     |
| `models.py`     | Defines `UserProfile` model for storing roles (counsellor, hod, etc.).               |
| `signals.py`    | Automatically creates a `UserProfile` when a `User` is created (via Django signals). |
| `tests.py`      | Placeholder for unit tests. You can ignore for now unless writing tests.             |
| `urls.py`       | Routes app-specific URLs like `/user/login`. Included in main `urls.py`.             |
| `views.py`      | Handles requests/responses. Contains login logic and role-based redirection.         |



## Getting Started

### 1. Clone the Repository
git clone https://github.com/yourusername/rolebasedlogin.git
cd rolebasedlogin

### 2. Set Up Environment Variables
Create a .env file in the root directory with your database credentials:
```
DB_NAME=your_db_name
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
```

### 3. Install Dependencies
pip install Django mysqlclient python-decouple

### 4. Run Migrations & Create Superuser
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

### 5. Start Development Server
python manage.py runserver

Visit: http://localhost:8000/user/


## User Roles & Access
Each user must be assigned a role through the Django Admin Panel.

| Role       | URL Path                      | Access Page                      |
| ---------- | ----------------------------- | -------------------------------- |
| Counsellor | `/user/counsellor_dashboard/` | Student enquiry & basic form     |
| HOD        | `/user/hod_dashboard/`        | Department-level decisions       |
| Accountant | `/user/accountant_dashboard/` | Payment verification             |
| Principal  | `/user/principal_dashboard/`  | Final approval & admission print |


## How It Works
- Admin creates a user in the Django Admin Panel.
- A UserProfile is auto-generated via signals.
- Admin assigns a role (e.g., counsellor, hod).
- On login, user is authenticated and redirected to a role-specific dashboard.


##  Role-Based View Protection
Use the @role_required(['role1', 'role2']) decorator to restrict views:
```
@role_required(['hod'])
def hod_dashboard(request):
```


## Contributing
Pull requests are welcome! If you have ideas for new features or want to improve role handling, fork the repo and submit a PR.


### If this project helps you, please give it a ⭐ on GitHub to support it!
