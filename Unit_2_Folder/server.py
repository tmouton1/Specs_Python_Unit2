from flask import Flask, render_template, url_for, redirect
from cupcakes import get_cupcakes, find_cupcake, add_cupcake_dictionary, cupcake_list


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")
    
app.route('/info')
def get_info():
    return render_template("info.html")

@app.route("/cupcakes")
def see_cupcakes():
    return render_template("cupcakes.html", cupcakes=get_cupcakes("cupcakes.csv"))

CUPCAKES = get_cupcakes('cupcakes.csv')

@app.route("/order")
def get_order():
   return render_template("order.html")

@app.route("/cupcake-individual")
def individual_cupcake():
        return render_template("individual-cupake.html")





    # ===============================
    
if __name__ == "__main__":

    print("yes")
    app.env = "development"
    app.run(debug = True, port = 8000, host = "localhost")


