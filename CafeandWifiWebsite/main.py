from flask import Flask, render_template, request
from flask_sqlalchemy import  SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer,String,Boolean

app = Flask(__name__)

class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Cafe(db.Model):
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


@app.route("/")
def main_page ():
    return render_template("main.html")

@app.route("/cities")
def all_cities():
    return render_template("cities.html")
@app.route("/suggest")
def suggest_cities():
    return render_template("suggest.html")
@app.route("/login")
def login_in():
    return render_template("login.html")
@app.route("/register")
def register_acc():
    return render_template("register.html")
@app.route("/city")
def city():
    cafes = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes =cafes.scalars().all()
    return render_template("city.html", cafes = all_cafes)
@app.route("/city/<int:cafe_id>")
def cafe_name (cafe_id):
    requested_cafe = db.get_or_404(Cafe,cafe_id)
    return  render_template("cafe.html",cafe_id = requested_cafe)

@app.route("/add",methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
        name = request.form.get("name"),
        map_url = request.form.get("map_url"),
        img_url = request.form.get("img_url"),
        location = request.form.get("location"),
        seats = request.form.get("seats"),
        has_toilet = request.form.get("has_toilet"),
        has_wifi = request.form.get("has_wifi"),
        has_socekts = request.form.get("has_sockets"),
        can_take_calls = request.form.get("can_take_calls"),
        coffee_price = request.form.get("coffee_price")
    )
    db.session.add(new_cafe)
    db.session.commit()
@app.route("/add", methods=["GET"])
def delete():
    get = request.args.get(id)
    db.session.delete(Cafe,id)
    db.session.commit()








if __name__ == "__main__":
    app.run(debug=True)