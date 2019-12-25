from flask import Flask, render_template
import logging
import os
import pandas as pd
import numpy as np

app = Flask(__name__)
app.logger.setLevel(logging.INFO)
DATABASE_URL = "database/Question.csv"
db = pd.read_csv(DATABASE_URL, encoding="utf-8")
questions = db.jp
np.random.seed(0)

@app.route("/", methods=["GET"])
def index():
    choice = np.random.randint(0, questions.size)
    qustion = questions[choice]
    return render_template("suggest.html",
            question=qustion)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
