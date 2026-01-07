from get_name import *
from validate_age import *
from survey import *
print("="*35)
print("Welcome to voting eligibility check. It's nothing to be scared of.")
print("="*35)
print("\n")

user_name = get_name()
print(f"Hi, {user_name}!\n")


age = int(input("Enter your age here: "))
validate_age(age)

survey_flag = input("Would you like to participate in our survey? (Yes/No): ")

if survey_flag == "Yes":
    survey()
elif survey_flag == "No":
    print("Thank you anways!")
    
print("\nThank you! Please visit us again soon. \n\n")