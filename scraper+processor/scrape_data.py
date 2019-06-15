import json

import instaloader
from instaloader import Profile

L = instaloader.Instaloader()


class DataScraper:
    dataset = {}

    def __init__(self):
        self.file = open("insta_accounts.txt", "r")

    def scrape_users(self):
        for line in self.file:
            us_in = str(line.strip())
            splited = us_in.split(':')
            try:
                self.scrape_user(splited[0].strip(), splited[1].strip())
            except KeyboardInterrupt:
                with open('data.json', 'a') as fp:
                    json.dump(self.dataset, fp)
            except:
                with open('data.json', 'a') as fp:
                    json.dump(self.dataset, fp)
        with open('data.json', 'a') as fp:
            json.dump(self.dataset, fp)

    def scrape_user(self, username, interest):
        print(username)
        profile = Profile.from_username(L.context, username)
        print(profile)
        self.dataset[username] = {}
        data_dict = self.dataset[username]
        data_dict['interests'] = interest
        posts = [post for post in profile.get_posts()]
        self.scrape_posts(posts, data_dict)

    def scrape_posts(self, posts, user_dict):
        user_dict['posts'] = {}
        for counter, post in enumerate(posts):
            print(f'---- still working {counter} ----')
            user_dict['posts'][f'post{counter}'] = {}
            data_dict = user_dict['posts'][f'post{counter}']
            data_dict['caption'] = post.caption
            data_dict['hashtags'] = post.caption_hashtags
            data_dict['photo_url'] = post.url
            if counter == 100:
                break


def start_scraping():
    ds = DataScraper()
    ds.scrape_users()

start_scraping()