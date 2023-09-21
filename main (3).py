class Player:
    def play(self):
        print("The Player is Playing Cricket")

class Batsman(Player):
    def play(self):
        print("The Batsman is Batting")

class Bowler(Player):
    def play(self):
        print("The Bowler is Bowling")

player=Player()
batsman=Batsman()
bowler=Bowler()
player.play()
batsman.play()
bowler.play()