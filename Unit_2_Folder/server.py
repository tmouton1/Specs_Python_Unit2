from flask import Flask, render_template, url_for, redirect
from cupcakes import get_cupcakes, find_cupcake, add_cupcake_dictionary

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", cupcakes=get_cupcakes("cupcakes.csv"))
    
app.route('/info')  # = 127.0.0.1:8000/information
def info():
    return render_template("info.html")

@app.route("/cupcakes")
def get_cupcakes():
    return render_template("cupcakes.html")


@app.route("/order")
def order():
    return render_template("order.html")


@app.route("/individual-cupcake/<name>")
def individual_cupcake(name):
    cupcake = find_cupcake("cupcakes.csv", name)
    if cupcake:
        return render_template("individual-cupcake.html",name)
    else: 
        return "Cupcake not found. Please feel free to select another!"


@app.route("/add-cupcake/<name>")
def add_cupcake(name):
    cupcake = find_cupcake("cupcakes.csv", name)

    if cupcake:
        add_cupcake_dictionary("orders.csv",cupcake)
        return redirect(url_for("home"))
    else:
        return "Sorry cupcake not found."

    # ===============================
    
        if __name__ == "__main__":

            print("yes")
        app.env = "development"
        app.run(debug = True, port = 8000, host = "localhost")


