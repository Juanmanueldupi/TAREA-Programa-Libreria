from flask import Flask, render_template, abort
import os
import json

app = Flask (__name__)

with open("books.json") as fichero:
    datos=json.load(fichero)

@app.route('/',methods=["GET","POST"])
def inicio():
    return render_template("inicio.html",libros=datos)

@app.route('/libro/<isbn>',methods=["GET","POST"])
def libro(isbn):
    for book in datos:
        if "isbn" in book.keys() and isbn == book["isbn"]:
            return render_template("biblioteca.html", libro=book)
    abort(404)


app.run('0.0.0.0' ,debug=False)
