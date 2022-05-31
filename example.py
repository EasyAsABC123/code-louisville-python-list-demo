def load_students():
    students = [
        {
            "fname": "Adrienne",
            "lname": "Adams"
        },
        {
            "fname": "Doug",
            "lname": "Wiley"
        },
        {
            "fname": "Emily",
            "lname": "Coleman"
        },
        {
            "fname": "Grace",
            "lname": "Ensign"
        },
        {
            "fname": "Katie",
            "lname": "Cook"
        },
        {
            "fname": "Kimberly",
            "lname": "B"
        },
        {
            "fname": "Mariah",
            "lname": "Corso"
        }
    ]

    return students


def standup(students):
    for student in students:
        print("Hello " + student["fname"])
        input("What did you work on last week?")
        input("What are you working on this week?")
        input("What do you need help with?")
        print(f"Thanks so much {student['lname']}")


def main():
    students = load_students()
    standup(students)


if __name__ == "__main__":
    main()
