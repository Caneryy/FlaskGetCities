from flask import Blueprint, request, Response
from bson.json_util import dumps

from .extensions import mongo

main = Blueprint('main', __name__)

@main.route('/')
def index():
    country_code = request.args.get('country_code')
    city_collection = mongo.db.cities
    cities = dumps(city_collection.find({"country_code": country_code}))

    return Response(cities, mimetype='application/json')