from flask import render_template, request, jsonify
from app import app

from database import MySQLHandler
from dataClasses.products import CerealObj, ProductFactory
'''
@app.route("/a", methods = ["GET","POST"])
def AP():
    if request.method == "GET":


        print(request.data)

        for _key in request.form:
            print("%s: %s" % (_key, request.form[_key]))

        _search_id = request.form.get("fname", "")
        _search_query = "id='%s'" % (_search_id) if _search_id else ""

        print(_search_query)
        _sql_handler:MySQLHandler = MySQLHandler()
        _build_dict_list = _sql_handler.search(CerealObj, search_term = _search_query)

        return jsonify(_build_dict_list)
    return render_template("index.html")
'''