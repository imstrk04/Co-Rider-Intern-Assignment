
# User Management App

## Overview

The User Management App is a web application built using Flask and MongoDB that enables users to perform CRUD (Create, Read, Update, Delete) operations on user data. This application is designed to facilitate the management of user information through a RESTful API.

## Table of Contents

- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing with Postman](#testing-with-postman)
- [Contributing](#contributing)
- [License](#license)

## Technologies

- **Backend:** Flask, Flask-PyMongo
- **Database:** MongoDB
- **Testing Tool:** Postman

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd user-management-app
   ```

2. Navigate to the `server` directory:

   ```bash
   cd server
   ```

3. (Optional) Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Ensure you have MongoDB installed and running on your machine.

## Usage

1. Start the Flask server:

   ```bash
   flask run
   ```

   The server will run at `http://localhost:5000` by default.

2. Access the application in your web browser or test it using Postman.

## API Endpoints

| Method | Endpoint                | Description                             |
|--------|-------------------------|-----------------------------------------|
| GET    | `/users`                | Retrieve a list of all users           |
| GET    | `/users/<id>`           | Retrieve a specific user by ID         |
| POST   | `/users/create`         | Create a new user                       |
| PUT    | `/users/<id>/edit`      | Update an existing user                 |
| DELETE | `/users/<id>/delete`    | Delete a user by ID                    |

### Request and Response Format

- **Create User (POST `/users/create`)**
  - **Request Body:**
    ```json
    {
      "name": "Virat Kohli",
      "email": "virat@gmail.com",
      "password": "password1"
    }
    ```

- **Get Users (GET `/users`)**
  - **Response:**
    ```json
    [
      {
        "_id": "user_id",
        "name": "Virat Kohli",
        "email": "virat@gmail.com"
      }
    ]
    ```

## Testing with Postman

1. Open Postman and create a new HTTP request for each of the API endpoints.
2. Use the appropriate HTTP method (GET, POST) for each request.
3. For POST requests, add the required headers (like `Content-Type: application/json`) and body data as shown above.
4. Send the requests and verify that the responses are correct and that the database is being updated as expected.

## Contributing

Contributions are welcome! If you would like to contribute, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Instructions for Customization

- Replace `<repository-url>` with the URL of your GitHub repository.
- You can further modify sections to include any additional information or specific instructions related to your project.
- Save this content as `README.md` in the root of your project directory.

This README will help others (and yourself) understand how to set up and use your User Management application!
