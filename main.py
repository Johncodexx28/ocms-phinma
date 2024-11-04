from flask import Flask,redirect,render_template
from werkzeug.utils import secure_filename 
from werkzeug.security import generate_password_hash,check_password_hash
import re,os 
from datetime import datetime
import json




class Online_Classroom_Management_System:
    def __init__(self, name):
        self.app = Flask(name)
        self.app.secret_key = 'OCSMSPHINMAUI'    
        
        
    def define_routes(self):
        
        @self.app.route('/')
        def homepage():
            return "<h1> testing <h1>"
        
        
    def run(self):
        self.app.run(host='0.0.0.0', port=5500, debug=True)
        

OCMS = Online_Classroom_Management_System(__name__)
OCMS.define_routes()
OCMS.run()
        