from flask import Flask
from flask_jwt_extended import JWTManager
from config import config
# Routes
from routes import PasswordRoutes
from routes import AuthRoutes

app = Flask(__name__)

def page_not_found(error):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

if __name__ == '__main__':
    app.config.from_object(config['development']) # This is the line that does the magic
    
    jwt = JWTManager(app)  # Inicializa JWTManager con tu aplicación
    
    # Configura la clave secreta del JWTManager
    app.config['JWT_SECRET_KEY'] = config['development'].JWT_SECRET_KEY
    
    # Blueprints
    app.register_blueprint(PasswordRoutes.pwd_routes, url_prefix='/api/v1/')
    app.register_blueprint(AuthRoutes.auth_routes, url_prefix='/api/v1/auth')
    
    # Error handlers
    app.register_error_handler(404, page_not_found)
    #app.register_error_handler(500, page_not_found)
    app.run()
