from flask import render_template, request, jsonify
import json
from app import app

from database import MySQLHandler
from dataClasses.products import CerealObj, ProductFactory

def search_database(search_query:str) -> list[dict[str,any]]:
    _sql_handler:MySQLHandler = MySQLHandler()
    _build_dict_list = _sql_handler.search(CerealObj, search_term = search_query)

    return jsonify(_build_dict_list)

def get_search_type(search_key:str) -> str:
    _split_key = search_key.split("_")
    if len(_split_key) == 2:
        if _split_key[0].lower() == "min":
            return "%s>=" % (_split_key[1])
        elif _split_key[0].lower() == "max":
            return "%s<=" % (_split_key[1])
    return "%s=" % (search_key)

def value_is_number(value:str) -> bool:
    try:
        value = float(value)
        return True
    except:
        return False

def id_already_exists_in_database(id: str) -> bool:
    if not id:
        return False    
    _search_query = "id='%s'" % (id)
    _search_list = search_database(_search_query)
    return len(_search_list) != 0

@app.route("/results")
def Search():

    _search_terms = []

    for _key in request.args:
        _search_type = get_search_type(_key)
        _value = request.args[_key]
        _value_str = str(_value) if value_is_number(_value) else "'%s'" % (_value)
        _search_term = "%s%s" % (_search_type, _value_str)
        _search_terms.append(_search_term)

    _query = " AND ".join(_search_terms)
    return search_database(_query)

@app.route("/")
def Home():
    if request.method == "GET":

        _search_query = ""
        try:
            _dict:dict = json.loads(request.data)
            _search_id = _dict.get("id", "")
            _search_query = "id='%s'" % (_search_id) if _search_id else ""
        except:
            pass
        
        return search_database(_search_query)
    '''
    elif request.method == "POST":
        try:
            _dict:dict = json.loads(request.data)
        except:
            return
        
        _id = _dict.get("id", "")
        if id_already_exists_in_database(_id):
            print(MySQLHandler.search("id='%s'" % (_id)))
    '''