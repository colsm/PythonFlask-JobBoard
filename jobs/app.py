from flask import Flask, render_template

app = Flaskk(__name__)

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')
