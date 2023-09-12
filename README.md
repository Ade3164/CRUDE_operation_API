CRUDE OPERATION API(Second stage HNG intership task)

**Description:** 
This API provides CRUD (Create, Read, Update, Delete) operations for managing a collection of persons. It allows you to add, retrieve, update, and delete person records.

 API Endpoints

- **GET /api/persons**: Retrieve a list of all persons.
- **GET /api/persons/{id or name}**: Retrieve a person by their ID or name.
- **POST /api/persons**: Create a new person record.
- **PUT /api/persons/{id}**: Update an existing person record by ID.
- **DELETE /api/persons/{id}**: Delete a person record by ID.

 Usage

- Use the API endpoints with appropriate HTTP methods to perform CRUD operations on person records.
- JSON data is expected for POST and PUT requests.
- Handle errors gracefully by checking the response status code and message.

Getting Started

1. Clone this repository.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Configure the database connection settings in `config.py`.
4. Start the API server by running `python app.py`.

 Database Configuration

- Modify the `config.py` file to specify your MySQL database connection details.
- Ensure that your MySQL server is running and the database schema is set up.

 Dependencies

- Flask: Web framework for building the API.
- MySQL Connector: Python driver for connecting to MySQL databases.
- Requirement.txt
License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

 Author

name: Idris Zakariyau
mail: adebayoidris051@gmail.com


