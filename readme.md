🛥 Watch E-Commerce Store (Django + Jazzmin)
A fully functional e-commerce platform built with Django and enhanced with django-jazzmin for a modern, sleek admin panel.
This project allows users to browse and purchase watches, while administrators can manage products, categories, and orders via a user-friendly admin interface.

📌 Features


🛒 Product Management – Add, edit, and delete watch products.


📂 Category Management – Organize products into categories.


🖼 Product Images – Upload and display watch images.


🏷 Pricing – Set prices for products.


📦 Order Management – Track and process customer orders.


🎨 Modern Admin UI – Powered by django-jazzmin.



🛠 Tech Stack


Backend: Django


Frontend: HTML, CSS, Bootstrap


Database: SQLite (default) / can be switched to PostgreSQL/MySQL


Admin Theme: django-jazzmin



📥 Installation & Setup
1️⃣ Clone the Repository
bashCopyEditgit clone https://github.com/sahilbhuva28/Watch-Ecommerce-Store.git
cd Watch-Ecommerce-Store

2️⃣ Create & Activate Virtual Environment
bashCopyEditpython -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows

3️⃣ Install Dependencies
bashCopyEditpip install -r requirements.txt

4️⃣ Apply Migrations
bashCopyEditpython manage.py migrate

5️⃣ Create Superuser (Optional)
bashCopyEditpython manage.py createsuperuser

Default Admin Credentials:
makefileCopyEditUsername: admin
Password: test@123


▶ Running the Server
bashCopyEditpython manage.py runserver

Then open your browser and go to:


🌐 Website: http://127.0.0.1:8000/


🔑 Admin Panel: http://127.0.0.1:8000/admin/



📸 Admin Panel Preview (django-jazzmin)
The admin panel comes with a modern dashboard, quick navigation, and responsive UI — making it easier for you to manage products and orders.