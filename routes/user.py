from flask import Flask, Blueprint, render_template, jsonify
from flask_cors import CORS  
from app.models.database import Database
from app.models.helpers import ReturnData 
from app.config import * 

returnData = ReturnData()

app = Flask(__name__)
CORS(app)

usuario_especifico_blueprint = Blueprint('usuario', __name__)

@usuario_especifico_blueprint.route('/user/<int:id>')
def user(id:int):
    return jsonify(returnData.getEspecificUser(id))

app.register_blueprint(usuario_especifico_blueprint)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    