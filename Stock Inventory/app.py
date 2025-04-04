from flask import Flask, render_template

app = Flask(__name__)

# Sample inventory list with items
inventory = [
    {"serial_number": 1, "type": "Nightwear", "price": 500, "stock": 50, "code": "NW-001"},
    {"serial_number": 2, "type": "Sarees", "price": 1500, "stock": 30, "code": "SR-002"},
    {"serial_number": 3, "type": "Salwar", "price": 1000, "stock": 20, "code": "SW-003"}
]

@app.route("/")
def index():
    return render_template("home.html", inventory=inventory)

if __name__ == "__main__":
    # Set host to 0.0.0.0 and port to 8080 for deployment platforms like Render or PythonAnywhere.
    app.run(host="0.0.0.0", port=8080, debug=True)
