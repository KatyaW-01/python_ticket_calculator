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