from flask import Flask, render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase,Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from datetime import  datetime




app= Flask(__name__)

class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///list-to-do.db'
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class ListForm(FlaskForm):
    get = StringField("Write you next task here",validators=[DataRequired()])

class List(db.Model):
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    list: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()

Bootstrap(app)

@app.route("/")
def index():
    today_date = datetime.today().strftime('%Y-%m-%d')
    form = ListForm()
    result = db.session.execute(db.select(List))
    all_cafes = result.scalars().all()
    return render_template("index.html",list =all_cafes, form =form,date = today_date)
@app.route("/",methods=["POST"])
def add_to_list():
    form = ListForm()
    if form.validate_on_submit():
        add = List(
            list=form.get.data
        )
        db.session.add(add)
        db.session.commit()
        return redirect(url_for("index"))
@app.route("/delete/<int:list_id>")
def delete(list_id):
    list_to_delete = db.get_or_404(List,list_id)
    db.session.delete(list_to_delete)
    db.session.commit()
    redirect(url_for("index"))
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)