import requests
from randommer import Randommer


class SocialNumber(Randommer):
    def get_SocialNumber(self, api_key: str) -> str:
        '''get SocialNumber

        Args:
            api_key (str): api key

        Returns:
            str: number as str
        '''
        url = self.get_url()
        headers = {
            "X-Api-Key": api_key
        }
        response = requests.get(url=f'{url}/api/SocialNumber', headers=headers)
        if response.status_code == 200:
            return response.json()
        return False

soc_num = SocialNumber()
key = "f1ab06cd2da14928a4f4299e85162d76"
print(soc_num.get_SocialNumber(key))