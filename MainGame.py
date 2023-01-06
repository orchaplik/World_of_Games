import Live
from Games import CurrencyRouletteGame, GuessGame, MemoryGame

name = input('enter your first name: ')
Live.welcome(name)
game = Live.load_game()
diff = int(Live.difficulty())
if int(game) == 1:
    MemoryGame.play(diff)
elif int(game) == 2:
    GuessGame.play(diff)
else:
    CurrencyRouletteGame.play(diff)
