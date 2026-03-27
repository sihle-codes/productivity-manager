# Imports
from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_scss import Scss
from datetime import datetime

# App Setup
app = Flask(__name__)
Scss(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db" # Link a database using SQL Alchemy
db = SQLAlchemy(app) # SQL Alchemy Object

# Data Class ~ Row of Data
class MyTask(db.Model): # db.Model represents 1 row of data. Acts like a template
    # instance variables represent columns
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    complete = db.Column(db.Integer, default=0)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    
    # if printed, will return this
    def __repr__(self) -> str:
        return f"Task {self.id}"


# Routes to Webpages
# NB! Routes must match HTML

# Home Page
@app.route("/", methods=["POST","GET"]) # methods parameter defines what HTTP request methods can be used
def index():
    # Add a Task
    if request.method == "POST":
        current_task = request.form['content'] # Link to 'content' form in index.html
        new_task = MyTask(content=current_task)
        try:
            db.session.add(new_task) # Adds row to DB using content from form
            db.session.commit()
            return redirect("/") # Sends back to homepage
        except Exception as e:
            print(f"ERROR:{e}")
            return f"ERROR:{e}"
        
    # See all current tasks
    else:
        tasks = MyTask.query.order_by(MyTask.created).all() # SELECT * FROM Tasks ORDER BY created
        return render_template("index.html", tasks=tasks) # Use HTML template and available DB
    
# Delete a Task
@app.route("/delete/<int:id>")
def delete(id:int): # Based on ID, delete task
    delete_task = MyTask.query.get_or_404(id)
    try: # db.session creates temp connection to DB
        db.session.delete(delete_task) # Deletes row from DB 
        db.session.commit() # commit works like git commit
        return redirect("/") # Sends back to homepage
    except Exception as e:
        return f"ERROR:{e}"
    
# Edit a Task
@app.route("/edit/<int:id>", methods=["GET", "POST"]) 
def edit(id:int):
    task = MyTask.query.get_or_404(id)
    if request.method == "POST":
        task_content = request.form['content']
        try:
            db.session.commit()
            return redirect("/")
        except Exception as e:
            return f"ERROR:{e}"
    else:
        return render_template('edit.html', task=task)




# Runner and Debugger
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)