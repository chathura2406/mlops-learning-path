import requests

class CryptoTracker:
    def __init__(self):
        # Api me paara CoinGecko API eka gannawa
        self.api_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

    def get_price(self):
        try:
            # 1. Internet eken data illanawa
            response = requests.get(self.api_url)
            
            if response.status_code == 200:
                data = response.json()
                
                # CoinGecko eke data structure eka tikak wenas:
                # {'bitcoin': {'usd': 95000}}
                price = data["bitcoin"]["usd"]
                
                print(f"Current Bitcoin Price (USD): ${price}")
            else:
                print(f"Data ganna bari una! Status Code: {response.status_code}")
                
        except Exception as e:
            print(f"Connection Error: {e}")

# --- Main Part ---
bitcoin = CryptoTracker()
bitcoin.get_price()