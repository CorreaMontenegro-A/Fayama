from flask import Flask
from routes.main import main

# Creación de la aplicación Flask
app = Flask(__name__)

# Registro del blueprint principal
app.register_blueprint(main)

# Configuración para modo debug
if __name__ == '__main__':
    app.run(debug=True)
