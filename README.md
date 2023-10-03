# Mongodb back-end and Flask front-end

## Overview

[![video demonstration](https://img.youtube.com/vi/JqyL-SQhe5w/0.jpg)](https://youtu.be/JqyL-SQhe5w)

### mongodb cheat sheet:

[MongoDB Cheat Sheet](https://www.mongodb.com/developer/products/mongodb/cheat-sheet/)

This is a web application built using Flask and MongoDB that provides a simple interface to display and add new teachers. It also includes a script to extract JSON file content and store it in MongoDB.

## Features

- Display a list of teachers.
- Add new teachers to the database.
- Import data from a JSON file to MongoDB.

## Getting Started

### Prerequisites

- Python 3.x installed
- MongoDB installed and running
- Flask installed (`pip install Flask`)
- pymongo library installed (`pip install pymongo`)

### Installation

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/MKHLink/DataTool_ScholarshipAuditions.git
   ```

2. Change into the project directory:

   ```
   cd backend
   ```

3. Install the required Python packages:

   ```
   pip install -r requirements.txt
   ```

4. Set up MongoDB:
   - Make sure MongoDB is running on your local machine or provide a connection string in your Flask app.
   - Set up the username and password on __init__.py

### Usage

1. Start the Flask application:

   ```
   python run.py
   ```

2. Open your web browser and access the application at `http://localhost:5000`.

3. Use the web interface to view the list of teachers and add new teachers.

### Importing Data

To import data from a JSON file into MongoDB, you can use the included example script. Modify the script and JSON file path as needed.

At backend/jsonfiles

## Folder Structure

- `templates/`: HTML templates for the web pages.
- `backendApp/`: Backend code including the Flask app and MongoDB connection.
- `backend/jsonfiles/facultiesExample.json`: Script to import data from a JSON file to MongoDB.

## Acknowledgements

- Thank you to the Flask and MongoDB communities for providing excellent documentation and resources.

```

You should customize the sections like "Overview," "Features," "Getting Started," "Installation," "Usage," and "Folder Structure" to match your specific application. Additionally, you may want to include information about any additional features, database configurations, and deployment instructions if applicable.
