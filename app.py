import string

from flask import Flask, render_template
import mysql.connector as database
from werkzeug.exceptions import abort
import numpy as np
import pandas as pd

app = Flask(__name__)


def create_message_dict(*args, tags=True): #tags is boolean for switching between
                                            #list and dialog
    if tags:
        tags = ("id_receiver", "name", "datetime", "text")
    else:
        tags = ("id", "id_sender", "id_receiver", "datetime", "text")

    messages = []
    for items in args:
        if items is None:
            pass
        else:
            for item in items:
                messages.append(pd.Series(item, tags))
    return messages

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
    cur.execute("SELECT * "
                "FROM message "
                "WHERE id_receiver = %s", (contact_id,))
    res = cur.fetchall()
    if res is None:
        abort(404)  # TODO: come up with return if no messages
    return res


@app.route('/')
def index():

    con = get_db_connection()
    cur = con.cursor()

    # TODO connect loginig mechanism to change search id
    id = 1

    cur.execute("SELECT id_receiver, name, MAX(`datetime`), `text` "
                "FROM message JOIN `user` "
                "WHERE id_sender=%s "
                "GROUP BY id_receiver", (id,) )
    res = cur.fetchall()
    message = create_message_dict(res)
    return render_template('index.html', message=message)


@app.route('/<int:dialog_id>')
def dialog(dialog_id):
    res = get_messages_by_contact(dialog_id)
    message = create_message_dict(res, tags=False)
    return render_template('dialog.html', message=message)
