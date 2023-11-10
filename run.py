from flask import Flask
from app.routes.index import index_blueprint
from app.routes.inicio import inicio_blueprint
from app.routes.users import usuarios_blueprint
from app.routes.user import usuario_especifico_blueprint 
from app.routes.deleteUser import deleta_usuario_blueprint 
from flask_cors import CORS  

app = Flask(__name__)
CORS(app)

app.register_blueprint(index_blueprint)
app.register_blueprint(inicio_blueprint)
app.register_blueprint(usuarios_blueprint)
app.register_blueprint(usuario_especifico_blueprint)
app.register_blueprint(deleta_usuario_blueprint)


if __name__ == '__main__':
  app.run(debug=True)
