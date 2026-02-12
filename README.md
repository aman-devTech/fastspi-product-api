FastAPI Product API 🚀
A simple and practical backend API built with FastAPI + PostgreSQL for managing products.
This project focuses on clean structure, proper database handling, and real-world API features like search, pagination, and filtering.

👤 Author
Aman Raj
B.Tech CSE | Backend Development Enthusiast
FastAPI • Python • PostgreSQL • REST APIs

🌐 Live Demo
👉 https://fastapi-product-api-v3.onrender.com
👉 Swagger Docs: /docs

📌 About the Project
This API allows users to perform full CRUD operations on products and includes additional features such as:
Search products by name
Pagination support
Filter by price
Input validation
Database integration with PostgreSQL
The main goal was to understand how a real backend works — beyond just writing endpoints.

🛠 Tech Stack
Python
FastAPI
PostgreSQL
SQLAlchemy
Pydantic
Uvicorn

📂 Project Structure
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

🚀 Features
1. CRUD Operations
Create a product
Get all products
Get product by ID
Update product
Delete product

2. Extra Functionalities
Search by product name
Paginatio
Filter products by minimum price
Validation for price & quantity

🔗 API Endpoints

➤ Get All Products
GET /product

➤ Get Product by ID
GET /product/{id}

➤ Add New Product
POST /product

Sample Body
{
  "id": 1,
  "name": "phone",
  "description": "budget phone",
  "price": 699.99,
  "quantity": 50
}

➤ Update Product
PUT /product/{id}

➤ Delete Product
DELETE /product/{id}

➤ Search by Name
GET /product/search/{name}

➤ Pagination
GET /product/page/?page=1&limit=5

➤ Price Filter
GET /product/price/?min_price=100

⚙ Setup Locally
Clone the repo
Create virtual environment
Install dependencies
pip install -r requirements.txt
Add .env file
DATABASE_URL=your_postgres_url
Run the server
uvicorn app.main:app --reload

Open in browser
👉 http://127.0.0.1:8000/docs

🧠 What I Learned
Building real APIs using FastAPI
Connecting FastAPI with PostgreSQL
Structuring backend projects
Writing clean and reusable code
Handling validations and errors
Deploying backend on Render

🚧 Phase 2 Plan
Next improvements I plan to add:
JWT Authentication
User module
Role-based access
Better logging
Unit tests
Docker support

Thanks for checking out my project! 😊