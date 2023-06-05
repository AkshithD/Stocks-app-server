from flask import Blueprint, jsonify, send_file
from io import BytesIO
import requests
import json
from config import twelve_api_key

bp = Blueprint('twelve_api', __name__)
current_stock = None

@bp.route('/api/twelve', methods=['GET'])
def get_stock():
    querystring = {"country": "United States", "exchange":"NYSE","format":"json"}

    headers = {
        "X-RapidAPI-Key": twelve_api_key,
        "X-RapidAPI-Host": "twelve-data1.p.rapidapi.com"
    }

    response = requests.get('https://twelve-data1.p.rapidapi.com/stocks', headers=headers, params=querystring)
    return jsonify(response.json())

def get_stock_data(symbol):
    url = "https://twelve-data1.p.rapidapi.com/time_series"

    querystring = {"symbol":symbol,"interval":"1month","outputsize":"30","format":"json"}

    headers = {
        "X-RapidAPI-Key": twelve_api_key,
        "X-RapidAPI-Host": "twelve-data1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    global current_stock
    current_stock = response.json()
    return jsonify(current_stock)

@bp.route('/api/twelve/graph/<symbol>', methods=['GET'])
def get_stock_graph(symbol):
    get_stock_data(symbol)
    global current_stock

    if current_stock is None:
        return jsonify(error="Stock data not available")

    # Extract the necessary data from the current_stock JSON
    labels = []
    data = []

    # Process the current_stock JSON data to populate labels and data lists
    for i in range(len(current_stock['values'])-1, -1, -1):
        labels.append(current_stock['values'][i]['datetime'])
        data.append(current_stock['values'][i]['close'])

    # Generate the graph using labels and data
    graph_data = {
        "version": "2",
        "backgroundColor": "transparent",
        "devicePixelRatio": 1.0,
        "format": "png",
        "chart": {
            "type": "line",
            "data": {
                "labels": labels,
                "datasets": [
                    {
                        "label": "Stock Prices",
                        "data": data,
                        "fill": False,
                        "borderColor": "green",
                        "backgroundColor": "green"
                    }
                ]
            }
        }
    }
    graph_json = json.dumps(graph_data)  # Convert to JSON format
    # Your code to generate the graph goes here
    graph_url = "https://quickchart.io/chart"
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(graph_url, headers=headers, data=graph_json)
    if response.status_code == 200:
        # Retrieve the image data
        graph_image_data = response.content
        # Return the image data as a response with the appropriate content type
        return send_file(BytesIO(graph_image_data), mimetype='image/png')
    else:
        return jsonify(error="Failed to generate graph")