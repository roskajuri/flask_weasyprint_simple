from flask import Flask, render_template, url_for
from flask_weasyprint import HTML, render_pdf

app = Flask(__name__)


#perus route
@app.route('/hello/<name>/')
def hello_html(name):
    return render_template('hello.html', name=name)

#perus route pdf
@app.route('/hello_<name>.pdf')
def hello_pdf(name):
    print("start")
    return render_pdf(url_for('hello_html', name=name))
    print("stop")

#ulkopuolinen pdf

@app.route('/moi.pdf')
def moi():

    print("start")
    return render_pdf('http://www.google.fi')
    print("stop")

if __name__ == '__main__':
    app.run(debug=True)