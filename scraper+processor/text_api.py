import requests


class TextApi:
    TEXT_API = 'https://www.twinword.com/api/v5/topic/generate/'

    def __init__(self, text):
        self.text = text

    def get_response(self):
        response = requests.post(url=self.TEXT_API,
                                 data={'text': self.text})
        try:
            return response.json().get('topic')
        except Exception:
            return {}
