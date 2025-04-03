from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample inventory data
inventory = [
    {"serial_number": 1, "type": "Nightwear", "price": 500, "stock": 50, "code": "NW-001"},
    {"serial_number": 2, "type": "Sarees", "price": 1500, "stock": 30, "code": "SR-002"},
    {"serial_number": 3, "type": "Salwar", "price": 1000, "stock": 20, "code": "SW-003"}
]

@app.route("/")
def index():
    return render_template("home.html", inventory=inventory)

@app.route("/add", methods=["POST"])
def add_item():
    new_item = {
        "serial_number": len(inventory) + 1,  # Auto-incrementing Serial Number
        "type": request.form["type"],
        "price": int(request.form["price"]),
        "stock": int(request.form["stock"]),
        "code": request.form["code"]
    }
    inventory.append(new_item)
    return redirect(url_for("index"))

@app.route("/edit/<int:serial_number>", methods=["GET", "POST"])
def edit_item(serial_number):
    item = next((i for i in inventory if i["serial_number"] == serial_number), None)
    if not item:
        return "Item not found", 404

    if request.method == "POST":
        item["type"] = request.form["type"]
        item["price"] = int(request.form["price"])
        item["stock"] = int(request.form["stock"])
        return redirect(url_for("index"))

    return render_template("edit.html", item=item)

if __name__ == "__main__":
    app.run(debug=True)
