"""
Emails
Estimate: 30 mins
Actual: 40 mins
"""


def main():
    email_to_names = {}
    email = input("Email: ")
    while email != "":
        full_name = extract_name(email)
        confirm = input(f"Is your name {full_name}? (y/n)").lower()
        if confirm != "y" and confirm != "":
            full_name = input("Name: ")
        email_to_names[email] = full_name
        email = input("Email: ")
    for email, full_name in email_to_names.items():
        print(f"{full_name} ({email})")


def extract_name(email):
    """This function will extract name"""
    email_address = email.split("@", 1)[0]
    user_name = email_address.split(".", 1)
    join_name = " ".join(user_name)
    full_name = join_name.title()
    return full_name


main()