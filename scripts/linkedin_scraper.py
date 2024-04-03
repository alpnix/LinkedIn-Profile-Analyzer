import requests
from bs4 import BeautifulSoup


class job_scraper:
    def __init__(self, keywords, location):
        self.keywords = keywords
        self.location = location

    def scrape(self):
        linkedin_search_url = (
            "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?"
        )
        # Format the search URL with the keywords and location
        search_url = f"{linkedin_search_url}keywords={self.keywords}&location={self.location}&start=0"

        # Send the HTTP request to LinkedIn
        response = requests.get(search_url)

        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all job listings on the page
        jobs_on_this_page = soup.find_all("li")

        job_data = []

        # Extract details for each job
        for job in jobs_on_this_page:
            try:
                job_id = (
                    job.find("div", {"class": "base-card"})
                    .get("data-entity-urn")
                    .split(":")[3]
                )
                job_details_url = (
                    f"https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{job_id}"
                )

                # Fetch each job's details
                job_details_response = requests.get(job_details_url)
                job_soup = BeautifulSoup(job_details_response.text, "html.parser")

                company_name = (
                    job_soup.find("div", {"class": "top-card-layout__card"})
                    .find("a")
                    .find("img")
                    .get("alt")
                )
                job_title = (
                    job_soup.find("div", {"class": "top-card-layout__entity-info"})
                    .find("a")
                    .text.strip()
                )
                job_seniority = (
                    job_soup.find("ul", {"class": "description__job-criteria-list"})
                    .find("li")
                    .text.replace("Seniority level", "")
                    .strip()
                )
                job_link = (
                    job_soup.find("div", {"class": "top-card-layout__entity-info"})
                    .find("a")
                    .get("href")
                )

                # Append the job details to the job_data list
                if all([company_name, job_title, job_seniority, job_link]):
                    job_data.append(
                        {
                            "company_name": company_name,
                            "job_title": job_title,
                            "job_seniority": job_seniority,
                            "job_link": job_link,
                        }
                    )
            except Exception as e:
                # Handle potential errors in job detail extraction
                print(f"Error: {e}")

        return job_data


if __name__ == "__main__":
    scraper = job_scraper("Software Engineer", "New York")
    print(scraper.scrape())
