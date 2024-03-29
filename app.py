import psycopg2
from flask import Flask, render_template, request

app = Flask(__name__)
connect = psycopg2.connect("dbname=tutorial user=postgres password=0000")
cur = connect.cursor()  # create cursor


@app.route('/')
def main():
    return render_template("main.html")


@app.route('/return', methods=['post'])
def re_turn():
    return render_template("main.html")


@app.route('/print_table', methods=['post'])
def print_table():
    cur.execute("SELECT * FROM users;")
    result = cur.fetchall()

    return render_template("print_table.html", users=result)


@app.route('/register', methods=['post'])
def register():
    id = request.form["id"]
    password = request.form["password"]
    send = request.form["send"]

    if send=='login':


        cur.execute("SELECT password FROM users WHERE id=\'{}\';".format(id))
        result =cur.fetchall()

        if result[0][0] ==password:
            return render_template("login_success.html")
        else:
            return render_template("login_fail.html")
    else:
        cur.execute("SELECT COUNT(id) FROM users WHERE id=\'{}\';".format(id))
        result = int(cur.fetchall()[0][0])
        if result==1:
            return render_template("ID_collision.html")
        else:
            cur.execute("INSERT into users values(\'{}\',\'{}\');".format(id,password))
            return render_template("login_success.html")

if __name__ == '__main__':
    app.run()
