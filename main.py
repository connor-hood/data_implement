# tuple for month
# set for birthday locations
# dictionary for contest winner
from sweepstakes import Sweepstakes


months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December")
print(months[2])

birthday_location = {"Honolulu", "Omaha", "Branson"}
birthday_location.add("Denver")
birthday_location.add("Portland")
birthday_location.add("New York")

for value in birthday_location:
    print(value)

sweepstakes = Sweepstakes()
sweepstakes.enter_contest("Bob Barker")
sweepstakes.enter_contest("Tracy Sanne")
sweepstakes.enter_contest("Connor Hood")
sweepstakes.enter_contest("JJ Vega")
sweepstakes.draw_winner()

myFam = [{
    "firstName": "Katie",
    "lastName": "Jaapar",
    "relationship": "Mother"
}, {
    "firstName": "Aaron",
    "lastName": "Jaapar",
    "relationship": "Brother"
}, ]
print(myFam)
