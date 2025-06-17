def movie_cost(age,movie):
  if age <= 12 and movie == "regular":
    return 8
  elif age <=12 and movie == "premium":
    return 10
  elif age >=13 and age <=59 and movie == "regular":
    return 12
  elif age >=13 and age <=59 and movie == "premium":
    return 15
  elif age >= 60 and movie == "regular":
    return 10
  elif age >= 60 and movie == "premium":
    return 12
  

customer_age = int(input("What is your age? "))
movie_type = input("What movie will you be seeing? Please enter regular or premium. ")

cost = movie_cost(customer_age,movie_type)

print(f"Your ticket will be ${cost}")