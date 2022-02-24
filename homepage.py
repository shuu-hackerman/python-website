from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from sqlalchemy import true
app = Flask(__name__)
app.secret_key = "elemesmo"
app.permanent_session_lifetime = timedelta(days=5)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/test")
def test():
    return render_template("new.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        flash(f"Login Succesful!, Voce entrou com sucesso")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash(f"Already Logged In, Ja esta logado!")
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
    else:
        flash(f"You are not logged in, Voce nao esta logado")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash(f"You have been logged out! Voce foi desconectado, {user}", "info")
    session.pop("user", None)    
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug =True)