# CRUD Operation API

This is a Node.js API built with Express and PostgreSQL for performing CRUD (Create, Read, Update, Delete) operations on a "Persons" table. It provides endpoints to manage individual persons in the database.

## Getting Started

To get started with this API, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Ade3164/CRUDE_operation_API

GET /api/1
Response:
{ "id": 1, "name": "John Doe" }

POST /api
Request:

{ "name": "Alice Johnson" }

response 
{ "id": 3, "name": "Alice Johnson" }

PUT /api/2
Request:
{ "name": "Updated Name" }
response:

{ "id": 2, "name": "Updated Name" }

DELETE /api/3
Response:

{ "message": "Person deleted" }.

Technologies Used

Node.js
Express.js
PostgreSQL
pg-promise
dotenv


Author

Name: Zakariyau Idris
email: Adebayoidris051@gmail.com
