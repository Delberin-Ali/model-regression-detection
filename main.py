from app.classifier import classify_email


def main():
    email = """
    Hello,

    I was charged twice for my subscription
    this month.

    Can you refund the extra payment?

    Thank you.
    """

    result = classify_email(email)

    print("Category:", result.category.value)
    print("Summary:", result.summary)


if __name__ == "__main__":
    main()