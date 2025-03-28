from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
import datetime

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)
# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)
x = datetime.datetime.now()

# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()

class NewPost(FlaskForm):
    block_post = StringField("Blog Post Title",validators=[DataRequired()])
    subtitle = StringField("Subtitle",validators=[DataRequired()])
    name = StringField("Your Name",validators=[DataRequired()])
    blog_img_url = StringField("Blog Img URL",validators=[URL()])
    blog_content = CKEditorField("Content",validators=[DataRequired()])
    submit = SubmitField("Submit Post")






@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    get_list =  db.session.execute(db.select(BlogPost))
    posts = get_list.scalars().all()
    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/post_page/<int:post_id>')
def show_post(post_id):

    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.get_or_404(BlogPost,post_id)
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route("/add_post",methods=["POST","GET"])
def add_new_post():
    form = NewPost()
    if form.validate_on_submit():
        new_post = BlogPost(
            title = form.block_post.data,
            subtitle = form.subtitle.data,
            date = x.today().strftime("%B %d, %Y"),
            body = form.blog_content.data,
            author = form.name.data,
            img_url = form.blog_img_url.data,
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))

    return render_template("make-post.html",form=form)

# TODO: edit_post() to change an existing blog post
@app.route("/edit-post/<int:post_id>",methods = ["POST","GET"])
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = NewPost(
        block_post=post.title,
        subtitle=post.subtitle,
        blog_img_url=post.img_url,
        name=post.author,
        blog_content=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.block_post.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.blog_img_url.data
        post.author = edit_form.name.data
        post.body = edit_form.blog_content.data
        db.session.commit()
        return redirect(url_for('show_post',post_id = post.id))


    return render_template("make-post.html", post = True, form = edit_form)

# TODO: delete_post() to remove a blog post from the database
@app.route("/delete/<int:post_code>")
def delete_post(post_code):
    post = db.get_or_404(BlogPost, post_code)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('get_all_posts'))




# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
