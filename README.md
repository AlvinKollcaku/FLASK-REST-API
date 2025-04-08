# Flask REST API

This project is a REST API built using Flask, designed for secure and efficient data handling with seamless database migrations. It integrates JWT-based authentication, object-relational mapping with SQLAlchemy, data serialization/deserialization with Marshmallow, and containerization with Docker.

## Technologies Used

- **Flask**: Lightweight Python web framework for building the API.
- **SQLAlchemy**: ORM (Object Relational Mapper) for database modeling and queries.
- **Marshmallow**: Library for object serialization and validation.
- **Flask-Migrate**: Extension for handling database migrations using Alembic.
- **Alembic**: Database migration tool integrated with SQLAlchemy.
- **JWT Authentication**: JSON Web Tokens for secure user authentication.
- **Docker**: Containerization for environment consistency and easier deployment.

## Project Features

- **JWT Authentication**: Secure API endpoints with JSON Web Tokens for user authentication and authorization.
- **SQLAlchemy ORM**: Database models and relationships managed via SQLAlchemy.
- **Data Validation with Marshmallow**: All incoming and outgoing data is validated and serialized with Marshmallow schemas.
- **Database Migrations**: To manage database versioning and migrations using Flask-Migrate and Alembic.
- **Dockerized Setup**: The API is containerized for easier deployment and environment consistency across development, testing, and production.

## Database schema
![image](https://github.com/user-attachments/assets/3a8f546b-0e2d-4f49-8770-70ccdb809c39)

## Endpoints handled by the API

![image](https://github.com/user-attachments/assets/92e7ba33-db78-4237-8351-694f7c6f9ca8)

# Walkthrough

## 1. User Registers

**Request**

![Registration Request](https://github.com/user-attachments/assets/28f57a9b-a5c3-4418-86b4-abe1a004b936)

**Response**

![Registration Response](https://github.com/user-attachments/assets/3ccf64f5-6a58-440f-808e-bfeb46b56a3f)

---

## 2. User Logs In and Receives the Access Token

**Request**

![Login Request](https://github.com/user-attachments/assets/0812decd-9122-4c88-8ae8-760e0d549afd)

**Response**

![Login Response](https://github.com/user-attachments/assets/6e749809-cfac-44cb-b9e4-070be8fd750f)

---

## 3. Retrieve the User

![Get User](https://github.com/user-attachments/assets/036b474a-5191-4da7-84ff-43820d4ac32b)

---

## 4. Create an Event (Logged-in User)

![Create Event](https://github.com/user-attachments/assets/d3b79f94-5dff-4350-9bd8-e7901cec7a8d)

---

## 5. Modify the Event (Created by the Same User)

![Modify Event](https://github.com/user-attachments/assets/243f4286-c6da-4ada-959a-c4d9d63725eb)

---

## 6. Only the Event Creator Can Modify/Delete

![Unauthorized Modification](https://github.com/user-attachments/assets/565c2a1f-72e5-4900-83ce-88e83e43e7d2)

---

## 7. Create a Tag

![Create Tag](https://github.com/user-attachments/assets/6c08283f-cb36-4fac-b7e6-13697cdc1e9d)

---

## 8. Assign a Tag to an Event

![Assign Tag](https://github.com/user-attachments/assets/08e8d9f2-32d3-4f77-a544-516d1bae285c)

---

## 9. Receive RSVP for an Event

![RSVP](https://github.com/user-attachments/assets/da07c6c2-b1d0-4d19-a9e6-cb6b386feaea)

---

## 10. Other Endpoints

Deletion and updating work similarly as shown in the examples above.















