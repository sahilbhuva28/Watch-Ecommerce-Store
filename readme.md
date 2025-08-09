Watch E-commerce Store

A fully functional e-commerce platform built with Django and enhanced with django-jazzmin for a modern admin panel.
Users can browse and purchase watches; admins can manage products, categories, and orders.

📌 Features
🛒 Product management (add / edit / delete)

📂 Category management

🖼 Product images

🏷 Pricing

📦 Order management

🎨 Modern admin UI (django-jazzmin)

🛠 Tech Stack
Backend: Django

Frontend: HTML, CSS, Bootstrap

Database: SQLite (default) — can switch to PostgreSQL/MySQL

Admin Theme: django-jazzmin

📥 Installation & Setup
These commands assume your repo root contains a folder named project with the Django project (adjust if different).

1. Clone the repository
bash
Copy
Edit
git clone https://github.com/sahilbhuva28/Watch-Ecommerce-Store.git
cd Watch-Ecommerce-Store
(If your folder name contains spaces, wrap it in quotes. The clone above creates Watch-Ecommerce-Store — no spaces.)

2. Create & activate a virtual environment
Windows (PowerShell):

powershell
Copy
Edit
python -m venv venv
.\venv\Scripts\Activate.ps1
Windows (cmd):

cmd
Copy
Edit
python -m venv venv
venv\Scripts\activate
macOS / Linux:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
If you prefer a different venv name, replace venv with your choice.

3. Install dependencies
If requirements.txt is at the repo root:

bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt is in another folder, point to it with a path:

Example: requirements.txt in project/setup/requirements.txt

bash
Copy
Edit
pip install -r project/setup/requirements.txt
Example: one folder up

bash
Copy
Edit
pip install -r ../requirements.txt
Full absolute path (Windows):

powershell
Copy
Edit
pip install -r "C:\path\to\Watch-Ecommerce-Store\requirements.txt"
4. Apply migrations and run
bash
Copy
Edit
cd project
python manage.py migrate
5. Create a superuser
bash
Copy
Edit
python manage.py createsuperuser
(Do not commit or publish admin credentials in the repo — use a secure password.)

6. Run the dev server
bash
Copy
Edit
python manage.py runserver
Open:

Website: http://127.0.0.1:8000/

Admin: http://127.0.0.1:8000/admin/

⚠️ Important notes
Do not commit venv/ — it makes the repository large and unnecessary. Instead:

Add venv/ to .gitignore.

Commit requirements.txt:

bash
Copy
Edit
pip freeze > requirements.txt
Others can recreate the environment with pip install -r requirements.txt.

Example .gitignore (add to repo root):

bash
Copy
Edit
venv/
__pycache__/
*.pyc
db.sqlite3
/media/
.env
Secrets & credentials: Use environment variables or a .env file (and add .env to .gitignore). Don’t include real passwords or API keys in the README.
