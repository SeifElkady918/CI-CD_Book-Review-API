from flask import Flask, jsonify, request

app = Flask(__name__)
books = [
    {"id": 1, "title": "Example Book", "author": "John Doe", "review": "An amazing read!"}
]

@app.route("/reviews", methods=["GET"])
def get_reviews():
    return jsonify(books)

@app.route("/reviews", methods=["POST"])
def add_review():
    data = request.get_json()
    new_id = max(book["id"] for book in books) + 1 if books else 1
    new_book = {
        "id": new_id,
        "title": data.get("title"),
        "author": data.get("author"),
        "review": data.get("review")
    }
    books.append(new_book)
    return jsonify(new_book), 201

if __name__ == "__main__":
    app.run(debug=True)
