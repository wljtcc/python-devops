from flask import app, request, Flask
  
app = Flask(__name__) 

@app.route("/store")
def get_stores():
    name = request.args.get("name")
    id = request.args.get("id")
    return {
        "name": name, 
        "id": id
        }


if __name__ == "__main__": 
    app.run(host='0.0.0.0', port=5000, debug=True)