import requests
from bs4 import BeautifulSoup

class Profile:
    def __init__(self, profile_url):
        self.url = profile_url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
            'From': 'alniksarli@davidson.edu'
        }


    def get_text(self):
        response = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup)
        text = [section.get_text() for section in soup.select('.artdeco-card.pv-profile-card.break-words')]
        return text

    def get_summary(self):
        pass

    def get_experience(self):
        pass

    def get_education(self):
        pass

    def get_certifications(self):
        pass

    def get_skills(self):
        pass

    def get_courses(self):
        pass


if __name__ == "__main__":
    profile = Profile("https://www.linkedin.com/in/alpniksarli/")
    text = profile.get_text()
    print(text)
