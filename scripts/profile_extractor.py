from PyPDF2 import PdfReader


class Profile:
    def __init__(self, filepath: str) -> None:
        self.reader = PdfReader(filepath)

    def get_text(self):
        text = " ".join([page.extract_text() for page in self.reader.pages])
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
    profile = Profile("profiles/profile.pdf")
    text = profile.get_text()
    print(text)
