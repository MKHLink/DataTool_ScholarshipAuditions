from backendApp import app, db
from flask import render_template, request, redirect, url_for, flash
from backendApp.forms import FacultyForm
from datetime import datetime

@app.route("/")
def index():  
    faculties = []
    
    for faculty in db.faculty.find().sort("date_created", -1):
        faculty["_id"] = str(faculty["_id"])
        faculty["date_created"] = faculty["date_created"].strftime("%m/%d/%Y, %H:%M:%S")
        faculties.append(faculty)
        
    return render_template("index.html", faculties=faculties)

@app.route("/add_faculty", methods=["GET", "POST"])
def add_faculty():
    form = FacultyForm()
    
    if form.validate_on_submit():
        faculty = {
            "schoolName": form.schoolName.data,
            "schoolDepartment": form.schoolDepartment.data,
            "firstName": form.firstName.data,
            "lastName": form.lastName.data,
            "title": form.title.data,
            "disipline": form.disipline.data,
            "email": form.email.data,
            "city": form.city.data,
            "state": form.state.data,
            "schoolUrl": form.schoolUrl.data,
            "date_created": datetime.now()
        }
        
        db.faculty.insert_one(faculty)
        
        flash("Faculty added successfully!", "success")
        
        return redirect(url_for("index"))
    
    return render_template("add_faculty.html", form=form, legend="Add Faculty")
