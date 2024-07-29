from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


def read_csv(file_path):
    products = []
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append(
                {
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"]),
                }
            )
    return products


def read_sql(database_path):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()
    conn.close()
    products = []
    for row in rows:
        products.append(
            {"id": row[0], "name": row[1], "category": row[2], "price": row[3]}
        )
    return products


@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id", type=int)

    if source not in ["json", "csv", "sql"]:
        return render_template("product_display.html", error="Wrong source")

    if source == "json":
        data = read_json("products.json")
    elif source == "csv":
        data = read_csv("products.csv")
    elif source == "sql":
        data = read_sql("products.db")

    if product_id:
        product = next((p for p in data if p["id"] == product_id), None)
        if not product:
            return render_template(
                "product_display.html", error="Product not found"
            )
        data = [product]

    return render_template("product_display.html", products=data)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
