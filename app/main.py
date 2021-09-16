import uncurl
from flask import Flask, render_template, request

app = Flask(__name__)

curl_error = """usage: curl [-h] [-d DATA] [-b DATA_BINARY] [-X X] [-H HEADER]
               [--compressed] [-k] [--user USER] [-i] [-s]
               command url"""

def convert_curl(curl):
    try:
        req = uncurl.parse_context(curl)
        return req
    except:
        return None

@app.route("/", methods=['GET', 'POST'])
def convert_page():
    if request.method == 'POST':
        curl = request.form['curl']
        req = convert_curl(curl)
        if req != None:
            return render_template("home.html", method=req.method, body=req.data, headers=req.headers, url=req.url)
        else:
            return render_template("home.html", error=curl_error)
    return render_template("home.html")