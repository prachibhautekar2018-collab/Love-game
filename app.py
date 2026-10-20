import time

print("💖 WELCOME TO THE LOVE GAME 💖")
print("-" * 35)

name = input("First, tell me your beautiful name: ")

print("\nHey", name, "🥰❤️")
time.sleep(1)

print("\nI have some special questions for you... 💌")

feeling = input("\nDo you believe in love? (yes/no): ").lower()

if feeling == "yes":
    print("Awww! Then maybe you will understand my heart. 💕")
else:
    print("Maybe one day someone will change your mind. 🌹")

crush = input("\nIs there someone special in your life? (yes/no): ").lower()

if crush == "yes":
    print("Ohhh! Someone is already living in your heart! 👀❤️")
else:
    print("Interesting... Maybe someone is waiting for you! 😉")

print("\nLet me tell you a little secret... 🤫")
time.sleep(2)

print("\n💌 Dear", name, "💌")
print("Every time I talk to you, I feel happy.")
print("Your smile makes my day better.")
print("And honestly, I have started liking you. 🥹❤️")

print("\nNow comes the most important question... 💍")
answer = input("Will you give ME a chance? (yes/no/maybe): ").lower()

if answer == "yes":
    print("\n😍 OMGGGG!!")
    print("You just made my day, " + name + "! ❤️")
    print("Let's write a beautiful story together. 💑")

elif answer == "maybe":
    print("\nA little hope is enough for now. 🥹💕")
    print("Take your time. No pressure! 🌷")

else:
    print("\nIt's okay, " + name + ". ❤️")
    print("Your feelings matter, and I respect your answer. 🌹")

print("\n💖 END OF THE LOVE GAME 💖")
