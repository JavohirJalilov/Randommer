import requests
from randommer import Randommer


class Card(Randommer):
    def get_card(self, api_key: str, type_card=None) -> dict:
        '''get card from randommer
        
        Args:
            api_key (str): api key
            type (str): card type

        Returns:
            dict: card data
        '''
        url = self.get_url() + "/api/card"
        payload = {
            "type": type_card
        }
        headers = {
            "X-Api-Key": api_key
        }
        response = requests.get(url, params=payload, headers=headers)
        if response.status_code == 200:
            return response.json()
        return False

    def get_card_types(self, api_key: str) -> list:
        '''get cars types from randommer

        Args:
            api_key (str): api key
            
        Returns:
            list: list of types
        '''
        base_url = self.get_url()
        headers = {
            "X-Api-Key":api_key
        }
        url = f"{base_url}/api/Card/Types"
        r = requests.get(url, headers=headers)
        return r.json()

card = Card()
key = "f1ab06cd2da14928a4f4299e85162d76"

print(card.get_card_types(key))