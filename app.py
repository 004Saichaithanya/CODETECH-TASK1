from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Skill(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    level=db.Column(db.Integer,nullable=True)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


# @app.route('/services')
# def services():
#     return "Hello services!"

# skills = [
#     {"name": "Python", "level": 80},
#     {"name": "JavaScript", "level": 70},
#     {"name": "HTML/CSS", "level": 90},
# ]


# Route for the skills page
@app.route("/skills", methods=["GET", "POST"])
def skills_page():
    if request.method == "POST":
        # Get skill name and level from form data
        new_skill = request.form.get("skill_name")
        new_level = int(request.form.get("skill_level"))

        skills=Skill(name=new_skill,level=new_level)
        db.session.add(skills)
        db.session.commit()
        return redirect(url_for('skills_page'))
    skills=Skill.query.all()

        # Append new skill to the skills list
        # skills.append({"name": new_skill, "level": new_level})
    return render_template("skills.html", skills=skills)


@app.route("/education")
def education():
    return render_template("education.html")


@app.route("/achievements")
def achievements():
    return render_template('achievements.html')


# @app.route("/work")
# def work():
#     return "Hello work!"


@app.route("/contact")
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
