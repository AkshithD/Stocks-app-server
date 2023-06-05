from flask import Flask
from flask_cors import CORS, cross_origin
import db
import vantage_api
import twelve_api
import Mboum_api

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Register the blueprints
app.register_blueprint(db.bp)
app.register_blueprint(vantage_api.bp)
app.register_blueprint(twelve_api.bp)
app.register_blueprint(Mboum_api.bp)

# Main route for the application
@app.route('/')
def home():
    return 'Hello, World!'

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5069))  # Use the value of PORT environment variable or default to 5000
    print("app is running on port:", port)
    app.run(host='0.0.0.0', port=port)