import requests
import config

def get_stock_report(stock_name):
    try:
        # API request to fetch stock data
        api_url = f"https://finnhub.io/api/v1/quote?symbol={stock_name}&token={config.STOCK_API_KEY}"
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            # Ensure all required keys exist in the response
            if 'c' in data and 'h' in data and 'l' in data and 'o' in data and 'pc' in data:
                return (
                    f"Current Price: {data['c']}\n"
                    f"High Price: {data['h']}\n"
                    f"Low Price: {data['l']}\n"
                    f"Open Price: {data['o']}\n"
                    f"Previous Close: {data['pc']}"
                )
            else:
                return "Error: Missing data in the response."
        else:
            return "Error: Failed to fetch stock data."
    except Exception as e:
        print(f"Error fetching stock report: {e}")
        return "Error: An unexpected issue occurred while fetching stock data."
