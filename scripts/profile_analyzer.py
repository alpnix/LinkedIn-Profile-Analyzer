import os
import spacy
import ast

from openai import OpenAI


key = "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"


class ProfileAnalyzer:
    def __init__(self, profile, job):
        self.profile = profile
        self.job = job
        self.profile_keywords = None

    def profile_keyword_extraction(self):
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(self.profile)
        profile_keywords = doc.ents
        self.profile_keywords = profile_keywords

    def analyze(self):
        self.profile_keyword_extraction()

        prompt = """
        I want to be a {}. These are some keywords of my experience: {}. 
        How much does my experience keywords eval with the job's technical and softskills? 
        What else should I learn? 
        Return only a short, concise evaluation followed by a list of skills I need to learn in a Python list [] format.""".format(
            self.job, self.profile_keywords
        )

        client = OpenAI(api_key=key)
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a career advisor."},
                {"role": "user", "content": prompt},
            ],
        )
        response = completion.choices[
            0
        ].message.content  # string representation of a list
        # print(response)

        skills_start = response.index("[")
        skills_end = response.index("]")
        eval = response[:skills_start]
        skills = ast.literal_eval(
            response[skills_start : skills_end + 1]
        )  # turn string into list

        print(eval, "\n", skills)
        return eval, skills


if __name__ == "__main__":
    profile = profile_analyzer(
        """
I am a third-year computer science major and an international student at Davidson College. I am pursuing the Columbia Combined Plan, where I will spend my fourth and fifth undergrad years at the School of Engineering at Columbia University. I will graduate in 2026 with a BS from Davidson College and a BSE from Columbia University, both in CS.

I love coding - solving complex problems and shipping codes used by millions excite me. My favorite tools are Python/Flask, Java, Javascript, SQL, and HTML/CSS, and I am familiar with cloud platforms like AWS, Azure, and Google Cloud. I have built and deployed several cloud-based Python programs to solve real-life problems for my school's VR lab, companies, and my own project. I am pursuing a career in software engineering.

I am currently the sponsorship lead at Hack@Davidson, a Major League Hacking event.
                               """,
        "Software Engineer",
    )
    print(profile.analyze())
