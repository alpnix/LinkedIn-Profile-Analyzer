import os
import spacy
import ast

from openai import OpenAI


key = "placeholder"


class profile_analyzer:
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
        print(response)

        skills_start = response.index("[")
        skills_end = response.index("]")
        eval = response[:skills_start]
        skills = ast.literal_eval(
            response[skills_start : skills_end + 1]
        )  # turn string into list

        print(eval, "***", skills)
        return eval, skills
