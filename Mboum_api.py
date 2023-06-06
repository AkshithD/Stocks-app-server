from flask import Blueprint, jsonify, request
import requests
import os

bp = Blueprint('mboum_api', __name__)

@bp.route('/api/mboum/<symbol>', methods=['GET'])
def get_stock(symbol):
    url = "https://mboum-finance.p.rapidapi.com/op/option"

    querystring = {"symbol":symbol}

    headers = {
        "X-RapidAPI-Key": os.environ.get('api_key'),
        "X-RapidAPI-Host": "mboum-finance.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    return jsonify(response.json())

@bp.route('/api/mboum/news', methods=['GET'])
def get_news():
    url = "https://mboum-finance.p.rapidapi.com/ne/news"

    headers = {
        "X-RapidAPI-Key": os.environ.get('api_key'),
        "X-RapidAPI-Host": "mboum-finance.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    return jsonify(response.json())
