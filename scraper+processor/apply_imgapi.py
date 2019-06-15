import json

from image_api import PhotoApi

json_filename = 'final2.json'
with open(json_filename, 'r') as f:
    datastore = json.load(f)
for user, user_dict in datastore.items():
    for post,post_dict in user_dict['posts'].items():
        post_dict['img_api'] = PhotoApi().get_parsed_response(post_dict['photo_url'])
    with open('safe.json', 'a') as fs:
        json.dump({user: user_dict}, fs)
with open('img_data.json', 'a') as fp:
    json.dump(datastore, fp)