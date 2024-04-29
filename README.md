# LinkedLeverage - LinkedIn Profile Enhancement Tool

LinkedLeverage is a comprehensive tool designed to help college students and job seekers optimize their LinkedIn profiles, discover relevant job opportunities, and enhance their skills through tailored course recommendations. Our tool analyzes LinkedIn profiles against desired job roles, provides actionable feedback, and connects users with potential job listings and educational resources.

## Features

- **LinkedIn Profile Analysis:** Extracts and analyzes data from LinkedIn profiles to give users feedback on how well their profile matches their desired job roles.
- **Job Matching:** Scrapes LinkedIn for job postings that align with the user's skills and aspirations.
- **Course Recommendations:** Suggests relevant courses to users to help them close the skills gap identified during the profile analysis.

## Getting Started

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/alpnix/LinkedLeverage.git
```

Navigate to the project directory:

```bash
cd LinkedLeverage
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Usage

Run the Flask application:

```bash
python application.py # or python3 depending on your environment setup
```

Access the web application by navigating to localhost:5000 in your web browser.

## Structure

- `application.py`: The Flask server script that runs the backend of the tool.
- `requirements.txt`: A list of required Python packages for the project.
- `/templates`: This directory contains the HTML templates for the frontend.
  - `index.html`: The main webpage template that users interact with.
- `/scripts`: This directory contains the Python scripts for the tool's functionality.
  - `courses_scraper.py`: Scrapes Coursera for courses related to the user's profile.
  - `linkedin-profile-extractor.py`: Extracts profile data from a user's LinkedIn PDF.
  - `linkedin_scraper.py`: Scrapes LinkedIn for job listings that match the user's profile and aspirations.
  - `profile_analyzer.py`: Analyzes the extracted LinkedIn profile data and provides feedback.

## Team Members

- Alp Niksarli (Product Owner, Developer)
- Sky Luo (Scrum Master, Developer)
- Donald Lin (Scrum Master, Developer)
- Delario Nance Jr. (Scrum Master, Developer)
