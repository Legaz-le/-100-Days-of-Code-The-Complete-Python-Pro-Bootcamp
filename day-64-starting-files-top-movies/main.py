from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

class Base(DeclarativeBase):
  pass

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
db = SQLAlchemy(model_class=Base)
Bootstrap5(app)

# CREATE DB
db.init_app(app)
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[str] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[str] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()

class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")

class AddMovieForm(FlaskForm):
    add = StringField("Title Movie",validators=[DataRequired()])
    submit = SubmitField("Add Movie")

@app.route("/edit", methods = ["POST","GET"])
def edit ():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie,movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

API_TOKEN ="xxxxxx"
ENDPOINT = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"
API_KEY ="xxxxx"
header = {
    "accept": "application/json",
    "Authorization":f'Bearer{API_TOKEN}',
}

@app.route("/add",methods=["POST","GET"])
def add ():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie_title = form.add.data
        response = requests.get(url=ENDPOINT, params={"api_key":API_KEY,"query": movie_title})
        data = response.json()['results']
        return render_template("select.html", options =data)

    return render_template("add.html", form=form)

@app.route("/find",methods=["POST","GET"])
def find_movie():
    form = RateMovieForm()
    movie_api_id =request.args.get("id")
    if movie_api_id:
        movie_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        response = requests.get(movie_url,params={"api_key":API_KEY})
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('edit' ,id=new_movie.id))








@app.route("/")
def home():
    movies = db.session.execute(db.select(Movie).order_by(Movie.ranking))
    all_movie = movies.scalars().all()
    for i in range(len(all_movie)):
        all_movie[i].ranking = len(all_movie) - i
    db.session.commit()
    return render_template("index.html", all_movie=all_movie)








if __name__ == '__main__':
    app.run(debug=True)
