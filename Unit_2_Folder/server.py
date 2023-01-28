from flask import Flask, render_template, url_for, redirect
from cupcakes import get_cupcakes, find_cupcake, add_cupcake_dictionary


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", cupcakes = get_cupcakes("cupcakes.csv"))    

@app.route("/cupcakes")
def see_cupcakes():
    return render_template("cupcakes.html", cupcakes=get_cupcakes("cupcakes.csv"))

@app.route("/add-cupcake/<name>")
def add_cupcake(name):
    cupcake = find_cupcake("cupcakes.csv", name)

    if cupcake:
        add_cupcake_dictionary("orders.csv", cupcake)
        return redirect(url_for("home"))
    else:
        return "Sorry cupcake not found."

@app.route("/order")
def get_order():
    
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
    cakes = ['Strawberry Shortcake', 'Choco Freeze', 'Peanut Butter Swirl', 'Strawbery Shortcake']
    return render_template("individual.html", cakes=cakes)

    


    # ===============================
    
if __name__ == "__main__":

    print("yes")
    app.env = "development"
    app.run(debug = True, port = 8000, host = "localhost")


