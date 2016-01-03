# all the imports
import sqlite3
from flask import Flask, request, g, redirect, url_for, \
    abort, render_template, flash
from tinydb import TinyDB, Query

db = TinyDB('db.json')

# configuration
DEBUG = True

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

if __name__ == '__main__':
    app.run()
