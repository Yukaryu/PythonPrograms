import random

from replit import clear

from art import logo, vs
from game_data import data

score = 0
keep_playing = True
print(logo)


#get a random account
def play_game():

  def get_random_account():
    x = random.randint(0, len(data) - 1)
    account_data = data[x]
    return account_data

  A = get_random_account()
  B = get_random_account()

  while keep_playing:
    A = B
    B = get_random_account()
    while A == B:
      B = get_random_account()

    print(f"Compare A: {A['name']}, {A['description']}, from {A['country']} ")
    print(vs)
    print(f"Against B: {B['name']}, {B['description']}, from {B['country']} ")

    def compare():
      AorB = input("Who has more followers? Type 'A' or 'B': ").upper()
      A_followers = A["follower_count"]
      B_followers = B["follower_count"]
      print(A_followers)
      print(B_followers)
      if A_followers > B_followers:
        if AorB == "A":
          return "You Win!!! 💜"
        else:
          return "You Lose!!! 😭"
      elif A_followers < B_followers:
        if AorB == "B":
          return "You Win!!! 💜"
        else:
          return "You Lose!!! 😭"
      else:
        print("The follower count's the same!")
        return "You Win!!! 💜"

    def feedback():
      global score
      if compare() == "You Win!!! 💜":
        score += 1
        clear()
        print(logo)
        return (f"You are right! Current score: {score}")
      else:
        print(f"Sorry, that's wrong. Final score: {score}")
        #my error- forgot the global keyword, created bug, game never-ending, even when wrong.
        global keep_playing
        keep_playing = False
        return ""

    print(feedback())


while keep_playing:
  play_game()

