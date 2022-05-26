from flask import Flask
from routes.routes import route
app = Flask(__name__)
app.register_blueprint(route)
app.secret_key="abc"
app.config['UPLOAD_FOLDER'] = 'src\\media\\profile'
# app.config['UPLOAD_FOLDER'] = 'F:\\Flask\\Flask API with Postgre\\src\\media\\profile'
app.config['UPLOAD_FOLDER_FOR_POST'] = 'src\\media\\post'