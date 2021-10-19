from flask import Flask, render_template
import mysql.connector as database
from werkzeug.exceptions import abort

app = Flask(__name__)


def get_db_connection():
    con = database.connect(database='messenger', user='root', password='365841')
    return con


def get_message_by_id(id):
    con = get_db_connection()
    cur = con.cursor()
    cur.execute("SELECT text, datetime FROM message WHERE id = %s", (id,))
    res = cur.fetchone()
    return res


def get_messages_by_contact(contact_id):
    con = get_db_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM message WHERE id_receiver = %s", (contact_id,))
    res = cur.fetchall()
    if res is None:
        abort(404)  # TODO: come up with return if no messages
    return res


@app.route('/<int:contact_id>')
def index():
    messages = get_messages_by_contact("3")[0]
    tags = ("ID message: ", "ID sender: ", "ID receiver: ", "Date&Time: ", "Message: ")
    # for message, tag in zip(messages, tags): how to output many rows
    #     print(tag, message)
    return render_template('index.html', messages=messages, tags=tags, zip=zip)
