<<<<<<< HEAD
# 🛥 Watch E-Commerce Store (Django + Jazzmin)

A fully functional e-commerce platform built with **Django** and enhanced with **django-jazzmin** for a modern, sleek admin panel.  
This project allows users to browse and purchase watches, while administrators can manage products, categories, and orders via a user-friendly admin interface.

---

## 📌 Features
- 🛒 **Product Management** – Add, edit, and delete watch products.
- 📂 **Category Management** – Organize products into categories.
- 🖼 **Product Images** – Upload and display watch images.
- 🏷 **Pricing** – Set prices for products.
- 📦 **Order Management** – Track and process customer orders.
- 🎨 **Modern Admin UI** – Powered by `django-jazzmin`.

---

## 🛠 Tech Stack
- **Backend:** Django  
- **Frontend:** HTML, CSS, Bootstrap  
- **Database:** SQLite (default) / can be switched to PostgreSQL/MySQL  
- **Admin Theme:** django-jazzmin  

---

## 📥 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/sahilbhuva28/Watch-Ecommerce-Store.git
cd Watch-Ecommerce-Store
````

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv
# For macOS/Linux
source venv/bin/activate
# For Windows
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations

```bash
python manage.py migrate
```

### 5️⃣ Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

**Default Admin Credentials:**

```bash
Username: admin
Password: test@123
```

---

## ▶ Running the Server

```bash
python manage.py runserver
```

**Open in Browser:**

```bash
Website: http://127.0.0.1:8000/
Admin:   http://127.0.0.1:8000/admin/
```

---

📸 **Admin Panel Preview (django-jazzmin)**
The admin panel comes with a modern dashboard, quick navigation, and responsive UI — making it easier for you to manage products and orders.



=======
Alright — here’s your `README.md` with **all commands and credentials inside proper fenced code boxes** so it’s neat and GitHub-friendly:

````markdown
# 🛥 Watch E-Commerce Store (Django + Jazzmin)

A fully functional e-commerce platform built with **Django** and enhanced with **django-jazzmin** for a modern, sleek admin panel.  
This project allows users to browse and purchase watches, while administrators can manage products, categories, and orders via a user-friendly admin interface.

---

## 📌 Features
- 🛒 **Product Management** – Add, edit, and delete watch products.
- 📂 **Category Management** – Organize products into categories.
- 🖼 **Product Images** – Upload and display watch images.
- 🏷 **Pricing** – Set prices for products.
- 📦 **Order Management** – Track and process customer orders.
- 🎨 **Modern Admin UI** – Powered by `django-jazzmin`.

---

## 🛠 Tech Stack
- **Backend:** Django  
- **Frontend:** HTML, CSS, Bootstrap  
- **Database:** SQLite (default) / can be switched to PostgreSQL/MySQL  
- **Admin Theme:** django-jazzmin  

---

## 📥 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/sahilbhuva28/Watch-Ecommerce-Store.git
cd Watch-Ecommerce-Store
````

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv
# For macOS/Linux
source venv/bin/activate
# For Windows
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations

```bash
python manage.py migrate
```

### 5️⃣ Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

**Default Admin Credentials:**

```bash
Username: admin
Password: test@123
```

---

## ▶ Running the Server

```bash
python manage.py runserver
```

**Open in Browser:**

```bash
Website: http://127.0.0.1:8000/
Admin:   http://127.0.0.1:8000/admin/
```

---

📸 **Admin Panel Preview (django-jazzmin)**
The admin panel comes with a modern dashboard, quick navigation, and responsive UI — making it easier for you to manage products and orders.

```

I kept **all steps** in `bash` code blocks where relevant so your README will look clean and professional when viewed on GitHub.  

Do you want me to now **add screenshot placeholders** so this README is visually appealing? That would make it look like a real e-commerce project page.
```
>>>>>>> 710d05a (refactor: separate footer into reusable template with dedicated CSS and organize index.html structure)
