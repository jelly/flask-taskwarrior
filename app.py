#!/usr/bin/python

from flask import Flask, render_template
from flask_talisman import Talisman

from tasklib import TaskWarrior, Task


csp = {
    'default-src': '\'self\'',
    'style-src': '\'self\'',
    'font-src': '\'self\'',
    'form-action': '\'self\''
}

def create_app(debug=False):
    talisman = Talisman()
    app = Flask(__name__)
    # TODO: config
    app.debug = debug

    talisman.init_app(app,
                      force_https=False,
                      session_cookie_secure=False,
                      content_security_policy=csp,
                      referrer_policy='no-referrer')

    return app

def create_taskwarrior():
    # TODO: config of flask
    TW = '/home/jelle/.task'
    return TaskWarrior(TW)


app = create_app(True)
tw = create_taskwarrior()  # TODO: bind to Flask app? Module?


@app.route("/")
def index():
    return render_template('index.html', tasks=tw.tasks)

def main():
    app.run()


if __name__ == "__main__":
    main()
