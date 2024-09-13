#Flask class is used to create the application instance, jsonify for convert to json format
from flask import Flask, jsonify

#creating the application instance
app = Flask('__name__')


#Define the route
@app.route('/')
def get_info(): #view function has the business  logic
    return jsonify("Welcome to the first app")


@app.route('/person-details')
def get_person_info(): # view function has the business logic
    return ({"name":"Mahesh", "age":26})