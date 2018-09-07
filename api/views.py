from flask import Flask, request, jsonify
from views import *

app = Flask(__name__)

@app.route('/game')
def newgame():
    board = request.args.get('board')
    return board
    
