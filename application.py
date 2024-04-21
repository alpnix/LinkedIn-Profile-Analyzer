from flask import Flask, render_template, request
import openai
from scripts import (
    linkedin_scraper,
    profile_extractor,
    profile_analyzer,
    courses_scraper,
)


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    profile_link = request.form.get("linkedin")
    profile_pdf = request.files["linkedin_file"]
    job = request.form.get("job")

    tos = request.form.get("tos")
    if tos == None:
        return render_template(
            "index.html", tos_message="Agree to Information Release to Use Our Service"
        )

    job_scraping = linkedin_scraper.JobScraper(keywords=job, location="United States")
    job_data = job_scraping.scrape()

    profile_extraction = profile_extractor.Profile(profile_pdf)
    profile_text = profile_extraction.get_text()

    profile_analysis = profile_analyzer.ProfileAnalyzer(profile=profile_text, job=job)
    profile_feedback, recommended_skills = profile_analysis.analyze()

    courses_scraping = courses_scraper.CourseScraper(recommended_skills)
    courses = courses_scraping.scrape()

    print(profile_feedback)
    print(recommended_skills)
    print(job_data)
    # print(type(job_data[0]))
    print(courses)
    # print(type(courses[0]))

    return render_template(
        "index.html",
        profile_feedback=profile_feedback + str(recommended_skills),
        jobs=job_data,
        courses=courses,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5500)
