from flask import Flask
app=Flask(__name__)

tasks=[
    {
        'contact':9987644456,
        'name': 'Raju',
        'done':False,
        'id':1
        },
    {
        'contact':9876543222,
        'name': 'Rahul',
        'done':False,
        'id':2
        }]
@app.route("/")
def hello_world():
    return "Hello World"
if(__name__=="__main__"):
    app.run(debug=False)

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "meaasage":"Please provide the data!"
            },400)
    task={
        'id':tasks[-1][id]+1,
        'name':request.json['name'],
        'contact': request.json.get('contact', ""),
        'done':False
        }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"Task added successfully!"
        })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
        })
if(__name__=="__main__"):
    app.run(debug=False)
