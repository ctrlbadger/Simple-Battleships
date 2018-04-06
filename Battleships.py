def DrawGrid(Board):
    print("  "+" ".join([str(chr(Char+65)) for Char in range(len(Board[0]))]))
    for LineIndex in range(len(Board)):
        print(str(LineIndex) + " " +" ".join(Board[LineIndex]))

def InterpretInput(Coordinate):
    Coordinate = Coordinate.replace(' ', '')
    input(Coordinate)
    try:
        return [int(Coordinate[1]), ord(Coordinate[0].upper())-65]
    except:
        return [int(Coordinate[0]), ord(Coordinate[1].upper())-65]

class PlayerBoards:
    Ships = []
    def __init__(self, Boardsize):
        self.PrivateBattleShips = [['.' for _ in range(0, Boardsize)] for _ in range(0, Boardsize)]
        self.GuessBattleShips = [['.' for _ in range(0, Boardsize)] for _ in range(0, Boardsize)]
    def MakeGuess(self, Guess, EnemyBoard):
        if EnemyBoard[Guess[0]][Guess[1]] == 'X':
            self.GuessBattleShips[Guess[0]][Guess[1]] = 'H'
            EnemyBoard[Guess[0]][Guess[1]] = 'H'
            return True
        else:
            self.GuessBattleShips[Guess[0]][Guess[1]] = 'M'
            EnemyBoard[Guess[0]][Guess[1]] = 'M'
            return False
    def AddShip(self, CurrentShip):
        CurrentShip.DrawBattleShip(self.PrivateBattleShips)
        self.Battleships = CurrentShip

class Battleship:
    def __init__(self, Name, Size, Coordinate, Vertical):
        self.Name = Name
        self.HasHit = False
        self.Size = Size
        self.Coordinate = Coordinate
        self.Vertical = Vertical
    def DrawBattleShip(self, Board):
        if self.Vertical == True:
            for Index in range(self.Coordinate[0], self.Coordinate[0] + self.Size):
                print(Index)
                Board[Index][self.Coordinate[1]] = 'X'
        else:
            for Index in range(self.Coordinate[1], self.Coordinate[1] + self.Size):
                Board[self.Coordinate[0]][Index] = 'X'
        return

Ships = {'Aircraft Carrier': 5, 'Batleship': 4, 'Submarine': 3, 'Cruiser': 3, 'Destroyer': 2}

class MainLoop():
    def __init__(self, BoardSize):
        self.Players = [PlayerBoards(BoardSize), PlayerBoards(BoardSize)]
        self.InputShips()
        while True:
            for CurrentPlayerIndex in range(len(self.Players)):
                self.PlayersTurn(CurrentPlayerIndex)
                self.GameTurn(CurrentPlayerIndex)
    def PlayersTurn(self, Index):
        print('\n'*50)
        input("It is player " + str(Index) + "'s turn'")

    def InputShips(self):
        for CurrentPlayerIndex in range(len(self.Players)):
            self.PlayersTurn(CurrentPlayerIndex)
            CurrentPlayerShips = []
            for Name, Size in Ships.items():
                DrawGrid(self.Players[CurrentPlayerIndex].PrivateBattleShips)
                print("Where is your", Name, " with a length of", Size)
                ShipCoord = InterpretInput(input(':'))
                print("Across or Down?")
                Vertical = input(':').upper() == "DOWN"
                Ship = Battleship(Name, Size, ShipCoord, Vertical)
                #Ship.DrawBattleship(self.Players[CurrentPlayerIndex].PrivateBattleShips)
                CurrentPlayerShips.append(Ship)
                self.Players[CurrentPlayerIndex].AddShip(Ship)

            self.Players[CurrentPlayerIndex].Battleships = CurrentPlayerShips

    def GameTurn(self, CurrentPlayerIndex):
        print("Enemy Board:")
        DrawGrid(self.Players[CurrentPlayerIndex].GuessBattleShips)
        print("Private Board:")
        DrawGrid(self.Players[CurrentPlayerIndex].PrivateBattleShips)
        print("Where do you want to fire?")
        ShipCoord = InterpretInput(input(':'))
        Hit = self.Players[CurrentPlayerIndex].MakeGuess(ShipCoord, self.Players[(CurrentPlayerIndex + 1) % 2].PrivateBattleShips)
        if Hit:
            print("You hit! Congratulations!")
        else:
            print("You missed! bad luck!")
        input("Press enter to end your turn")
Main = MainLoop(10)
