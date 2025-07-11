import random

print("\n🎯 Welcome to Number Guessing Game!!! 🎯")
print("🔢 You have to guess a number between 1 and 100.")
print("🕹️ You'll have 10 guesses.\nLet's start!\n")

num = random.randint(1, 100)
tries = 0
max_tries = 10

while tries < max_tries:
    try:
        guess = int(input(f"👉 Attempt {tries + 1}: Enter your guess: "))
    except ValueError:
        print("❌ Invalid input! Please enter a number.\n")
        continue

    tries += 1

    if guess == num:
        print("\n🎉 Congo! You Guessed It Right!")
        print(f"✅ You got it in {tries} tries.")
        break
    elif guess > num:
        print("📉 Lower number please.")
    else:
        print("📈 Higher number please.")

    if tries < max_tries:
        print(f"🕒 Guesses left: {max_tries - tries}\n")
    else:
        print("\n💀 Sorry! You've used all your guesses.")
        print(f"🎯 The correct number was: {num}")

print("\n🎮 Game Over.")



