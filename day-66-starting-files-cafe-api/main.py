from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(
            self):  # This is a dictionary comprehension function created inside the Cafe class definition. It will be used to turn rows into a dictionary before sending it to jsonify.
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}



with app.app_context():
    db.create_all()




@app.route("/")
def home():

    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/all")
def get_all_cafes ():
    cafes = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = cafes.scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


@app.route("/search")
def search_get_location ():
    query_location = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location == query_location))
    # Note, this may get more than one cafe per location
    all_cafes = result.scalars().all()
    if all_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_new_cafe():
    new_cafe = Cafe(
        name = request.form.get("name"),
        map_url = request.form.get("map_url"),
        img_url = request.form.get("img_url"),
        location = request.form.get("location"),
        seats = request.form.get("seats"),
        has_toilet = bool(request.form.get("has_toilet")),
        has_wifi = bool(request.form.get("has_wifi")),
        has_sockets = bool(request.form.get("has_sockets")),
        can_take_calls = bool(request.form.get("can_take_calls")),
        coffee_price = request.form.get("coffee_price")
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record
@app.route("/update_price/<int:cafe_id>",methods=["PATCH"])
def update_price_coffee(cafe_id):
    price = request.args.get("new_price")
    cafe = db.get_or_404(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price = price
        db.session.commit()
        return jsonify(success={"success":"Successfully update the price"}),200
    else:
        return jsonify(error={"Not found":"Sorry a id with that caffe didn't found in the database"}),400




# HTTP DELETE - Delete Record
@app.route("/report_closed/<int:cafe_id>",methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        cafe = db.get_or_404(Cafe, cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403


if __name__ == '__main__':
    app.run(debug=True)
