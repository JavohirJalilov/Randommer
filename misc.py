import requests
from randommer import Randommer


class Misc(Randommer):
    def get_cultures(self, api_key: str) -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key

        Returns:
            list: list of cultures
        '''
        url = self.get_url() + "/api/Misc/Cultures"
        headers = {
            "X-Api-Key": api_key
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        return False
    
    def get_random_address(self, api_key: str, number: int, culture='en') -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key
            number (str): number
            culture (str): culture

        Returns:
            list: random address
        '''
        pass
        url = self.get_url() + "/api/Misc/Random-Address"
        params = {
            "number": number,
            "culture": culture
        }
        headers = {
            "X-Api-Key": api_key
        }
        response = requests.get(url=url, params=params, headers=headers)
        if response.status_code == 200:
            return response.json()
        return False
misc = Misc()
key = "f1ab06cd2da14928a4f4299e85162d76"
print(misc.get_random_address(api_key=key, number=32))