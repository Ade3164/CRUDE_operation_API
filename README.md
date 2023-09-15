 My Node.js CRUD API

This is a simple Node.js CRUD (Create, Read, Update, Delete) API using Express.js and PostgreSQL for database storage. It allows you to manage a list of persons with their names and perform basic CRUD operations on them.

 Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes.

Prerequisites

Before you begin, ensure you have met the following requirements:

- Node.js and npm (Node Package Manager) installed on your machine.
- PostgreSQL database installed locally or a connection to a remote PostgreSQL database.
- A text editor or IDE for code editing (e.g., Visual Studio Code).

 Installation

Clone the repository:

   ```bash
   git clone https://github.com/yourusername/my-node-crud-api.git

   Navigate to the project directory:

bash
Copy code
cd my-node-crud-api
Install the project dependencies:

bash
Copy code
npm install
Create a .env file in the root directory and configure your PostgreSQL database connection. Here's an example:

env
Copy code
DATABASE_URL=your_database_connection_string
Start the server:

bash
Copy code
npm start
The API should now be running locally at http://localhost:5000.

API Endpoints
GET /api/persons: Retrieve a list of all persons.
GET /api/persons/:id: Retrieve a person by ID.
GET /api/persons?name={person_name}: Retrieve a person by name.
POST /api/persons: Create a new person.
PUT /api/persons/:id: Update a person by ID.
DELETE /api/persons/:id: Delete a person by ID.
Usage
You can use a tool like Postman to interact with the API endpoints.

Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow the standard GitHub fork and pull request process.

License
This project is licensed under the MIT License - see the LICENSE.md file for details.

Author: Idris  Zakariyau


