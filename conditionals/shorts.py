# We're building a program that recommends the user the type of game to play...
def master():
    difficult=input("Difficult or Casual ").title()
    if not (difficult=="Difficult" or difficult=="Casual"):
          print("Enter a valid level difficulty")
          return # To say to the user this is the end.

         

    player=input("Multiplayer or Singleplayer ").title()
    if not (player=="Multiplayer" or player=="Singleplayer"):
          print("Enter a valid no. of player")
          return # To say to the user this is the end.

    if difficult=="Difficult"and player=="Multiplayer":
       recommend("Poker")
    elif difficult=="Casual" and player=="Multiplayer":
         recommend("Poly")
    elif difficult=="Casual" and player=="Multiplayer":
         recommend("Potter")
    else:
         recommend("PUBG")
     
def recommend(game):
    print(f"You might like {game}")



master()
