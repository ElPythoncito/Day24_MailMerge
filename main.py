# ----------------------------------------------EL PYTHONCITO XD 🐍🐍🐍🐍
import time
import sys

new_names = []

# Read invited_names.txt
with open("./Input/Names/invited_names.txt") as data:
    names = data.readlines()

# Remove \n of names
for name in names:
    new_names.append(name.replace("\n", ""))

# Read starting_letter.txt
with open("./Input/Letters/starting_letter.txt") as data:
    original_letter = data.read()

# Animation
print("Writing letters ", end="")
for i in range(5):
    print("✉️", end="")
    sys.stdout.flush()
    time.sleep(0.5)
print(f"\nYour letters are ready ✉️✉️✉️!!!")

for name in new_names:
    with open(f"./Output/ReadyToSend/letter_for_{name}", mode="w") as data:
        letter = original_letter.replace("[name]", f"{name}")
        data.write(letter)
