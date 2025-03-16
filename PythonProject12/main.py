from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, mapped_column,Mapped
from sqlalchemy import Integer, String


class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database_post.db"
# initialize the app with the extension
db.init_app(app)

class Post(db.Model):
    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False)
    description: Mapped[str] = mapped_column(String(250),nullable=False)
    post: Mapped[str] = mapped_column(String(250),unique=True)
    Url_header: Mapped[str] = mapped_column(String(250),nullable=False)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    posts = db.session.execute(db.select(Post))
    get = posts.scalars().all()
    return render_template("index.html", content = get)

@app.route("/post/<int:post_id>")
def post(post_id):
    requested_post = db.get_or_404(Post,post_id)
    return render_template("post.html",  post = requested_post)
@app.route("/add", methods=['GET'])
def add_post():
    new_post = Post()
    db.session.add(new_post)
    db.session.commit()
@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/register")
def register():
    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)