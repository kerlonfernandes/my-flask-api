from flask import Flask, Blueprint

app = Flask(__name__)

inicio_blueprint = Blueprint('inicio', __name__)

@inicio_blueprint.route('/inicio')
def index():
  return 'Inicio'

app.register_blueprint(inicio_blueprint)

if __name__ == '__main__':
  app.run(debug=True)