import requests
from randommer import Randommer


class Name(Randommer):
    def get_name(self, api_key: str, nameType: str, quantity: int) -> list:
        '''get name

        Args:
            api_key (str): api key
            nameType (str): nameType
            quantity (str): number of names

        Returns:
            list: list of names
        '''
        url = self.get_url()
        params = {
            "nameType": nameType,
            "quantity": quantity
        }
        headers = {
            "X-Api-Key": api_key
        }
        response = requests.get(url=f'{url}/api/Name', params=params, headers=headers)
        if response.status_code == 200:
            return response.url
        return False
    
    def get_name_suggestions(self, api_key: str, startingWords: str) -> list:
        '''get name suggestions

        Args:
            api_key (str): api key
            startingWords (str): startingWords

        Returns:
            list: list of name suggestions
        '''
        url = self.get_url() + "/api/Name/Suggestions"
        params = {
            "startingWords": startingWords
        }
        headers = {
            "X-Api-Key": api_key
        }
        response = requests.get(url=url, params=params, headers=headers)
        if response.status_code == 200:
            return response.json()
        return False
    
    def get_name_cultures(self, api_key: str) -> list:
        '''get available cultures

        Args:
            api_key (str): api key

        Returns:
            list: list of names
        '''
        url = self.get_url()
        headers = {
            "X-Api-Key": api_key
        }
        response = requests.get(url=f'{url}/api/Name/Cultures', headers=headers)
        if response.status_code == 200:
            return response.json()
        return False

name = Name()
key = "f1ab06cd2da14928a4f4299e85162d76"
print(name.get_name(api_key=key, nameType="John, Maccarti, John Maccarti", quantity=3))