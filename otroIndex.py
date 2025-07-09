from flask import Flask, jsonify, request 


app = Flask(__name__)

#metpfo
@app.route("/message", methods = ["GET"])
def get_message():
    return jsonify({"msg":"Hola desde el GET"}),201
#jsonify convierte nuestro contenido a JSON
#y asi se ve como una direccion de un Api


@app.route("/message", methods = ["POST"])
def get_message():
    return jsonify({"msg":"Hola desde el POST"}),201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
#hasta la linea 7 colocar en los templates de flask, para ejecutar las propiedades


#introducir id en el get
@app.route("/message/<id>", methods = ["GET"])
def get_message(id):
    return jsonify({"msg":"Hola desde el GET", "user":f"eres{id}"}),201


@app.route("/register", method=[POST])
def register_user():

    body = request.get_json(silent = True)
    if body is None:
        return jsonify ({"msg": "todo mal"}),400
    if "email" not in body:
        return jsonify({"msg":"necesitas introducir email"})
    
    return jsonify({"msg":"todo ok", "email": body["email"]}),200