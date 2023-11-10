from flask import Flask, Blueprint, render_template, jsonify
from flask_cors import CORS  
from app.models.database import Database
from app.models.helpers import ReturnData 
from app.config import * 
returnData = ReturnData()

app = Flask(__name__)
CORS(app)
# , resources={r"/*": {"origins": "*"}}

usuarios_blueprint = Blueprint('usuarios', __name__)

@usuarios_blueprint.route('/users')
def usuarios():
    return jsonify(returnData.getUsers())
app.register_blueprint(usuarios_blueprint)

if __name__ == '__main__':
  app.run(debug=True)