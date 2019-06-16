import json
from collections import Counter

from scraper.interests import INTERESTS

class InterestClassifier:


    def __init__(self):
        self.final_dict = {}

    def open_dataset(self):
        # data_scraped_filename = 'data_scraped.json'
        data_final_clustering_filename = 'data_final_clustering3.json'
        with open(data_final_clustering_filename, 'r') as f:
            self.data_final_clustering = json.load(f)

    def sort_categories(self):

        for user in self.data_final_clustering:
            score = dict(user)
            score.pop('Username')
            k = Counter(score)
            high = k.most_common(3)
            print(high)
            user['Class'] = high
            with open('data_final_validation3.json', 'a') as fs:
                json.dump(user, fs)



    def keywithmaxval(self, d):
        """ a) create a list of the dict's keys and values;
            b) return the key with the max value"""
        v = list(d.values())
        k = list(d.keys())
        return k[v.index(max(v))]




se = InterestClassifier()
se.open_dataset()
se.sort_categories()


