def is_valid_email(email: str) -> bool:
    if not isinstance(email, str):
        return False

    email = email.strip()
    if not email or " " in email:
        return False

    if not email.endswith(".com"):
        return False

    if "@" not in email:
        return False

    local, sep, domain = email.partition("@")
    if not sep or not local or not domain:
        return False

    return True


def main() -> None:
    email = input("Enter an email: ")
    print("Valid" if is_valid_email(email) else "Invalid")
    input("Press Enter to exit...")


if __name__ == "__main__":
    main()
