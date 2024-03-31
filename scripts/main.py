import os
import spacy
import ast

from openai import OpenAI

# from dotenv import load_dotenv

# load_dotenv()

key = "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"


def profile_keyword_extraction(profile):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(profile)
    return doc.ents


def evaluate(profile_keywords, job):
    prompt = """
    I want to be a {}. These are some keywords of my experience: {}. 
    How much does my experience keywords eval with the job's technical and softskills? 
    What else should I learn? 
    Return only a short, concise evaluation followed by a list of skills I need to learn in a Python list [] format.""".format(
        job, profile_keywords
    )

    client = OpenAI(api_key=key)
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a career advisor."},
            {"role": "user", "content": prompt},
        ],
    )
    response = completion.choices[0].message.content  # string representation of a list
    print(response)

    skills_start = response.index("[")
    skills_end = response.index("]")
    eval = response[:skills_start]
    skills = ast.literal_eval(
        response[skills_start : skills_end + 1]
    )  # turn string into list

    print(eval, "***", skills)
    return eval, skills


def main():
    profile_key_words = profile_keyword_extraction(
        """
    I am a third-year computer science major and an international student at Davidson College. 
    I am pursuing the Columbia Combined Plan, where I will spend my fourth and fifth undergrad years at the School of Engineering at Columbia University. 
    I will graduate in 2026 with a BS from Davidson College and a BSE from Columbia University, both in CS.
    I love coding - solving complex problems and shipping codes used by millions excite me. 
    My favorite tools are Python/Flask, Java, Javascript, SQL, and HTML/CSS, and I am familiar with cloud platforms like AWS, Azure, and Google Cloud. 
    I have built and deployed several cloud-based Python programs to solve real-life problems for my school's VR lab, companies, and my own project. 
    I am pursuing a career in software engineering.
    I am currently the sponsorship lead at Hack@Davidson, a Major League Hacking event.
    """
    )
    eval, recc_skills = evaluate(profile_key_words, "SWE")


if __name__ == "__main__":
    main()
