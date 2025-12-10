# We're building a program that recommends the user the type of game to play...
def master():
    difficult=input("Difficult or Casual ").title()
    player=input("Multiplayer or Singleplayer ").title()


    if difficult=="Difficult":
        if player=="Multiplayer":
            recommend("PUBG") 
        elif  player=="Singleplayer":
                recommend("Poker")
        
            
        else:
            print("Try something else ")
    elif difficult=="Casual":
        if player=="Multiplayer":
            recommend("Firefox")
        elif player=="Singleplayer":
                recommend("Hooker1")

        else:
            print("Enter a valid level difficulty")
    else:
        print("Enter a valid level difficulty")

     
def recommend(game):
    print(f"You might like {game}")



master()
