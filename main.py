
from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art
print(art.logo) 

bids = {}
more_members=False
def highest_bidder(record):
  highest_bid = 0
  winner = ""
  for bidder in record:
     
     amount = record[bidder]
     if amount>highest_bid:
       winner=bidder
       highest_bid=amount
  print(f"the winner is {winner} with a bid of ${highest_bid}")


      
while not more_members:
  name=input("Whats your name? ")
  bid=int(input("Whats your bid? "))
  bids[name]=bid
  choice=input("Are there more members? ")
  if choice== "yes":
    clear()
  
  elif choice =="no":
    more_members=True
    highest_bidder(bids)
  else:
    print("invalid input")
    
    


    

