# Importación de Blueprint y render_template de Flask
from flask import Blueprint, render_template

# Creación del Blueprint 'main' para organizar las rutas principales
main = Blueprint('main', __name__)

# Ruta principal que renderiza la página de inicio
@main.route('/')
def home():
    return render_template('home.html')

# Ruta para la página de servicios
@main.route('/servicios')
def servicios():
    return render_template('servicios.html')

# Ruta para la página de contacto
@main.route('/contacto')
def contacto():
    return render_template('contacto.html') 