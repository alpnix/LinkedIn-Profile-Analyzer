from flask import Flask, render_template, request
import linkedin_scraper
import profile_analyzer
import profile_extractor

job_scraping = linkedin_scraper.JobScraper()
profile_analysis = profile_analyzer.ProfileAnalyzer()
profile_extraction = profile_extractor.Profile()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5500)
