
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABSASE_URI'] = 'mysql+mysqconnector://root:root@127.0.0.1/student'
app.config['SQLALCHEMY_TRACK_MODIFCATIONS'] = False

db = SQLAlchemy(app)

class Students(db.Model):
    __tablename__ = 'students'
    id = db.column(db.Integer, primary_key=True)
    student_number = db.column(db.String(20), nullable=False)
    first_name = db.column(db.String(30), nullable=False)
    middle_name = db.column(db.String(30), nullable=False)
    last_name = db.column(db.String(30), nullable=False)
    gender = db.column(db.Integer(2), nullable=False)
    birthday = db.Column(db.Date, nullable=False)

    def to_dict(self):
        return {
            "id":self.id,
            "student_number":self.student_number,
            "first_name":self.first_name,
            "middle_name":self.middle_name,
            "last_name": self.last_name,
            "gender": self.gender,
            "birthday": self.bithday.strftime("%Y-%m-%d")
        }
    
    @app.route("/students" , methods="GET")
    def get_students():
        students = Students.query.limit(100)
        return jsonify(
            {
                "success": True, "data":[student.to_dict() for student in students]
            }
        ), 200
    
            
    
if __name__=='__main__':
    
    app.run(debug=True) 