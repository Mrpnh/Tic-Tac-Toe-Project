

# Initial Board

board=[str(i+1) for i in range(9)]

# Printing the Board

def printBoard(bo):
   print(" -----------")
   print("|",bo[0],"|",bo[1],"|",bo[2],"|")
   print(" -----------")
   print("|",bo[3],"|",bo[4],"|",bo[5],"|")
   print(" -----------")
   print("|",bo[6],"|",bo[7],"|",bo[8],"|")
   print(" -----------")


# Filling 'X' or 'O' in desired postion by entering the number of that position

def filldetails(bo,player):
    pos=int(input(f"Enter the  position of '{player}' in range of 1-9\n"))
    if bo[pos-1]=='X' or bo[pos-1]=='O':
        print("Already filled!")
        filldetails(bo,player)
    else:
        bo[pos-1]=player


# Checking if a player Won or not

def isWin(bo):
      if bo[0]==bo[1]==bo[2] or bo[3]==bo[4]==bo[5] or bo[6]==bo[7]==bo[8]:
          return True
      if bo[0]==bo[3]==bo[6] or bo[1]==bo[4]==bo[7] or bo[2]==bo[5]==bo[8]:
          return True
      if bo[0]==bo[4]==bo[8] or bo[2]==bo[4]==bo[6]:
          return True
      return False

# Checking Who won the game

def whoWon(count):
    if count%2==0:
        print("\n'0' Won the Game")
    else:
        print("'X' Won the Game")
    

# Main function

if __name__ == "__main__":
    printBoard(board)
    count=0
    for i in range(9):
        if isWin(board):
            whoWon(count)
            break
        if i%2==0:
            count+=1
            filldetails(board,'X')
        else:
            count+=1
            filldetails(board,'O')
              
        printBoard(board)
    else:
        if isWin(board):
            whoWon(count)
        else:
            print("Game Tied Guys!!")