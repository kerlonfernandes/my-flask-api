from flask import Flask, Blueprint, render_template, jsonify
from flask_cors import CORS  
from app.models.database import Database
from app.models.helpers import ReturnData 
from app.config import * 

returnData = ReturnData()

app = Flask(__name__)
CORS(app)

deleta_usuario_blueprint = Blueprint('deleta_usuario', __name__)

@deleta_usuario_blueprint.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id:int):
    return jsonify(returnData.deleteUser(id))
app.register_blueprint(deleta_usuario_blueprint)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    