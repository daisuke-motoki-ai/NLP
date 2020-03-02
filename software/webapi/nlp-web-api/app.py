# -*- coding: utf-8 -*-
# https://qiita.com/ynakayama/items/2cc0b1d3cf1a2da612e4

from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import MeCab

app = Flask(__name__)

# Main
def picked_up():
    messages = [
        "こんにちは形態素解析したいフレーズを教えてください",
        "形態素解析？",
        "形態素解析するよ"
    ]
    return np.random.choice(messages)

def tokenize(text):
    tagger = MeCab.Tagger()
    node = tagger.parseToNode(text)
    tokens = []
    while node:
        if node.surface != '':
            tokens.append(node.surface)
        node = node.next
    return tokens

# Routing
@app.route('/')
def index():
    title = "ようこそ"
    message = picked_up()
    return render_template('index.html',
                           message=message, title=title)

@app.route('/post', methods=['POST', 'GET'])
def post():
    title = "こんにちは"
    if request.method == 'POST':
        name = request.form['name']
        tagger = MeCab.Tagger()
        words = tagger.parse(name)
        words = tokenize(name)
        return render_template('index.html',
                               name=words, title=title)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
