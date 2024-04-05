from flask import render_template, request, jsonify
from app import app

from database import MySQLHandler
from dataClasses.products import CerealObj, ProductFactory

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/results")
def Results():
    return jsonify("_build_dict_list")

@app.route("/<test>")
def ID(test):
    if request.method == "GET":

        _search_id = ""
        try:
            _search_id = test#request.form.get("fname", "")
        except:
            print("nada")
        _search_query = "id='%s'" % (_search_id) if _search_id else ""

        print(_search_query)
        _sql_handler:MySQLHandler = MySQLHandler()
        _build_dict_list = _sql_handler.search(CerealObj, search_term = _search_query)

        return jsonify(_build_dict_list)
    #return render_template("index.html")
    #return render_template("index.html")