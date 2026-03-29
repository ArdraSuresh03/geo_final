# 🌍 Geo Location User Search API

## 📌 Project Description

This project is a simple Django REST API where users can:

* Add their location (latitude & longitude)
* Define a service radius
* Search for nearby users based on location

---

## 🚀 Features

* Add user with location
* Get list of users
* Search nearby users using latitude & longitude
* Distance calculation

---

## 🛠️ Tech Stack

* Python
* Django
* Django REST Framework
* SQLite
* HTML + JavaScript (Frontend)

---

## 📂 API Endpoints

### ➤ Add User

POST `/api/users/`

Example:

```
{
  "name": "Ardra",
  "lat": 10,
  "long": 76,
  "service_radius": 50
}
```

---

### ➤ Get Users

GET `/api/users/list/`

---

### ➤ Search Users

GET `/api/search/?lat=10&lon=76`

---

## 💻 How to Run

```bash
pip install django djangorestframework
python manage.py migrate
python manage.py runserver
```

---

## 👤 Author

Ardra

---
