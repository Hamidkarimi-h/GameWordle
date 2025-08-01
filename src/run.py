from src.wordle import Wordle


file_path = r'src\data\words_freq_data.txt'
wordle = Wordle(file_path)
wordle.run()