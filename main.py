

from art import logo
print(logo)
print("Welcome to the secret auction program.")

end_of_bidders = False
bidders_dict = {}

while end_of_bidders == False:
  name = input("What is your name?\n")
  bid = int(input("What is your bid?\n$"))
  more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")

  bidders = {
    name: bid,
  }
  bidders_dict.update(bidders)

  if more_bidders == 'no':
    end_of_bidders = True
  else:
    print("\n" * 20)

winner_bid = 0
winner_name = ""
for name in bidders_dict:
  if end_of_bidders == True:
    if bidders_dict[name] > winner_bid:
      winner_bid = bidders_dict[name]
      winner_name = name
print("\n" * 20)
print(f"The winner is {winner_name} with a bid of ${winner_bid}.")