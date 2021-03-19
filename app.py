from logging import error
from flask import Flask, render_template, url_for, request, session, flash
from werkzeug.utils import redirect
from util import json_response
import data_manager as d
import data_handler
import datetime
import persistence as p

app = Flask(__name__)
app.secret_key = "valami" 



@app.route("/new-card/", methods=["GET","POST"])
def createnewcard():
    list_questions = p.show_cards()
    ids = []
    for add_questions in list_questions:
        ids.append(add_questions["id"])
    new_questions = {}
    if request.method == "POST":
        if len(ids) == 0:
            new_questions["id"] = "0"
        else:
            new_questions["id"] = str(int(max(ids)) + 1)
        new_questions['board_id'] = 1
        new_questions["title"] = "newlycreatedcard"
        new_questions["status_id"] = 0
        new_questions["order"] = 0
        list_questions.append(new_questions)
        p.write_to_file(list_questions)
        return redirect("/")
    return render_template("index.html")





@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session.pop("email", None)
        session.pop("password",None)
        paswd = request.form["password"]
        email_address = request.form["email"]
        user = d.get_user_by_email_and_pass(email_address, paswd)
        password = ''
        for _ in user:
            password = _["password"]
        if user and request.form['password'] and password:
            for _ in user:
                session['password'] = _['password']
                session["email"] = _["email"]
            return redirect("/")
        else:
            flash("Login failed: Wrong password or email","red")
            return redirect("/")
    return render_template("login.html") 



@app.route("/register", methods=["POST", "GET"])
def register_new_account():
    session.pop("email",None)
    if request.method == "POST": 
        password = request.form["password"]
        email = request.form["email"]
        created_on = datetime.datetime.now().strftime("%d-%B-%Y %H:%M:%S")
        d.register_new_user(password, email, created_on)
        return redirect("/")
    return render_template("register.html", session=session)



@app.route('/logout', methods=["GET","POST"])
def logout():
    session.pop('email',None)
    session.pop("password", None)
    flash("You have been successfully logged out!","green")
    return redirect("/")


@app.route("/", methods=["GET","POST"])
def index():
    """
    This is a one-pager which shows all the boards and cards
    """
    return render_template("index.html", session=session)


@app.route("/get-boards")
@json_response
def get_boards():
    """
    All the boards
    """
    return data_handler.get_boards()

@app.route("/get-cards")
@json_response
def get_cards():
    """
    All the boards
    """
    return data_handler.get_all_cards()


@app.route("/get-cards/<int:board_id>")
@json_response
def get_cards_for_board(board_id: int):
    """
    All cards that belongs to a board
    :param board_id: id of the parent board
    """
    return data_handler.get_cards_for_board(board_id)


@app.route("/get-statuses")
@json_response
def get_statuses():
    """
    All cards that belongs to a board
    :param board_id: id of the parent board
    """
    return data_handler.get_statuses()


def main():
    app.run(debug=True)

    # Serving the favicon
    with app.app_context():
        app.add_url_rule(
            '/favicon.ico', redirect_to=url_for('static', filename='favicon/favicon.ico'))


if __name__ == '__main__':
    main()
