from flask import Flask
from config import Config
from extension import db, jwt
from auth import auth_bp
from routes import routes_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(routes_bp)

@app.route('/')
def index():
    return "Product Inventory API is running!"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)