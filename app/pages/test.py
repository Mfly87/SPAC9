from flask import render_template, request
from app import app

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
    return render_template("index.html")