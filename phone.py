import requests
from randommer import Randommer


class Phone(Randommer):
    def generate(self, api_key: str, CountryCode: str, Quantity: int) -> list:
        '''get bulk telephone numbers for a country

        Args:
            api_key (str): api key
            CountryCode (str): CountryCode ex: 'uz'
            Quantity (str): Quantity

        Returns:
            list: list of phone numbers
        '''
        url = self.get_url()
        params = {
            "CountryCode": CountryCode,
            "Quantity": Quantity
        }
        headers = {
            "X-Api-Key": api_key
        }
        response = requests.get(url=f'{url}/api/Phone/Generate', params=params, headers=headers)
        if response.status_code == 200:
            return response.json()
        return False
    
    def get_IMEI(self, api_key: str, Quantity: int) -> list:
        '''get bulk imei

        Args:
            api_key (str): api key
            Quantity (str): Quantity

        Returns:
            list: list of phone numbers
        '''
        url = self.get_url()
        params = {
            "Quantity": Quantity
        }
        headers = {
            "X-Api-Key": api_key
        }
        response = requests.get(url=f'{url}/api/Phone/IMEI', params=params, headers=headers)
        if response.status_code == 200:
            return response.json()
        return False
    
    def is_valid(self, api_key: str, telephone: str, CountryCode: str) -> bool:
        '''get bulk imei

        Args:
            api_key (str): api key
            telephone (str): phone number
            CountryCode (str): CountryCode ex: 'uz'

        Returns:
            bool: is valid
        '''
        url = self.get_url()
        params = {
            "telephone": telephone,
            "CountryCode": CountryCode
        }
        headers = {
            "X-Api-Key": api_key
        }
        response = requests.get(url=f'{url}/api/Phone/Validate', params=params, headers=headers)
        if response.status_code == 200:
            return response.json()
        return False
    
    def get_countries(self, api_key: str) -> list:
        '''get countries

        Args:
            api_key (str): api key

        Returns:
            list: lsit of countries
        '''
        url = self.get_url()
        headers = {
            "X-Api-Key": api_key
        }
        response = requests.get(url=f'{url}/api/Phone/Countries', headers=headers)
        if response.status_code == 200:
            return response.json()
        return False

phone = Phone()
key = "f1ab06cd2da14928a4f4299e85162d76"
print(phone.get_countries(api_key=key))