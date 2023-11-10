from flask import Flask, Blueprint

app = Flask(__name__)

index_blueprint = Blueprint('index', __name__)

@index_blueprint.route('/')
def index():
  return 'index!'

app.register_blueprint(index_blueprint)

if __name__ == '__main__':
  app.run(debug=True)