from flask import render_template, request
from app import app

from database import MySQLHandler

@app.route("/action_page", methods = ["POST"])
def AP():
    if request.method == "POST":
        try:
            _data: dict[str,str] = request.form

            for _d in _data:
                print("%s: %s" % (_d, _data[_d]))
            print("DONE")
        except:
            print("UNDONE")

        a:MySQLHandler = MySQLHandler()
        print(a)
    return render_template("index.html")