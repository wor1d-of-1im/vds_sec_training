# app.py

from flask import Flask, request, render_template
from auth import login_check

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    error = ""

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        result = login_check(username, password)

        if result == "SUCCESS":
            # RESPONSE KHÁC BIỆT RÕ RÀNG
            return f"""
            <h1>Welcome {username}</h1>
            <p>Login successful!</p>
            """
        else:
            error = result

    return render_template("login.html", error=error)

if __name__ == "__main__":
    app.run(debug=True)