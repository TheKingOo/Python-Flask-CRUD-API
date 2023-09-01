# Flask CRUD API for Data Management

This Flask-based API project provides Create, Read, Update, and Delete (CRUD) functionality for data stored in a MySQL database. You can use this API as a foundation for various data management tasks, making it suitable for a wide range of applications.

## Prerequisites

Before you begin, ensure you have the following prerequisites installed:

- Python 3.x
- Flask
- pymysql
- json (usually comes with Python)
- Other required libraries (install using `pip install`)

## Setting up the Development Environment

1. Clone this repository to your local machine
2. Create a virtual environment:
 ```
python3 -m venv venv
```  
3. Activate your virtual environment :
   
- On Windows:
```
venv\Scripts\activate
```
- On macOS and Linux:
```
source venv/bin/activate
```
3. Install required libraries:
```
pip install Flask pymysql
```

## Configuration
In both `db.py` and `app.py`, you'll need to configure the database connection details. Open these files and fill in the following information:
```python
# db.py
import pymysql

conn = pymysql.connect(
    host="your_mysql_host",
    user="your_mysql_username",
    password="your_mysql_password",
    database="your_database_name",
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

```
```python
# app.py
from flask import Flask , request , jsonify
import json
import pymysql


app = Flask(__name__)


# Database connection configuration
def db_connection():
    conn = None
    try:
        conn = pymysql.connect(host="your_mysql_host",
    			       	user="your_mysql_username",
                               	password="your_mysql_password",
                               	database="your_database_name",
                               	charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    except pymysql.error as e :
        print(e)
    return conn

# Other API code...

```
## Running the API
To run the API, execute the following command:
```
python app.py
```
The API will be accessible at `http://localhost:5000`.

## API Endpoints
- **GET /items:** Retrieve all items.
- **GET /items/{id}:** Retrieve an item by its ID.
- **POST /items:** Create a new item.
- **PUT /items/{id}:** Update an item by its ID.
- **DELETE /items/{id}:** Delete an item by its ID.
  
## Example Data: "Autos"
In this project, we've used a sample database named "autos" as an illustrative example. This dataset includes the following fields:
- **`id_autos:`** An auto's unique identifier.
- **`id_parking:`** An identifier representing the parking location.
- **`matricule:`** The vehicle's registration number.
  
 Please note that you can customize the database schema to suit your specific requirements. The provided example serves as a starting point for understanding the CRUD operations implemented in this Flask API. To adapt this project to your needs, you can modify the database name and schema in the `db.py` file .
  
## Contributions
Contributions are welcome! If you'd like to enhance or extend this Flask CRUD API, feel free to submit pull requests or report issues. This project is open to collaboration and improvement.
