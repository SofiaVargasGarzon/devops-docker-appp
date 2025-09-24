from flask import Flask, jsonify

app = Flask(_name_)

@app.get("/")
def root():
    return jsonify(message="¡Hola desde DevOps + Docker!")

@app.get("/health")
def health():
    return jsonify(status="ok")
    
if _name_ == "_main_":
    app.run(host="0.0.0.0", port=8080)
