

from flask import Flask,render_template
import requests
import regex
API_KEY_FOR_GENDERIZE = "051337bf26dc55dfc120de3190a80b4d"
ENDPOINT_GENDERIZE = "https://api.genderize.io"
ENDPOINT_AGE = "https://api.agify.io"


app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("main.html")
@app.route("/guess/<name>")
def guess_age_gender(name):
    params = {
        "name": name,
    }
    response_gender = requests.get(url=ENDPOINT_GENDERIZE, params=params)
    get_gender = regex.search('"gender":"(.+?)","probability"',response_gender.text).group(1)
    response_age = requests.get(url=ENDPOINT_AGE,params=params)
    get_age = regex.search(',"age":(.+?)}',response_age.text).group(1)
    return render_template("index.html",get=name,gender=get_gender,age=get_age)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", post=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
