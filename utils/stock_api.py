
import requests
import config

def get_stock_report(stock_name):
    try:
        # Replace with your stock API endpoint
        api_url = f"https://api.example.com/stock/{stock_name}?apikey={config.STOCK_API_KEY}"
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            return (
                f"Current Price: {data['price']}
"
                f"Recommendation: {data['recommendation']}
"
                f"Change: {data['change']}
"
                f"Volume: {data['volume']}"
            )
        return None
    except Exception as e:
        print(f"Error fetching stock report: {e}")
        return None
