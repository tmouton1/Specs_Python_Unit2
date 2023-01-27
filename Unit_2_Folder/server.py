from flask import Flask, render_template, url_for, redirect
from cupcakes import get_cupcakes, find_cupcake, add_cupcake_dictionary, cupcake1,cupcake2,cupcake3,cupcake4


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", cupcakes = get_cupcakes("cupcakes.csv"))    

@app.route("/cupcakes")
def see_cupcakes():
    return render_template("cupcakes.html", cupcakes=get_cupcakes("cupcakes.csv"))


@app.route("/order")
def get_order():
    place_order=get_cupcakes("orders.csv")
    return render_template("order.html")

@app.route("/info")
def about_info():
    return render_template("info.html")

# ===============================
# @app.route("/individual")
# def individual_cupcake():
#     cupcakes= "jose"
#     letters = list(cupcakes)

#     cupcake_dictionary = {'cupcake_name': 'strawberry'}
#     return render_template("individual.html", cupcakes=cupcakes, letters=letters, cupcake_dictionary=cupcake_dictionary)


@app.route("/individual")
def individual_cupcake():
    cupcake_list = ['Strawbery Shortcake', 'Red Velvet','Choco Freeze', 'Peanut Butter Swirl'

    ]
    return render_template("individual.html",cupcake_list=cupcake_list)

    


    # ===============================
    
if __name__ == "__main__":

    print("yes")
    app.env = "development"
    app.run(debug = True, port = 8000, host = "localhost")


