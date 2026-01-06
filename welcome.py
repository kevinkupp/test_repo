from get_name import *
from validate_age import *

print("="*35)
print("Welcome to voting eligibility check. It's nothing to be scared of.")
print("="*35)
print("\n")

user_name = get_name()
print(f"Hi, {user_name}!\n")


age = int(input("Enter your age here: "))
validate_age(age)

