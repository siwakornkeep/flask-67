from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/home")
def home():
    # return "<h1>home</h1>"
    name = "lisa"
    age = 27
    my_dict = {"name": "Lisa", "age": 27}
    return render_template("home.html", name=name, age=age, my_dict=my_dict)

@app.route("/create", methods=["GET"] )
def create():
    return render_template("create.html")

@app.route("/store", methods=["POST"])
def store():
    if request.method == "POST":
        flower_name = request.form['flower_name']
        lat_num = request.form['lat_num']
        long_num = request.form['long_num']
        place = request.form['place']
        detail = request.form['detail']
        print(flower_name, lat_num, long_num, place, detail)
    return redirect('/home')

if __name__ == "__main__":
    app.run(debug=True)
    #app.run()
    