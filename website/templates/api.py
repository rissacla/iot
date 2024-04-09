from flask import Flask, Blueprint, render_template, request, redirect, url_for, session, jsonify
# Define your Blueprint outside create_app functionapi_bp = Blueprint("api", name, url_prefix="/api")
# Replace this with actual processing or storage logic
measurements = []
# Define routes related to api_bp Blueprint@api_bp.route('/')
def index():       
    return "Welcome to the Flask server for receiving device data!"

@api_bp.route('/data', methods=['POST'])
def receive_data():    
    data = request.json
    print("Received data:", data)    
    measurements.append(data)  # Example: Store received data
    return jsonify({"status": "success", "message": "Data received"}), 200

@api_bp.route('/toggleCharger', methods=['POST'])
def toggle_charger():
    charger_state = request.json.get('chargerState')    
    print("Charger state toggled to:", charger_state)    
    return jsonify({"status": "success", "message": "Charger toggled"}), 200

def create_app():    # Create and configure the app    
    app = Flask(__name__, instance_relative_config=True)    
    app.config.from_mapping(        
        SECRET_KEY="enter secret key here",    )    
    # Register blueprints    
    app.register_blueprint(api_bp)    
    return app

# This part is optional, just for running the Flask application directlyif name == "__main__":
    app = create_app()    
    app.run(debug=True)