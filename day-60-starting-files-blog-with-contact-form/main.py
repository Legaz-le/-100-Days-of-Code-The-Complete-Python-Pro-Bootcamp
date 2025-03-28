

from flask import Flask, render_template,request
import requests
import smtplib

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

EMAIL = "xxxxxxx"
password = "xxxxxxx"
app = Flask(__name__)




@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method == 'POST':
        return receive_data()
    else:
        return render_template("contact.html")



def receive_data():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    message = request.form["message"]
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=password)
        connection.sendmail(
            from_addr=EMAIL, to_addrs="worldhaha@mail.ru",
            msg=f"Subject:Message\n\nName:{name}\nEmail:{email}\nPhone:{phone}\nMessage:{message}")
    return render_template("contact.html",name="Successfully sent message")





@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
