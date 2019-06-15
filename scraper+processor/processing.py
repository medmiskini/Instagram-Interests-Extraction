import json
from interests import INTERESTS
from text_api import TextApi
from text_similarity import SimilarApi
from utils import list_to_string, deemojify

# Final script for score Calculation
# Needs to run on a json file that has run through the image api processing (output of apply_imgapi)

class UserProcessing:
    def __init__(self, user_dict):
        self.user_dict = user_dict
        self.photo_count = 1
        self.content_count = 1

    def get_score_dict(self):
        score_dict = {}
        for counter, (post, post_dict) in enumerate(self.user_dict['posts'].items()):
            # image processing
            self.photo_count += 1
            post_dict['img_topic'] = TextApi(list_to_string(post_dict['img_api'])).get_response()
            for interest in INTERESTS:
                key = interest[0]
                interest_score = 0
                if post_dict.get('img_topic', None):
                    for j,keyword in enumerate(interest):
                        print(j)
                        for i, (topic,prob) in enumerate(post_dict['img_topic'].items()):
                            try:
                                interest_score += SimilarApi(topic, keyword).get_response() * prob
                            except:
                                pass
                            if i==2:
                                break
                        if j==1:
                            interest_score = interest_score / 6
                        else:
                            interest_score = interest_score / 3
                if score_dict.get('p_'+ key, None):
                    score_dict['p_'+ key] = score_dict['p_'+ key] +interest_score
                else:
                    score_dict['p_' + key] = interest_score
            # caption/tags processing
            text = None
            if post_dict['hashtags']:
                text = ' '.join(post_dict['hashtags'])
                self.content_count += 1
            elif post_dict['caption']:
                text = deemojify(post_dict['caption'])
                self.content_count += 1
            if text:
                post_dict['content_topic'] = TextApi(text).get_response()
                for interest in INTERESTS:
                    key = interest[0]
                    interest_score = 0
                    if post_dict.get('content_topic',None):
                        for j, keyword in enumerate(interest):
                            for i, (topic, prob) in enumerate(post_dict['content_topic'].items()):
                                interest_score += SimilarApi(topic, keyword).get_response() * prob
                                if i == 1:
                                    break
                            if j == 2:
                                interest_score = interest_score / 6
                            else:
                                interest_score = interest_score / 3
                    if score_dict.get(key, None):
                        score_dict[key] = score_dict[key] + interest_score
                    else:
                        score_dict[key] = interest_score
            if counter == 10:
                break
        for interest,score in score_dict.items():
            try:
                if interest.startswith('p_'):
                    score_dict[interest] = score/self.photo_count
                else:
                    score_dict[interest] = score/self.content_count
            except:
                pass
        return score_dict

json_filename = 'final2.json'
with open(json_filename, 'r') as f:
    datastore = json.load(f)
for user, user_dict in datastore.items():
    user_dict['scoring'] = UserProcessing(user_dict).get_score_dict()
    with open('final_safe.json', 'a') as fs:
        json.dump({user: user_dict}, fs)
with open('final_data.json', 'a') as fp:
    json.dump(datastore, fp)


