from flask import Flask
from sqlalchemy import SQLAlCHEMY

app = Flask(__name__)
app.config['SQLALCHEMY_DATSBASE_URI']="sqlite:///project.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlCHEMY(app)

class Todo():
    sno = ds.column(db.Integer,primary_key=True)
    title = ds.column(db.String(200),nullable=False)
    desc = ds.column(db.String(200),nullable=False)
    date_created = ds.column(db.Integer,primary_key=True)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/products")
def productpage():
    return "<p> This is product page</p>"


if __name__=="__main__":
    app.run(debug=True)