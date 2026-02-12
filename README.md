# FastAPI Product API 🚀

A simple and practical backend API built with **FastAPI + PostgreSQL** for managing products.  
This project focuses on clean structure, proper database handling, and real-world API features like search, pagination, and filtering.

---

## 👤 Author

**Aman Raj**  
B.Tech CSE | Backend Development Enthusiast  
FastAPI • Python • PostgreSQL • REST APIs  

---

## 🌐 Live Demo

👉 https://fastapi-product-api-v3.onrender.com  
👉 Swagger Docs: /docs  

---

## 📌 About the Project

This API allows users to perform full CRUD operations on products and includes additional features such as:

- Search products by name  
- Pagination support  
- Filter by price  
- Input validation  
- Database integration with PostgreSQL  

The main goal of this project was to understand how a real backend application is structured and deployed.

---

## 🛠 Tech Stack

- Python  
- FastAPI  
- PostgreSQL  
- SQLAlchemy  
- Pydantic  
- Uvicorn  

---

## 📂 Project Structure

```
FastAPI_phase-1/
│── app/
│   ├── routers/
│   │     └── product.py
│   ├── main.py
│   ├── database.py
│   ├── database_model.py
│   └── models.py
│
│── .env
│── requirements.txt
│── render.yaml
│── README.md
```

---

## 🚀 Features

### CRUD Operations
- Create a product  
- Get all products  
- Get product by ID  
- Update product  
- Delete product  

### Extra Functionalities
- Search by product name  
- Pagination  
- Filter products by minimum price  
- Validation for price & quantity  

---

## 🔗 API Endpoints

### Get All Products  
`GET /product`

### Get Product by ID  
`GET /product/{id}`

### Add New Product  
`POST /product`

Sample Request Body:

```json
{
  "id": 1,
  "name": "phone",
  "description": "budget phone",
  "price": 699.99,
  "quantity": 50
}
```

### Update Product  
`PUT /product/{id}`

### Delete Product  
`DELETE /product/{id}`

### Search by Name  
`GET /product/search/{name}`

### Pagination  
`GET /product/page/?page=1&limit=5`

### Price Filter  
`GET /product/price/?min_price=100`

---

## ⚙ Setup Locally

1. Clone the repository  
2. Create a virtual environment  
3. Install dependencies  

```bash
pip install -r requirements.txt
```

4. Add a `.env` file  

```
DATABASE_URL=your_postgres_url
```

5. Run the server  

```bash
uvicorn app.main:app --reload
```

6. Open in browser  
http://127.0.0.1:8000/docs  

---

## 🧠 What I Learned

- Building real APIs using FastAPI  
- Connecting FastAPI with PostgreSQL  
- Structuring backend projects  
- Writing clean and reusable code  
- Handling validations and errors  
- Deploying backend applications  

---

### Thanks for checking out my project!
