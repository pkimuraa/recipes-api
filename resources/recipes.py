from flask import request
from flask_restplus import Resource

class Recipes(Resource):

    @get_recipes.route("/recipe", methods=['GET', 'POST'])
    def recipes():
        error = None
        if request.method == 'POST':
            return 'Hello World'
        else:
            return 'Adios World'