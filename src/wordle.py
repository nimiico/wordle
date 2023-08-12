import random

from src.utils import print_error, print_success, print_warning

random.seed(42)


class wordle:
    def __init__(self, file_path: str, word_len: int=5, limit: int=10000):
        self.word_len = word_len
        self.words = self.generate_word_ferequency(file_path, word_len, limit)

    def generate_word_ferequency(self, file_path, word_len: int, limit: int):
    #Build Data
      words_freq = []

      with open (file_path) as f:
          for line in f:
              word, frequency = line.split(', ')
              frequency = int(frequency)
              words_freq.append((word, frequency))

      # Sort Data
      words = sorted(words_freq, key=lambda w_freq: w_freq[1], reverse=True)

      # Limit Data
      words = words[:limit]

      #Drop Frequency Data
      words = [w_freq[0] for w_freq in words_freq]

      # Filter Data
      words = list(filter(lambda w: len(w) == word_len, words))
      return words

    def run(self, ):
      word = random.choice(self.words)
      word = word.upper()

      # Start Game
      num_try = 6
      success = False

      while num_try:
          guess_word = input(f'\nEnter a {self.word_len} letter word (or q to exit): ')
          if guess_word == 'q':
              break
          guess_word = guess_word.upper()

          #Word Length
          if len(guess_word) != 5:
              print(f'word must have {self.word_len} letters. you entered {len(guess_word)}!')
              continue

          # Check valid word
          if guess_word.lower() not in self.words:
              print_warning('word is not valid!')
              continue

          # Check valid, invalid position, invalid characters
          for w_letter, g_letter in zip(word, guess_word):
              if w_letter == g_letter:
                  print_success(f' {g_letter} ', end='')
                  print(' ', end='')
              elif g_letter in word:
                  print_warning(f' {g_letter} ', end='')
                  print(' ', end='')
              else:
                  print_error(f' {g_letter} ', end='')
                  print(' ', end='')

          # Check success
          if word == guess_word :
              print()
              print_success('\n Congratulations ')
              success = True
              break
          num_try -= 1

      if not success:
          print_warning('Game Over')
