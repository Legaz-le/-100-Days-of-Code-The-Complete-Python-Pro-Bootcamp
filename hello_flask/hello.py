from flask import Flask

app = Flask(__name__)

def make_bold(fun):
    def wrapper():
        return '<b>' + fun() + '</b>'
    return wrapper
def make_em(fun):
    def wrapper():
        return '<em>' + fun() + '</em>'
    return wrapper
def make_u(fun):
    def wrapper():
        return '<u>' + fun() + '</u>'
    return wrapper

@app.route("/")
def hello_world():
    return ('<h1 style="text-align: center">Hello, World!</h1>'
            '<p>This is a paragraph.<p>'
            '<img src="https://media.tenor.com/igcX5hdPWD4AAAAM/eating-cats.gif" width=200>')
#Different routes using the app.rout decorator
@app.route("/bye")
@make_bold
@make_em
@make_u
def bye():
    return "Bye"
#Creating variable paths and converting the path to a specified data type
@app.route("/<name>")
def greet(name):
    return f"Hello there {name} "

if __name__ == "__main__":
    #Run the app in debug mode to auto-reload
    app.run(debug=True)