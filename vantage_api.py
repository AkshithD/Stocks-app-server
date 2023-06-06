from flask import Blueprint, jsonify, request
import requests
import os

bp = Blueprint('vantage_api', __name__)

@bp.route('/api/vantage/<keyword>', methods=['GET'])
def search_stocks(keyword):
    url = "https://alpha-vantage.p.rapidapi.com/query"

    querystring = {"keywords":keyword,"function":"SYMBOL_SEARCH","datatype":"json"}

    headers = {
        "X-RapidAPI-Key": os.environ.get('api_key'),
        "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = response.json()
    return jsonify(data=data)


@bp.route('/api/popular_stocks', methods=['GET'])
def get_popular_stocks():
    stocks = [
  {
    "symbol": "AAPL",
    "name": "Apple Inc",
    "currency": "USD",
    "exchange": "NASDAQ",
    "mic_code": "XNGS",
    "country": "United States",
    "type": "Common Stock"
  },
  {
    "symbol": "MSFT",
    "name": "Microsoft Corporation",
    "currency": "USD",
    "exchange": "NASDAQ",
    "mic_code": "XNGS",
    "country": "United States",
    "type": "Common Stock"
  },
  {
    "symbol": "AMZN",
    "name": "Amazon.com, Inc.",
    "currency": "USD",
    "exchange": "NASDAQ",
    "mic_code": "XNGS",
    "country": "United States",
    "type": "Common Stock"
  },
  {
    "symbol": "GOOGL",
    "name": "Alphabet Inc. Class A",
    "currency": "USD",
    "exchange": "NASDAQ",
    "mic_code": "XNGS",
    "country": "United States",
    "type": "Common Stock"
  },
  {
    "symbol": "FB",
    "name": "Facebook, Inc. Class A",
    "currency": "USD",
    "exchange": "NASDAQ",
    "mic_code": "XNGS",
    "country": "United States",
    "type": "Common Stock"
  },
  {
    "symbol": "TSLA",
    "name": "Tesla, Inc.",
    "currency": "USD",
    "exchange": "NASDAQ",
    "mic_code": "XNGS",
    "country": "United States",
    "type": "Common Stock"
  },
  {
    "symbol": "NVDA",
    "name": "NVIDIA Corporation",
    "currency": "USD",
    "exchange": "NASDAQ",
    "mic_code": "XNGS",
    "country": "United States",
    "type": "Common Stock"
  },
  {
    "symbol": "JPM",
    "name": "JPMorgan Chase & Co.",
    "currency": "USD",
    "exchange": "NYSE",
    "mic_code": "XNYS",
    "country": "United States",
    "type": "Common Stock"
  },
  {
    "symbol": "V",
    "name": "Visa Inc. Class A",
    "currency": "USD",
    "exchange": "NYSE",
    "mic_code": "XNYS",
    "country": "United States",
    "type": "Common Stock"
  },
  {
    "symbol": "BAC",
    "name": "Bank of America Corporation",
    "currency": "USD",
    "exchange": "NYSE",
    "mic_code": "XNYS",
    "country": "United States",
    "type": "Common Stock"
  },
  {
    "symbol": "KO",
    "name": "The Coca-Cola Company",
    "currency": "USD",
    "exchange": "NYSE",
    "mic_code": "XNYS",
    "country": "United States",
    "type": "Common Stock"
  },
  {
    "symbol": "DIS",
    "name": "The Walt Disney Company",
    "currency": "USD",
    "exchange": "NYSE",
    "mic_code": "XNYS",
    "country": "United States",
    "type": "Common Stock"
  },
  {
    "symbol": "NFLX",
    "name": "Netflix, Inc.",
    "currency": "USD",
    "exchange": "NASDAQ",
    "mic_code": "XNGS",
    "country": "United States",
    "type": "Common Stock"
  },
  {
    "symbol": "UBER",
    "name": "Uber Technologies, Inc.",
    "currency": "USD",
    "exchange": "NYSE",
    "mic_code": "XNYS",
    "country": "United States",
    "type": "Common Stock"
  },
  {
    "symbol": "LYFT",
    "name": "Lyft, Inc. Class A",
    "currency": "USD",
    "exchange": "NASDAQ",
    "mic_code": "XNGS",
    "country": "United States",
    "type": "Common Stock"
  },
  {
    "symbol": "SBUX",
    "name": "Starbucks Corporation",
    "currency": "USD",
    "exchange": "NASDAQ",
    "mic_code": "XNGS",
    "country": "United States",
    "type": "Common Stock"
  },
  {
    "symbol": "INTC",
    "name": "Intel Corporation",
    "currency": "USD",
    "exchange": "NASDAQ",
    "mic_code": "XNGS",
    "country": "United States",
    "type": "Common Stock"
  },
  {
    "symbol": "ADBE",
    "name": "Adobe Inc.",
    "currency": "USD",
    "exchange": "NASDAQ",
    "mic_code": "XNGS",
    "country": "United States",
    "type": "Common Stock"
  },
  {
    "symbol": "CRM",
    "name": "salesforce.com, inc.",
    "currency": "USD",
    "exchange": "NYSE",
    "mic_code": "XNYS",
    "country": "United States",
    "type": "Common Stock"
  },
  {
    "symbol": "MRK",
    "name": "Merck & Co., Inc.",
    "currency": "USD",
    "exchange": "NYSE",
    "mic_code": "XNYS",
    "country": "United States",
    "type": "Common Stock"
  },
  {
    "symbol": "PFE",
    "name": "Pfizer Inc.",
    "currency": "USD",
    "exchange": "NYSE",
    "mic_code": "XNYS",
    "country": "United States",
    "type": "Common Stock"
  },
  {
    "symbol": "T",
    "name": "AT&T Inc.",
    "currency": "USD",
    "exchange": "NYSE",
    "mic_code": "XNYS",
    "country": "United States",
    "type": "Common Stock"
  },
  {
    "symbol": "WMT",
    "name": "Walmart Inc.",
    "currency": "USD",
    "exchange": "NYSE",
    "mic_code": "XNYS",
    "country": "United States",
    "type": "Common Stock"
  },
  {
    "symbol": "CSCO",
    "name": "Cisco Systems, Inc.",
    "currency": "USD",
    "exchange": "NASDAQ",
    "mic_code": "XNGS",
    "country": "United States",
    "type": "Common Stock"
  },
  {
    "symbol": "NKE",
    "name": "Nike, Inc. Class B",
    "currency": "USD",
    "exchange": "NYSE",
    "mic_code": "XNYS",
    "country": "United States",
    "type": "Common Stock"
  },
  {
    "symbol": "ORCL",
    "name": "Oracle Corporation",
    "currency": "USD",
    "exchange": "NYSE",
    "mic_code": "XNYS",
    "country": "United States",
    "type": "Common Stock"
  },
  {
    "symbol": "VZ",
    "name": "Verizon Communications Inc.",
    "currency": "USD",
    "exchange": "NYSE",
    "mic_code": "XNYS",
    "country": "United States",
    "type": "Common Stock"
  },
  {
    "symbol": "PG",
    "name": "The Procter & Gamble Company",
    "currency": "USD",
    "exchange": "NYSE",
    "mic_code": "XNYS",
    "country": "United States",
    "type": "Common Stock"
  },
  {
    "symbol": "BA",
    "name": "The Boeing Company",
    "currency": "USD",
    "exchange": "NYSE",
    "mic_code": "XNYS",
    "country": "United States",
    "type": "Common Stock"
  },
  {
    "symbol": "COST",
    "name": "Costco Wholesale Corporation",
    "currency": "USD",
    "exchange": "NASDAQ",
    "mic_code": "XNGS",
    "country": "United States",
    "type": "Common Stock"
  },
  {
    "symbol": "MCD",
    "name": "McDonald's Corporation",
    "currency": "USD",
    "exchange": "NYSE",
    "mic_code": "XNYS",
    "country": "United States",
    "type": "Common Stock"
  },
  {
    "symbol": "AMD",
    "name": "Advanced Micro Devices, Inc.",
    "currency": "USD",
    "exchange": "NASDAQ",
    "mic_code": "XNGS",
    "country": "United States",
    "type": "Common Stock"
  },
  {
    "symbol": "GOOG",
    "name": "Alphabet Inc. Class C",
    "currency": "USD",
    "exchange": "NASDAQ",
    "mic_code": "XNGS",
    "country": "United States",
    "type": "Common Stock"
  }
]


    return jsonify(stocks=stocks)