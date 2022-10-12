from flask  import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://trello_dev:password123@127.0.0.1:5432/trello'

db= SQLAlchemy(app)

class Card(db.Model):
    __tablename__ = 'cards'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    date = db.Column(db.String)
    status = db.Column(db.String)
    priority = db.Column(db.String)


@app.cli.command('create')
def create_db():
    db.create_all()
    print("Table created")

@app.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Tables dropped")

@app.cli.command('seed')
def seed_db():
    card = Card(
        title = 'Start the project',
        description = 'Stage 1 - Creating the database',
        status = 'To do',
        priority = 'High',
        date = date.today()
    )

    db.session.add(card)
    db.session.commit()
    print('Table seed')

@app.route('/')
def index():
    return "Hello World!"
