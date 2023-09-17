from flask import Flask, render_template, request
import js2py
import random

app = Flask(__name__)
@app.route("/")
@app.route("/home")
def home():
    return render_template("ilovehtml.html")
@app.route("/result", methods = ['POST', 'GET'])
def result():
    output = request.form.to_dict()
    password = ''
    numbercheck = request.form.getlist('numberscheck')
    symbolcheck = request.form.getlist('symbolscheck')
    if len(numbercheck) == 0:
        symbolsOnly = "!@#$%^&*()_+}{ABCDEFGHIJKLMNOPRQSTUVWXYZ"
        for x in range(0, 10):
            password_char = random.choice(symbolsOnly)
            password = password + password_char
    elif len(symbolcheck) == 0:
        digitsOnly = "1234567890ABCDEFGHIJKLMNOPRQSTUVWXYZ"
        for x in range(0, 10):
            password_char = random.choice(digitsOnly)
            password = password + password_char
    elif len(symbolcheck) == 1 and len(numbercheck) == 1:
        digitsAndSymbols = "ABCDEFGHIJKLMNOPRQSTUVWXYZ1234567890abcdefghijklmnoprqstuvwxyz!@#$%^&*()_+}{"
        for x in range(0, 10):
            password_char = random.choice(digitsAndSymbols)
            password = password + password_char

    return render_template("ilovehtml.html", password = password)
if __name__ == '__main__':
    app.run(debug = True)

