from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/dhenry3091/sites/etsydemo/tmp/database.db'
db = SQLAlchemy(app)

class Listing(db.Model):
    __tablename__ = "listing"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    description = db.Column(db.String(200))
    price = db.Column(db.Float(2))

@app.route('/')
def index():
    results = Listing.query.filter(1==1).all()
    return render_template ('index.html', listings= results)

@app.route('/about')
def about():
    return render_template ('about.html')

@app.route('/contact')
def contact():
    return render_template ('contact.html')