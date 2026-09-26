from flask import Flask, render_template, request, redirect

app = Flask(__name__)

blood_stock = {
    "A+": 10,
    "A-": 5,
    "B+": 8,
    "B-": 4,
    "O+": 12,
    "O-": 3,
    "AB+": 6,
    "AB-": 2
}

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        blood_group = request.form["blood_group"]
        units = int(request.form["units"])
        blood_stock[blood_group] += units
        return redirect("/")

    return render_template("index.html", blood_stock=blood_stock)


if __name__ == "__main__":
    app.run(debug=True)
