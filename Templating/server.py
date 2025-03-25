from flask import Flask, render_template
import requests

app = Flask(__name__)
response_post  = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_objects = []
for post in response_post:
    post_obj = (post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

@app.route("/")
def main ():
    return render_template("index.html", post =response_post)
@app.route("/post/<int:blog_id>")
def get_post(blog_id):
    return render_template("post.html", post = response_post, id = blog_id)





if __name__ == "__main__":
    app.run(debug=True)
