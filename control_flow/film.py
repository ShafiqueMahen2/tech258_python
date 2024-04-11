# Film ratings are "Universal", "PG", "12", "12A", "15", "18"
film_rating = "12A"

if film_rating == "Universal":
    print("All age groups can watch this film!")
elif film_rating == "PG":
    print("General viewing, but some scenes may be unsuitable for young children.")
elif film_rating == "12":
    print("This film is suitable for 12 year olds and over.")
elif film_rating == "12A":
    print("This film is suitable for 12 year olds and over, fine for those under 12 years old if an adult is present.")
elif film_rating == "15":
    print("This film is suitable for 15 year olds and over.")
elif film_rating == "18":
    print("This film is suitable for 18 year olds and over.")
else:
    print("This is not a correct rating, please use Universal, PG, 12, 12A, 15, 18.")
