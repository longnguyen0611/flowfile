from flask import Flask, request, jsonify
from trading import Trading

app = Flask(__name__)

@app.route('/api/stocks')
def get_stocks():
    tickers = request.args.get('tickers', 'VCB,VNM').split(',')
    trading = Trading(symbol=tickers[0])
    df = trading.price_board(symbol_ls=tickers, std_columns=True, to_df=True)
    return df.to_json(orient='records')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
