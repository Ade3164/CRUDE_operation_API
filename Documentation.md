

# CRUD Operation API Documentation

Welcome to the documentation for the CRUD Operation API. This API allows you to perform basic CRUD (Create, Read, Update, Delete) operations on a "Persons" table in a PostgreSQL database. You can interact with this API to manage person records.

## Table of Contents

1. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
2. [API Endpoints](#api-endpoints)
   - [Get All Persons](#get-all-persons)
   - [Get Person by ID or Name](#get-person-by-id-or-name)
   - [Create a New Person](#create-a-new-person)
   - [Update a Person](#update-a-person)
   - [Delete a Person](#delete-a-person)

## Getting Started

### Prerequisites

Before using this API, ensure you have the following prerequisites:

- Node.js (v12 or higher) installed on your machine.
- PostgreSQL database installed and running.
- An environment file (`.env`) with the necessary environment variables set (see `.env.sample` for reference).

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Ade3164?tab=repositories
   ```

2. Navigate to the project directory:

   ```bash
   cd crude_operation_api
   ```

3. Install the project dependencies:

   ```bash
   npm install
   ```

4. Start the API:

   ```bash
   npm start
   ```

   The API will be accessible at `http://localhost:5000` by default.

## API Endpoints

### Get All Persons

- **URL**: `/api/persons`
- **Method**: `GET`
- **Description**: Retrieve a list of all persons in the database.
- **Response**: A JSON array containing person records.

### Get Person by ID or Name

- **URL**: `/api/persons/:param`
- **Method**: `GET`
- **Description**: Retrieve a person by their ID or name.
- **Response**: A JSON object representing the person record.

### Create a New Person

- **URL**: `/api/persons`
- **Method**: `POST`
- **Description**: Create a new person record.
- **Request Body**: JSON object with a "name" field.
- **Response**: A JSON object representing the newly created person record.

### Update a Person

- **URL**: `/api/persons/:param`
- **Method**: `PUT`
- **Description**: Update a person's name by their ID or name.
- **Request Body**: JSON object with a "name" field.
- **Response**: A JSON object representing the updated person record.

### Delete a Person

- **URL**: `/api/persons/:param`
- **Method**: `DELETE`
- **Description**: Delete a person by their ID or name.
- **Response**: A JSON object with a success message.

