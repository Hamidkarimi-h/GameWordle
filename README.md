
# Wordle (Python)

## What is Wordle?

Wordle is a word game, which recently got very popular and was added to the New York Times Games website. It is developed by Josh Wardle. You can find the original game [here](https://www.nytimes.com/games/wordle/index.html). However, you can only play it once a day.

Luckily, in this version of Wordle that you are going to be programming, you will be able to play as many times as you want in a day. Moreover, you will be allowed to see which words could potentially be the right answer. What is more, you will be using a bigger data set than the actual Wordle, which basically involves all the 5-letter words in a Scrabble dictionary.

---

## Rules

- The player enters a random 5-letter word.
- If the random word is the word to be guessed, the game is over. The player receives a congratulations message.
- If the random word isn’t the word to be guessed, the player is informed about whether the right letter is at the right place and if some of the letters are in the word but wrongly placed.
- Based on this, the player has 6 tries to guess the word.
- At the end of the 6 attempts, if the player fails to guess the right word, the word is revealed.

---

## TODO

- Read the possible words from the txt file and save them in a list.
- Make sure that the user can enter input exactly 6 times.
- Make sure that regardless of the case, the input is processed correctly.
- Use appropriate data structures for valid characters, invalid positions, and invalid characters.
- Use the random module to make sure the word to be guessed is randomly chosen.
- Cluster the potential words accordingly and reveal them to the player each round.
- In case the player first guesses the right letter at the wrong place, and later on gets the place right, remove that from your valid characters invalid positions.

---

## Tips

- At the very beginning each of the words have a chance of being the word to be guessed.
- A word is invalid when there are invalid letters in it or when there is a valid letter at the wrong place.
- A word is possible when it isn’t invalid and contains the correctly guessed letter at the right place.
- You can initiate a random number by:

```python
from random import randint, seed
seed()
````

---

## Test Example

If the word to be guessed is `BUIST`:

* If you guess first `MILKY`, your cluster of potential words should consist of 1127 words.
* If you then guess `POUND`, the cluster should be reduced to 52 words.
* If you then guess `RATES`, the cluster should contain only 3 words: `['BUIST', 'BUSTI', 'QUIST']`.

---

## How to Run

1. Clone the repository and `cd` into it.

2. Install the requirements by running:

   ```bash
   pip install -r requirements.txt
   ```

3. Add the current directory to your PYTHONPATH:

   On Linux/macOS:

   ```bash
   export PYTHONPATH=$PYTHONPATH:$(pwd)
   ```

   On Windows (PowerShell):

   ```powershell
   $env:PYTHONPATH="$env:PYTHONPATH;$(Get-Location)"
   ```

4. Run the game:

   ```bash
   python src/wordle.py
   ```

---

## Project Structure

```
wordle/
├── src/
|   ├── utills.py
│   ├── wordle.py
│   ├── run.py
│   └── data/
│       └── words_freq_data.txt
├── .gitignore
├── README.md
└── requirements.txt
```

---


