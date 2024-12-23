import sys
import random
from colorama import Fore
from collections import Counter


worlist = [
    "about", "above", "after", "again", "agree", "ahead", "along", "aloud",
    "alone", "alter", "among", "angle", "angry", "apart", "apple", "apply",
    "arena", "arise", "around", "arrow", "askew", "atone", "audio", "avoid",
    "awake", "award", "aware", "away", "baker", "basis", "beach", "beard",
    "beast", "below", "bench", "berry", "bible", "birch", "blame", "blank",
    "blast", "bleed", "blend", "bless", "block", "blood", "bloom", "blown",
    "board", "boast", "bolts", "bonds", "bonus", "boost", "bound", "bowed",
    "boxer", "brake", "brass", "bread", "break", "brick", "bride", "brief",
    "brink", "brush", "build", "bunch", "burnt", "burst", "cabin", "cable",
    "caged", "cake", "calm", "canal", "candy", "carat", "cards", "carol",
    "carry", "carve", "cased", "catch", "cause", "chain", "chair", "chant",
    "chaos", "charm", "chase", "cheap", "cheat", "check", "chest", "chief",
    "child", "chill", "china", "choir", "chunk", "claim", "clash", "clean",
    "clear", "click", "climb", "cloak", "close", "cloud", "clown", "coach",
    "coast", "coats", "cocoa", "coins", "colds", "colon", "color", "combo",
    "comic", "comes", "conch", "cook", "coral", "couch", "count", "court",
    "cover", "crack", "craft", "crane", "crash", "crawl", "crazy", "cream",
    "creek", "crowd", "crown", "crude", "cruel", "crumb", "crush", "cries",
    "dance", "datum", "dawn", "deals", "death", "decaf", "decay", "deeds",
    "defer", "delay", "delta", "depth", "dirty", "disco", "dish", "dolls",
    "doubt", "dozen", "draft", "drama", "drawn", "dream", "dress", "drill",
    "drive", "drops", "drunk", "duets", "dummy", "dwarf", "dying", "eager",
    "early", "earth", "easel", "eaten", "edges", "edict", "eight", "elbow",
    "elect", "elite", "empty", "enemy", "enjoy", "enter", "epoch", "equal",
    "error", "essay", "evils", "exact", "exile", "exist", "extra", "faces",
    "facts", "faint", "fairy", "faith", "false", "fault", "favor", "fears",
    "fewer", "fiber", "field", "fight", "files", "films", "final", "first",
    "fish", "fixed", "flame", "flash", "flask", "fleet", "flesh", "flight",
    "flock", "floor", "flour", "flown", "focus", "folds", "fonts", "force",
    "forge", "forms", "found", "frame", "fraud", "fresh", "front", "fruit",
    "fuels", "funds", "funny", "gains", "gauge", "gazed", "gears", "ghost",
    "giant", "gifts", "girls", "given", "glade", "glass", "globe", "glory",
    "glove", "goals", "going", "grace", "grade", "grain", "grant", "grass",
    "grave", "great", "greek", "green", "greet", "grief", "gross", "group",
    "grown", "guard", "guess", "guest", "guide", "guilt", "habits", "hairs",
    "hands", "happy", "harms", "haunt", "havoc", "heard", "heart", "heavy",
    "hedge", "hello", "helps", "hence", "hero", "hides", "hills", "hints",
    "holds", "holes", "homes", "honor", "hosts", "house", "human", "humor",
    "hurts", "icons", "ideas", "ideal", "image", "inbox", "index", "inert",
    "inner", "input", "insist", "issue", "items", "ivory", "jacks", "jeans",
    "jewel", "joins", "jokes", "judge", "juice", "jumps", "keeps", "kicks",
    "kills", "kinds", "kings", "knife", "knock", "known", "labor", "lacks",
    "lakes", "lamps", "lands", "lanes", "large", "laser", "lasts", "laugh",
    "launch", "layer", "leads", "learn", "lease", "leave", "legal", "lemon",
    "level", "light", "limit", "lines", "links", "lions", "liquid", "lists",
    "loads", "loans", "lobby", "local", "locks", "lodge", "logic", "looks",
    "loose", "loved", "lover", "lower", "loyal", "lucky", "lunch", "lungs",
    "magic", "major", "maker", "makes", "males", "march", "marks", "masks",
    "match", "mates", "maths", "mayor", "means", "meats", "media", "medal",
    "meet", "mercy", "merit", "metal", "meter", "might", "minds", "minor",
    "miss", "model", "modem", "moist", "money", "month", "moral", "motor",
    "mount", "mouse", "mouth", "moves", "music", "nails", "named", "nasty",
    "naval", "needs", "nerve", "never", "niche", "night", "noise", "norms",
]
word = random.choice(worlist).lower()
origlis = list(word)
name = input(Fore.BLUE + "What is your name: ")
score = 100
guesses = 0
print(
    Fore.BLUE + "Welcome to Wordle Unlimited v1.3, " + name +
    "! To play, enter your guess below (a 5-letter word with no spaces) and we will tell you how close you are to guessing the word with the colors green, yellow, and red. Green means the letter is in the word, and in the correct place, yellow means the letter is in the word but not in the corect place, and red means the letter is not in the word altogether. Remember, you only get 6 attempts! Have Fun!\n")
counter = []
for i in word:
    if i not in counter:
        counter.append(i)
if len(counter) == 5:
    print(Fore.MAGENTA + "There are 5 unique letters in the word.")
else:
    print(Fore.MAGENTA + "There are some repeated characters in the word.")
guess = input(Fore.BLUE + "Enter your guess #1: ")
if len(guess) != 5:
    print(Fore.BLUE + "Please enter a 5 character word")
    guess = input(Fore.BLUE + "Enter your guess #1: ")
if len(guess) != 5:
    print(Fore.BLUE + "Please enter a 5 character word")
    guess = input(Fore.BLUE + "Enter your guess #1: ")
if len(guess) != 5:
    print(Fore.BLUE + "Please enter a 5 character word")
    guess = input(Fore.BLUE + "Enter your guess #1: ")

guess_list = list(guess.lower())
origlis_count = dict(Counter(origlis))
result = [None, None, None, None, None]

if guess_list[0] == origlis[0]:
    result[0] = Fore.GREEN + guess_list[0]
    origlis_count[guess_list[0]] -= 1
else:
    if guess_list[0] in origlis and origlis_count[guess_list[0]] > 0:
        result[0] = Fore.YELLOW + guess_list[0]
        origlis_count[guess_list[0]] -= 1
    else:
        result[0] = Fore.RED + guess_list[0]

if guess_list[1] == origlis[1]:
    result[1] = Fore.GREEN + guess_list[1]
    origlis_count[guess_list[1]] -= 1
else:
    if guess_list[1] in origlis and origlis_count[guess_list[1]] > 0:
        result[1] = Fore.YELLOW + guess_list[1]
        origlis_count[guess_list[1]] -= 1
    else:
        result[1] = Fore.RED + guess_list[1]

if guess_list[2] == origlis[2]:
    result[2] = Fore.GREEN + guess_list[2]
    origlis_count[guess_list[2]] -= 1
else:
    if guess_list[2] in origlis and origlis_count[guess_list[2]] > 0:
        result[2] = Fore.YELLOW + guess_list[2]
        origlis_count[guess_list[2]] -= 1
    else:
        result[2] = Fore.RED + guess_list[2]

if guess_list[3] == origlis[3]:
    result[3] = Fore.GREEN + guess_list[3]
    origlis_count[guess_list[3]] -= 1
else:
    if guess_list[3] in origlis and origlis_count[guess_list[3]] > 0:
        result[3] = Fore.YELLOW + guess_list[3]
        origlis_count[guess_list[3]] -= 1
    else:
        result[3] = Fore.RED + guess_list[3]

if guess_list[4] == origlis[4]:
    result[4] = Fore.GREEN + guess_list[4]
    origlis_count[guess_list[4]] -= 1
else:
    if guess_list[4] in origlis and origlis_count[guess_list[4]] > 0:
        result[4] = Fore.YELLOW + guess_list[4]
        origlis_count[guess_list[4]] -= 1
    else:
        result[4] = Fore.RED + guess_list[4]

result_str = " ".join(result)
print(result_str)

guesses += 1
if word.lower() == guess:
    print(Fore.BLUE + f"Nice job! You guessed the word in {guesses} tries!")
    print(Fore.BLUE + "Your score was:", int(score))
    sys.exit()
score -= 10

guess = input(Fore.BLUE + "Enter your guess #2: ")
if len(guess) != 5:
    print(Fore.BLUE + "Please enter a 5 character word")
    guess = input(Fore.BLUE + "Enter your guess #2: ")
if len(guess) != 5:
    print(Fore.BLUE + "Please enter a 5 character word")
    guess = input(Fore.BLUE + "Enter your guess #2: ")
if len(guess) != 5:
    print(Fore.BLUE + "Please enter a 5 character word")
    guess = input(Fore.BLUE + "Enter your guess #2: ")

guess_list = list(guess.lower())
origlis_count = dict(Counter(origlis))
result = [None, None, None, None, None]

if guess_list[0] == origlis[0]:
    result[0] = Fore.GREEN + guess_list[0]
    origlis_count[guess_list[0]] -= 1
else:
    if guess_list[0] in origlis and origlis_count[guess_list[0]] > 0:
        result[0] = Fore.YELLOW + guess_list[0]
        origlis_count[guess_list[0]] -= 1
    else:
        result[0] = Fore.RED + guess_list[0]

if guess_list[1] == origlis[1]:
    result[1] = Fore.GREEN + guess_list[1]
    origlis_count[guess_list[1]] -= 1
else:
    if guess_list[1] in origlis and origlis_count[guess_list[1]] > 0:
        result[1] = Fore.YELLOW + guess_list[1]
        origlis_count[guess_list[1]] -= 1
    else:
        result[1] = Fore.RED + guess_list[1]

if guess_list[2] == origlis[2]:
    result[2] = Fore.GREEN + guess_list[2]
    origlis_count[guess_list[2]] -= 1
else:
    if guess_list[2] in origlis and origlis_count[guess_list[2]] > 0:
        result[2] = Fore.YELLOW + guess_list[2]
        origlis_count[guess_list[2]] -= 1
    else:
        result[2] = Fore.RED + guess_list[2]

if guess_list[3] == origlis[3]:
    result[3] = Fore.GREEN + guess_list[3]
    origlis_count[guess_list[3]] -= 1
else:
    if guess_list[3] in origlis and origlis_count[guess_list[3]] > 0:
        result[3] = Fore.YELLOW + guess_list[3]
        origlis_count[guess_list[3]] -= 1
    else:
        result[3] = Fore.RED + guess_list[3]

if guess_list[4] == origlis[4]:
    result[4] = Fore.GREEN + guess_list[4]
    origlis_count[guess_list[4]] -= 1
else:
    if guess_list[4] in origlis and origlis_count[guess_list[4]] > 0:
        result[4] = Fore.YELLOW + guess_list[4]
        origlis_count[guess_list[4]] -= 1
    else:
        result[4] = Fore.RED + guess_list[4]

result_str = " ".join(result)
print(result_str)

guesses += 1
if word.lower() == guess:
    print(Fore.BLUE + f"Nice job! You guessed the word in {guesses} tries!")
    print(Fore.BLUE + "Your score was:", int(score))
    sys.exit()
score -= 10

guess = input(Fore.BLUE + "Enter your guess #3: ")
if len(guess) != 5:
    print(Fore.BLUE + "Please enter a 5 character word")
    guess = input(Fore.BLUE + "Enter your guess #3: ")
if len(guess) != 5:
    print(Fore.BLUE + "Please enter a 5 character word")
    guess = input(Fore.BLUE + "Enter your guess #3: ")
if len(guess) != 5:
    print(Fore.BLUE + "Please enter a 5 character word")
    guess = input(Fore.BLUE + "Enter your guess #3: ")

guess_list = list(guess.lower())
origlis_count = dict(Counter(origlis))
result = [None, None, None, None, None]

if guess_list[0] == origlis[0]:
    result[0] = Fore.GREEN + guess_list[0]
    origlis_count[guess_list[0]] -= 1
else:
    if guess_list[0] in origlis and origlis_count[guess_list[0]] > 0:
        result[0] = Fore.YELLOW + guess_list[0]
        origlis_count[guess_list[0]] -= 1
    else:
        result[0] = Fore.RED + guess_list[0]

if guess_list[1] == origlis[1]:
    result[1] = Fore.GREEN + guess_list[1]
    origlis_count[guess_list[1]] -= 1
else:
    if guess_list[1] in origlis and origlis_count[guess_list[1]] > 0:
        result[1] = Fore.YELLOW + guess_list[1]
        origlis_count[guess_list[1]] -= 1
    else:
        result[1] = Fore.RED + guess_list[1]

if guess_list[2] == origlis[2]:
    result[2] = Fore.GREEN + guess_list[2]
    origlis_count[guess_list[2]] -= 1
else:
    if guess_list[2] in origlis and origlis_count[guess_list[2]] > 0:
        result[2] = Fore.YELLOW + guess_list[2]
        origlis_count[guess_list[2]] -= 1
    else:
        result[2] = Fore.RED + guess_list[2]

if guess_list[3] == origlis[3]:
    result[3] = Fore.GREEN + guess_list[3]
    origlis_count[guess_list[3]] -= 1
else:
    if guess_list[3] in origlis and origlis_count[guess_list[3]] > 0:
        result[3] = Fore.YELLOW + guess_list[3]
        origlis_count[guess_list[3]] -= 1
    else:
        result[3] = Fore.RED + guess_list[3]

if guess_list[4] == origlis[4]:
    result[4] = Fore.GREEN + guess_list[4]
    origlis_count[guess_list[4]] -= 1
else:
    if guess_list[4] in origlis and origlis_count[guess_list[4]] > 0:
        result[4] = Fore.YELLOW + guess_list[4]
        origlis_count[guess_list[4]] -= 1
    else:
        result[4] = Fore.RED + guess_list[4]

result_str = " ".join(result)
print(result_str)

guesses += 1
if word.lower() == guess:
    print(Fore.BLUE + f"Nice job! You guessed the word in {guesses} tries!")
    print(Fore.BLUE + "Your score was:", int(score))
    sys.exit()
score -= 10

guess = input(Fore.BLUE + "Enter your guess #4: ")
if len(guess) != 5:
    print(Fore.BLUE + "Please enter a 5 character word")
    guess = input(Fore.BLUE + "Enter your guess #4: ")
if len(guess) != 5:
    print(Fore.BLUE + "Please enter a 5 character word")
    guess = input(Fore.BLUE + "Enter your guess #4: ")
if len(guess) != 5:
    print(Fore.BLUE + "Please enter a 5 character word")
    guess = input(Fore.BLUE + "Enter your guess #4: ")

guess_list = list(guess.lower())
origlis_count = dict(Counter(origlis))
result = [None, None, None, None, None]

if guess_list[0] == origlis[0]:
    result[0] = Fore.GREEN + guess_list[0]
    origlis_count[guess_list[0]] -= 1
else:
    if guess_list[0] in origlis and origlis_count[guess_list[0]] > 0:
        result[0] = Fore.YELLOW + guess_list[0]
        origlis_count[guess_list[0]] -= 1
    else:
        result[0] = Fore.RED + guess_list[0]

if guess_list[1] == origlis[1]:
    result[1] = Fore.GREEN + guess_list[1]
    origlis_count[guess_list[1]] -= 1
else:
    if guess_list[1] in origlis and origlis_count[guess_list[1]] > 0:
        result[1] = Fore.YELLOW + guess_list[1]
        origlis_count[guess_list[1]] -= 1
    else:
        result[1] = Fore.RED + guess_list[1]

if guess_list[2] == origlis[2]:
    result[2] = Fore.GREEN + guess_list[2]
    origlis_count[guess_list[2]] -= 1
else:
    if guess_list[2] in origlis and origlis_count[guess_list[2]] > 0:
        result[2] = Fore.YELLOW + guess_list[2]
        origlis_count[guess_list[2]] -= 1
    else:
        result[2] = Fore.RED + guess_list[2]

if guess_list[3] == origlis[3]:
    result[3] = Fore.GREEN + guess_list[3]
    origlis_count[guess_list[3]] -= 1
else:
    if guess_list[3] in origlis and origlis_count[guess_list[3]] > 0:
        result[3] = Fore.YELLOW + guess_list[3]
        origlis_count[guess_list[3]] -= 1
    else:
        result[3] = Fore.RED + guess_list[3]

if guess_list[4] == origlis[4]:
    result[4] = Fore.GREEN + guess_list[4]
    origlis_count[guess_list[4]] -= 1
else:
    if guess_list[4] in origlis and origlis_count[guess_list[4]] > 0:
        result[4] = Fore.YELLOW + guess_list[4]
        origlis_count[guess_list[4]] -= 1
    else:
        result[4] = Fore.RED + guess_list[4]

result_str = " ".join(result)
print(result_str)

guesses += 1
if word.lower() == guess:
    print(Fore.BLUE + f"Nice job! You guessed the word in {guesses} tries!")
    print(Fore.BLUE + "Your score was:", int(score))
    sys.exit()
score -= 10

guess = input(Fore.BLUE + "Enter your guess #5: ")
if len(guess) != 5:
    print(Fore.BLUE + "Please enter a 5 character word")
    guess = input(Fore.BLUE + "Enter your guess #5: ")
if len(guess) != 5:
    print(Fore.BLUE + "Please enter a 5 character word")
    guess = input(Fore.BLUE + "Enter your guess #5: ")
if len(guess) != 5:
    print(Fore.BLUE + "Please enter a 5 character word")
    guess = input(Fore.BLUE + "Enter your guess #5: ")

guess_list = list(guess.lower())
origlis_count = dict(Counter(origlis))
result = [None, None, None, None, None]

if guess_list[0] == origlis[0]:
    result[0] = Fore.GREEN + guess_list[0]
    origlis_count[guess_list[0]] -= 1
else:
    if guess_list[0] in origlis and origlis_count[guess_list[0]] > 0:
        result[0] = Fore.YELLOW + guess_list[0]
        origlis_count[guess_list[0]] -= 1
    else:
        result[0] = Fore.RED + guess_list[0]

if guess_list[1] == origlis[1]:
    result[1] = Fore.GREEN + guess_list[1]
    origlis_count[guess_list[1]] -= 1
else:
    if guess_list[1] in origlis and origlis_count[guess_list[1]] > 0:
        result[1] = Fore.YELLOW + guess_list[1]
        origlis_count[guess_list[1]] -= 1
    else:
        result[1] = Fore.RED + guess_list[1]

if guess_list[2] == origlis[2]:
    result[2] = Fore.GREEN + guess_list[2]
    origlis_count[guess_list[2]] -= 1
else:
    if guess_list[2] in origlis and origlis_count[guess_list[2]] > 0:
        result[2] = Fore.YELLOW + guess_list[2]
        origlis_count[guess_list[2]] -= 1
    else:
        result[2] = Fore.RED + guess_list[2]

if guess_list[3] == origlis[3]:
    result[3] = Fore.GREEN + guess_list[3]
    origlis_count[guess_list[3]] -= 1
else:
    if guess_list[3] in origlis and origlis_count[guess_list[3]] > 0:
        result[3] = Fore.YELLOW + guess_list[3]
        origlis_count[guess_list[3]] -= 1
    else:
        result[3] = Fore.RED + guess_list[3]

if guess_list[4] == origlis[4]:
    result[4] = Fore.GREEN + guess_list[4]
    origlis_count[guess_list[4]] -= 1
else:
    if guess_list[4] in origlis and origlis_count[guess_list[4]] > 0:
        result[4] = Fore.YELLOW + guess_list[4]
        origlis_count[guess_list[4]] -= 1
    else:
        result[4] = Fore.RED + guess_list[4]

result_str = " ".join(result)
print(result_str)

guesses += 1
if word.lower() == guess:
    print(Fore.BLUE + f"Nice job! You guessed the word in {guesses} tries!")
    print(Fore.BLUE + "Your score was:", int(score))
    sys.exit()
score -= 10

# Attempt 6
guess = input(Fore.BLUE + "Enter your guess #6: ")
if len(guess) != 5:
    print(Fore.BLUE + "Please enter a 5 character word")
    guess = input(Fore.BLUE + "Enter your guess #6: ")
if len(guess) != 5:
    print(Fore.BLUE + "Please enter a 5 character word")
    guess = input(Fore.BLUE + "Enter your guess #6: ")
if len(guess) != 5:
    print(Fore.BLUE + "Please enter a 5 character word")
    guess = input(Fore.BLUE + "Enter your guess #6: ")

guess_list = list(guess.lower())
origlis_count = dict(Counter(origlis))
result = [None, None, None, None, None]

if guess_list[0] == origlis[0]:
    result[0] = Fore.GREEN + guess_list[0]
    origlis_count[guess_list[0]] -= 1
else:
    if guess_list[0] in origlis and origlis_count[guess_list[0]] > 0:
        result[0] = Fore.YELLOW + guess_list[0]
        origlis_count[guess_list[0]] -= 1
    else:
        result[0] = Fore.RED + guess_list[0]

if guess_list[1] == origlis[1]:
    result[1] = Fore.GREEN + guess_list[1]
    origlis_count[guess_list[1]] -= 1
else:
    if guess_list[1] in origlis and origlis_count[guess_list[1]] > 0:
        result[1] = Fore.YELLOW + guess_list[1]
        origlis_count[guess_list[1]] -= 1
    else:
        result[1] = Fore.RED + guess_list[1]

if guess_list[2] == origlis[2]:
    result[2] = Fore.GREEN + guess_list[2]
    origlis_count[guess_list[2]] -= 1
else:
    if guess_list[2] in origlis and origlis_count[guess_list[2]] > 0:
        result[2] = Fore.YELLOW + guess_list[2]
        origlis_count[guess_list[2]] -= 1
    else:
        result[2] = Fore.RED + guess_list[2]

if guess_list[3] == origlis[3]:
    result[3] = Fore.GREEN + guess_list[3]
    origlis_count[guess_list[3]] -= 1
else:
    if guess_list[3] in origlis and origlis_count[guess_list[3]] > 0:
        result[3] = Fore.YELLOW + guess_list[3]
        origlis_count[guess_list[3]] -= 1
    else:
        result[3] = Fore.RED + guess_list[3]

if guess_list[4] == origlis[4]:
    result[4] = Fore.GREEN + guess_list[4]
    origlis_count[guess_list[4]] -= 1
else:
    if guess_list[4] in origlis and origlis_count[guess_list[4]] > 0:
        result[4] = Fore.YELLOW + guess_list[4]
        origlis_count[guess_list[4]] -= 1
    else:
        result[4] = Fore.RED + guess_list[4]

result_str = " ".join(result)
print(result_str)

guesses += 1
if word.lower() == guess:
    print(Fore.BLUE + f"Nice job! You guessed the word in {guesses} tries!")
    print(Fore.BLUE + "Your score was:", int(score))
    sys.exit()
score -= 10

print(Fore.BLUE + "Sorry, you've used all your attempts! The correct word was:", word)

sys.exit()