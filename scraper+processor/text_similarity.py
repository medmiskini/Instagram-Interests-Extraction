import requests


class SimilarApi:
    SIMILAR_API = 'https://www.twinword.com//api/v6/text/similarity/'

    def __init__(self, text1, text2):
        self.text1 = text1
        self.text2 = text2

    def get_response(self):
        response = requests.post(url=self.SIMILAR_API,
                                 data={'text1': self.text1,
                                       'text2': self.text2})
        try:
            return response.json().get('similarity')
        except Exception:
            return 0