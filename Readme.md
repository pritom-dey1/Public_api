# Dummy Data API for Testing

This repository provides **dummy data APIs** for testing and development purposes.  
Developers can use the provided endpoints to fetch fake data for users and products, making it easier to test their frontend, backend, or integration workflows without relying on real data.

---

## 🚀 Purpose

- Provide ready-to-use **dummy users and products** for testing.
- Help developers **build, test, and prototype** applications without using sensitive or real data.
- Support **GET requests** for fetching lists and single items.
- Support **limited fetch** via query parameters (e.g., `?limit=10`) for testing pagination.

---

## 📦 Available APIs

### Users

- **GET all users**:  
  ```
  https://public-api-3.onrender.com/api/users/
  ```
- **GET single user**:  
  ```
  https://public-api-3.onrender.com/api/users/<id>/
  ```
- **Optional limit**:  
  ```
  https://public-api-3.onrender.com/api/users/?limit=12
  ```
  Returns the first 12 users.

> **Note:** Users API is **read-only**. No create/update/delete allowed.

---

### Products

- **GET all products**:  
  ```
  https://public-api-3.onrender.com/api/products/
  ```
- **GET single product**:  
  ```
  https://public-api-3.onrender.com/api/products/<id>/
  ```
- **Optional limit**:  
  ```
  https://public-api-3.onrender.com/api/products/?limit=10
  ```
  Returns the first 12 products.

- **Note:** Product API is **read-only**. No create/update/delete allowed.


---

## 🔧 Data Included

- **Users**: 30 dummy users with `id`, `name`, `email` , `description` , `designation` , `photo_url` , `experience` , `salary` fields.
- **Products**: 30 dummy products with `id`, `name`, `price`, `category`, `photo_urls`, `ratings`, `description`, and `in_stock` fields.

---

## 📜 License

This repository is for **testing and learning purposes only**.  
Feel free to fork and modify for your own projects.

