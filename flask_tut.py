from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


# to render home route
@app.route("/")
def home():
    # can return inline html content
    return "Hello ! welcome to homepage <h1> HELLO</h1>"


# to render dynamic route
@app.route("/<name>")
def user1(name):
    return f"Hello {name}!"


# to render template
@app.route("/home1")
def home1():
    return render_template("index.html")


@app.route("/login/<usr>")
def user2(usr):
    return f"<h1>Hello {usr} , you are logged in</h1>"


# to render dynamic route with template
@app.route("/name/<name>")
def dyna_tem(name):
    return render_template("dynamic.html", content=name)


# to render form with get post methods
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user2 = request.form["nm"]
        return redirect(url_for("user2", usr=user2))
    else:
        return render_template("login.html")


# to render html template with python logic written inside it
@app.route("/python")
def html_py():
    return render_template("python.html", content=["a", "b", "c"])


# for redirection
# /admin1 only allows /admin1 but not /admin1/
@app.route("/admin1")
def redir1():
    # to redirect to other page when tried to access a unauthorised route
    # need to give function name inside url_for
    return redirect(url_for("home"))


# /admin2/ only allows /admin2 and /admin2/
@app.route("/admin2/")
def redir2():
    # to redirect to other page when tried to access a unauthorised route
    # need to give function name inside url_for
    return redirect(url_for("user", name="vishal"))


if __name__ == "__main__":
    app.run()
