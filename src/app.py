from flask import Flask
from config import config
# Routes
from routes import Password

app = Flask(__name__)

def page_not_found(error):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

if __name__ == '__main__':
    app.config.from_object(config['development']) # This is the line that does the magic
    
    # Blueprints
    app.register_blueprint(Password.main, url_prefix='/api/pass')
    
    # Error handlers
    app.register_error_handler(404, page_not_found)
    #app.register_error_handler(500, page_not_found)
    app.run()
