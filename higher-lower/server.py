from flask import Flask
import random
random_number = random.randint(0,9)
print(random_number)

app = Flask(__name__)
@app.route("/")
def hello_world():
    return ('<h1>Guess a number between 0 and 9 </h1>'
            '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExcHB1eXo3dWM4NHZ1NnRmeGVmb21rMDNqcnRpMWxuYzd5bGN2dThyMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/glJdAXojfP3wPEg84a/giphy.webp" width=500>')
@app.route("/<int:guess>")
def guess_number (guess):
       if guess > random_number:
           return ("<h1 style='color: black'>Too high,try again</h1>"
                "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcGFvdmhpdG52azA2cWJqNGR4eXM1OTNzZ2NpdDE5eWxuMXVlamlqayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TiOtVRx07iGqLmWk6m/giphy.webp'>")
       elif guess < random_number:
           return ("<h1 style='color:blue'>Too low,try again</h1>"
                "<img src='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMHQ3ajRjejVyOTVyeDR4cnY1Mjc0YTVkNW1hYjZqcGc3MzJidW1pdiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/nNOvniJd8KjNC/giphy.webp'>")
       else:
           return ("<h1 style='color:green'>You found right number </h1>"
                   "<img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcmViaW90aXNpbGp5bG1jMGthdnJmZ2NrbWU0Znl6c2xscWpqdXdzMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/5quxvnjc77jutz5KGR/giphy.webp'>")




if __name__ == "__main__":
    app.run(debug=True)
