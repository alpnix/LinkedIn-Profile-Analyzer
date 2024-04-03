import requests
from bs4 import BeautifulSoup

class CourseScraper: 
    def __init__(self, skills):
        self.skills = skills

    def scrape(self):
        coursera_search_url = (
            "https://www.coursera.org/search?"
        )
        course_data = []

        for skill in self.skills: 

            # Format the search URL with the search query and other filters
            search_url = f"{coursera_search_url}query={skill.replace(' ', '%20')}"

            # Send the HTTP request to Coursera
            response = requests.get(search_url)

            # Parse the HTML content
            soup = BeautifulSoup(response.text, "html.parser")

            # Find all courses on the page
            courses_on_the_page = soup.select(".cds-ProductCard-base")

            # Extract details for each job
            for course in courses_on_the_page:
                try:
                    course_title = (
                        course.find("h3")
                        .text.strip()
                    )
                    course_link = (
                        "https://www.coursera.org" +
                        course.find("a")
                        .get("href")
                    )

                    # Append the course details to the course_data list
                    if all([skill, course_title, course_link]):
                        course_data.append(
                            {
                                "skills": skill,
                                "course_title": course_title,
                                "course_link": course_link,
                            }
                        )
                
                except Exception as e:
                    # Handle potential errors in course detail extraction
                    print(f"Error: {e}")

        return course_data


if __name__ == "__main__":
    scraper = CourseScraper(["Python Programming", "Data Science"])
    print(scraper.scrape())
