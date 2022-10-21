import Live
import GuessGame
import MemoryGame
import CurrencyRouletteGame

name = input('enter your first name: ')
Live.welcome(name)
game = Live.load_game()
diff = Live.difficulty()
if int(game) == 1:
    MemoryGame.play(diff)
elif int(game) == 2:
    GuessGame.play(diff)
else:
    CurrencyRouletteGame.play(diff)
