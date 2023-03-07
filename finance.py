import requests
from randommer import Randommer

class Finance(Randommer):
    def get_crypto_address_types(self, api_key: str) -> list:
        '''get available crypto types

        Args:
            api_key (str): api key

        Returns:
            list: list of types
        '''
        url = self.get_url() + "/api/Finance/cryptoAddress/Types"
        headers = {
            "X-Api-Key": api_key
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        return False

    def get_crypto_address(self, crypto_type: str, api_key: str) -> dict:
        '''get available crypto address

        Args:
            crypto_type (str): crypto type
            api_key (str): api key

        Returns:
            dict: crypto address
        '''
        url = self.get_url() + "/api/Finance/cryptoAddress"
        params = {
            "cryptoType": crypto_type
        }
        headers = {
            "X-Api-Key": api_key
        }
        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            return response.json()
        return False

    def get_countries(self, api_key: str) -> list:
        '''get available countries

        Args:
            api_key (str): api key

        Returns:
            list: crypto address
        '''
        url = self.get_url() + "/Finance/Iban/{US}"
        
        headers = {
            "X-Api-Key": api_key
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.url
        return False

    def get_iban_by_country_code(self, country_code: str, api_key: str) -> dict:
        '''get available countries

        Args:
            country_code (str): country code
            api_key (str): api key

        Returns:
            dict: idan data
        '''
        url = self.get_url() + "/api/Finance/Countries"
        params = {
            "country_code": country_code
        }
        headers = {
            "X-Api-Key": api_key
        }
        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            return response.url
        return False
key = "f1ab06cd2da14928a4f4299e85162d76"
f = Finance()

print(f.get_countries(api_key=key))
