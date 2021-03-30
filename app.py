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


# add new card 
@app.route("/new-card/", methods=["GET","POST"])
def createnewcard():
    list_cards = p.show_cards()
    ids = []
    for add_cards in list_cards:
        ids.append(add_cards["id"])

    new_cards = {}

    if request.method == "POST":
        if not session:
            boards_public = p.show_boards()
            board_ids_public = []
            for board in boards_public:
                if board['user_id'] == 'public':
                    board_ids_public.append(board['id'])
            new_cards['board_id'] = board_ids_public[-1]
            if not ids:
                new_cards["id"] = 0
            else:
                new_cards["id"] = str(int(ids[-1]) + 1)
        else:
            boards = p.show_boards()
            board_ids = []
            for board in boards:
                if board['user_id'] == str(session['user_id']):
                    board_ids.append(board['id'])
            new_cards['board_id'] = str(board_ids[-1])
            if not ids:
                new_cards["id"] = 0
            else:
                new_cards["id"] = str(int(ids[-1]) + 1)
        new_cards["title"] = "newlycreatedcard"
        new_cards["status_id"] = 0
        new_cards["order"] = 0
        list_cards.append(new_cards)
        p.write_to_file(list_cards)
        return redirect(url_for('index'))
    return render_template("index.html")

# add new board
@app.route("/new-board/", methods=["GET","POST"])
def createnewboard():
    list_boards = p.show_boards()
    ids = []
    for add_boards in list_boards:
        ids.append(add_boards["id"])

    new_boards = {}
    if request.method == "POST":
        if not session:
            if ids:
                new_boards["id"] = str(int(ids[-1]) + 1)
            else:
                new_boards["id"] = 0            
            new_boards["user_id"] = 'public'
        else:
            new_boards["user_id"] = session['user_id']
            if ids:
                new_boards["id"] = str(int(ids[-1]) + 1)
            else:
                new_boards["id"] = '0'
        new_boards['title'] = "Newly created board"
        list_boards.append(new_boards)
        p.write_to_boards(list_boards)
        return redirect(url_for('index'))
    return render_template("index.html")


# login system
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session.pop("email", None)
        session.pop("password",None)
        session.pop("user_id",None)
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
                session['user_id'] = _['user_id']
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
    session.pop('user_id',None)
    session.pop('created_on',None)
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
    all_board = data_handler.get_boards()
    if session:
        my_boards = []
        for board in all_board:
            if board['user_id'] == str(session['user_id']):
                my_boards.append(board)
        return my_boards
    else:
        public_boards = []
        for board in all_board:
            if board['user_id'] == 'public':
                public_boards.append(board)
        return public_boards

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
