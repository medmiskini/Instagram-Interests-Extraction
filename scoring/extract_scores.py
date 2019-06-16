import json
from scraper.interests import INTERESTS

class ScoresExtractor:


    def __init__(self):
        self.final_dict = {}

    def open_dataset(self):
        # data_scraped_filename = 'data_scraped.json'
        data_final_filename = 'data_final3.json'
        with open(data_final_filename, 'r') as f:
            self.data_final = json.load(f)

    def score_labelize(self):
        self.array = []
        self.p_array = []
        for interest in INTERESTS:
            key = interest[0]
            self.p_array.append("p_"+key)
            self.array.append(key)


    def score_calc(self):
        user_object = {}


        for user, user_dict in self.data_final.items():
            user_object['Username'] = user
            scoring = user_dict['scoring']

            for category in self.array:
                p_category = "p_" + category
                user_object[category] = scoring[category] * 0.85 + scoring[p_category] * 0.15

            with open('data_final_clustering3.json', 'a') as fs:
                json.dump(user_object, fs)


se = ScoresExtractor()
se.open_dataset()
se.score_labelize()
se.score_calc()

