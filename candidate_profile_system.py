class PersonalInfo:

    def __init__(self, name, dob, contact, email):
        self.name = name
        self.dob = dob
        self.contact = contact
        self.email = email

    def display_personal(self):
        print("Candidate Name:", self.name)
        print("Date of Birth:", self.dob)
        print("Contact Number:", self.contact)
        print("Email:", self.email)


class Education(PersonalInfo):

    def __init__(self, name, dob, contact, email, degree, university, year, cgpa):
        PersonalInfo.__init__(self, name, dob, contact, email)
        self.degree = degree
        self.university = university
        self.year = year
        self.cgpa = cgpa

    def display_education(self):
        print("Degree:", self.degree)
        print("University:", self.university)
        print("Year of Graduation:", self.year)
        print("CGPA:", self.cgpa)


class Experience(Education):

    def __init__(self, name, dob, contact, email, degree, university, year, cgpa,
                 company, role, years_exp, skills):
        Education.__init__(self, name, dob, contact, email, degree, university, year, cgpa)
        self.company = company
        self.role = role
        self.years_exp = years_exp
        self.skills = skills

    def display_experience(self):
        print("Company Name:", self.company)
        print("Job Role:", self.role)
        print("Years of Experience:", self.years_exp)
        print("Skills:", self.skills)


class CandidateProfile(Experience):

    def display_complete_profile(self):

        print("\n----- Candidate Profile -----")

        self.display_personal()
        self.display_education()
        self.display_experience()

        if self.years_exp > 5:
            print("Eligibility: Eligible for Senior Role")
        else:
            print("Eligibility: Eligible for Junior Role")


# Creating two candidates

c1 = CandidateProfile(
    "Arjun",
    "15-03-1998",
    "9876543210",
    "arjun@email.com",
    "B.Tech",
    "JNTU Hyderabad",
    2020,
    8.5,
    "Infosys",
    "Software Engineer",
    6,
    "Python, Java, SQL"
)

c2 = CandidateProfile(
    "Sneha",
    "10-08-2001",
    "9123456780",
    "sneha@email.com",
    "B.Tech",
    "Osmania University",
    2023,
    8.9,
    "TCS",
    "Junior Developer",
    2,
    "Python, HTML, CSS"
)

c1.display_complete_profile()
c2.display_complete_profile()
