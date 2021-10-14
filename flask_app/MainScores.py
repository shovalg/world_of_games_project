from flask import render_template
from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE
from flask import Flask

app = Flask(__name__)


@app.route('/')
def score_server():
    with open(SCORES_FILE_NAME, 'r', encoding='utf-8') as scores_file:
        score = scores_file.read()
    return render_template("public/index.html", SCORE=score)


@app.errorhandler(BAD_RETURN_CODE)
def internal_error(error_msg):
    return render_template("error_handling/500.html", ERROR=error_msg)
