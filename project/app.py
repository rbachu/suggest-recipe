from flask import Flask, Blueprint, render_template
from os import environ

# Blueprints
from routes.home import home_bp
from routes.ingredients import ingredients_bp

blueprints = (home_bp, ingredients_bp)

def create_app():
    app = Flask(__name__)

    get_config(app)

    register_blueprint(app, blueprints)

    return app
# end create_app

def get_config(app):
    app.config.from_mapping(
        SECRET_KEY='ranjithks',
    )

    app.config.from_pyfile('config.py', silent=True)
    
    envFLASK = environ.get('FLASK_ENV')

    if envFLASK == 'development':
        app.debug = True
    else:
        app.debug = False
    
# end get_config

def register_blueprint(app, blueprints):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    # Configure explicit url routes to home blueprint
    app.add_url_rule('/', endpoint='index')
    app.add_url_rule('/home', endpoint='home')
    
# end register_blueprint

if __name__ == '__main__':
    app = create_app()
    app.run()
# end main()