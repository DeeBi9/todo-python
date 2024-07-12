from flask import Flask, request, render_template
from datetime import datetime
TODOLIST = {}

app = Flask("todo")

@app.route("/add",methods=['GET','POST'])
def addtoList():
    if request.method == 'POST':
        task = request.form.get("TODO")
        date = request.form.get("date")
        TODOLIST[date] = task
        print(TODOLIST)
    return render_template("index.html")

@app.route("/clear",methods=['GET'])
def clearList():
    TODOLIST.clear()
    return "<h1>Cleared</h1>",str(TODOLIST)

@app.route("/getlist",methods=['GET'])
def getall():
    return str(TODOLIST)

if __name__ == "__main__":
    app.run(debug=True)
