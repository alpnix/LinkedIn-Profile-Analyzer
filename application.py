from flask import Flask, render_template, request
import linkedin_scraper
import profile_analyzer
import profile_extractor


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    profile_link = request.form.get("linkedin")
    profile_pdf = request.form.get("linkedin_file")
    job = request.form.get("job")

    job_scraping = linkedin_scraper.JobScraper(keywords=job, location="United States")
    profile_extraction = profile_extractor.Profile(profile_pdf)

    job_data = job_scraping.scrape()
    profile_text = profile_extraction.get_text()

    profile_analysis = profile_analyzer.ProfileAnalyzer(profile=profile_text, job=job)
    profile_feedback = profile_analysis.analyze()

    return render_template(
        "index.html", profile_feedback=profile_feedback, jobs=job_data
    )


if __name__ == "__main__":
    app.run(debug=True, port=5500)
