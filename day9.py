from replit import clear
print("stupid hame")

bids = {}
bidiing = False

hb = 0

def heigest_bifing(bir):
  for i in bir:
    amount = bir[i]
    if amount > hb:
      hb = amount


while not bidiing:
  name = input("what is your name ")
  price = input("whats yout bit ")
  bids[name] = price
  contiune = input("are ther new biddings")
  if contiune == "no":
    bidiing = True
  elif contiune == "yes":
    clear()