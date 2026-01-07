def survey():
    val = int(input("Please rate your experience (1-5): "))
    if val > 0 and val >= 5:
        print("Thank you for your feedback")
    return
