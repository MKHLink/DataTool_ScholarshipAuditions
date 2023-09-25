from flask import flash, redirect, url_for
import json
from datetime import datetime
from backendApp import app, db

collection = db['faculty']  # Replace 'your_collection_name' with your actual collection name

@app.route('/import_data', methods=['GET'])
# Function to import data if not already imported
def import_data():
    # Check if a status flag exists in the database to indicate whether import has been done
    status_flag = db.status.find_one({"import_status": "done"})
    if status_flag:
        flash("Data already imported!", "info")
        return redirect(url_for("index"))
    
    # open file and load data
    with open(r"jsonfiles\facultiesExample.json", 'r') as json_file:
        data = json.load(json_file)

    for entry in data:
        # Extract data from JSON and prepare it for insertion
        schoolName = "University of California, San Diego"  # Set the school name as per your requirements
        schoolDepartment = entry.get("department", "")
        name_parts = entry.get("name", "").split()
        firstName = name_parts[0] if len(name_parts) > 0 else ""
        lastName = name_parts[-1] if len(name_parts) > 1 else ""
        title = entry.get("title", "")
        discipline = "visual arts"  # Set the discipline as per your requirements
        email = entry.get("email", "")
        city = "La Jolla"  # Set the city as per your requirements
        state = "CA"  # Set the state as per your requirements
        schoolUrl = entry.get("link", "")
        date_created = datetime.now() # Set the date as per your requirements
        
        # Create a dictionary to insert into MongoDB
        record = {
            "schoolName": schoolName,
            "schoolDepartment": schoolDepartment,
            "firstName": firstName,
            "lastName": lastName,
            "title": title,
            "disipline": discipline,
            "email": email,
            "city": city,
            "state": state,
            "schoolUrl": schoolUrl,
            "date_created": date_created
        }

        # Insert the record into MongoDB
        collection.insert_one(record)

     # Set the status flag to indicate that the import has been done
    db.status.insert_one({"import_status": "done"})
    
    flash("Data imported successfully!", "success")
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run()
