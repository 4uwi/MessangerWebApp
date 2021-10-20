import string

from flask import Flask, render_template
import mysql.connector as database
from werkzeug.exceptions import abort
import numpy as np
import pandas as pd

app = Flask(__name__)


# REMEMBER: 1 result is tuple, many results is list
def create_message_dict(*args):
    tags = ("id_message", "id_sender", "id_receiver", "datetime", "text")
    messages = []
    for items in args:
        if items is None:
            pass
        else:
            for item in items:
                messages.append(pd.Series(item, tags))
    return messages



# class Message:
#     data = ()
#
#     def __init__(self, *args):
#         tags = ("ID message:", "ID sender:", "ID receiver:", "Date&Time:", "Message:")
#         self.data = pd.Series(args, tags)
#         return self
#
#     def __iter__(self):
#         for item in self.data:
#             yield item


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


@app.route('/')
def index():
    con = get_db_connection()
    cur = con.cursor()

    cur.execute("SELECT * FROM message")
    res = cur.fetchall()
    message = create_message_dict(res)
    return render_template('index.html', message=message)


@app.route('/<int:contact_id>')
def dialog(contact_id):
    res = get_messages_by_contact(contact_id)
    message = create_message_dict(res)
    return render_template('dialog.html', message=message)
