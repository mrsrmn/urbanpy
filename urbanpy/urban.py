import requests
import json
from .result import Result


class Urban:

    def __init__(self, key):
        self.key = key

    def search(self, name):
        """
        :return: Info about the word that got searched
        """

        url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
        querystring = {"term": name}

        headers = {
            'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
            'x-rapidapi-key': self.key
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        final = json.loads(response.content)["list"][0]

        return Result(
            definition=final["definition"],
            permalink=final["permalink"],
            thumbs_up=final["thumbs_up"],
            thumbs_down=final["thumbs_down"],
            sounds_url=final["sound_urls"],
            author=final["author"],
            defid=final["defid"],
            written_on=final["written_on"],
            example=final["example"]
        )
