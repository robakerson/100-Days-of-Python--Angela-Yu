import art
from random import randint
from game_data import data
from replit import clear

#returns one random competitor
def pick_competitor():
  return data[randint(0,49)]

#return true if player's guess had more followers than other competitor
def did_player_win(guess, competitor_a, competitor_b):
  if competitor_a['follower_count'] > competitor_b['follower_count']:
    if guess == 'a':
      return True
    else:
      return False
  if competitor_b['follower_count'] > competitor_a['follower_count']:
    if guess == 'b':
      return True
    else:
      return False

#if fed empty string, returns 2 random competitors.
#if fed legitimate competitor, then one becomes that competitor and two becomes random competitor
def pick_competitors(prev_competitor):
  if not prev_competitor:
    one = pick_competitor()
  else:
    one = prev_competitor
  two = pick_competitor()
  while one == two:
    two = pick_competitor()
  return one, two

#feed all data, print all relavent text, ask for player guess, return True if win and False if lost
def play_round(cur_score, competitor_one, competitor_two):
  if cur_score > 0:
    print(f"You're right! Current score: {cur_score}")
  print(f"Compare A: {competitor_one['name']}, a {competitor_one['description']}, from {competitor_one['country']}.")
  print(art.vs)
  print(f"Against B: {competitor_two['name']}, a {competitor_two['description']}, from {competitor_two['country']}.")
  player_guess = input("Who has more followers? Type 'a' or 'b': ")
  if did_player_win(player_guess, competitor_one, competitor_two):
    return True
  else:
    return False

#controls end game display
def end_game(cur_score):
  clear()
  print(art.logo)
  print(f"Sorry, that's wrong. Final score: {cur_score}")

#var inits
score = 0
game_on = True
#pick 2 random competitors
competitor_one, competitor_two = pick_competitors('')

clear()
print(art.logo)
#execute another play_round as long as player guesses correctly
while play_round(score, competitor_one, competitor_two):
  score += 1
  #competitor one becomes previous competitor 2 if player guessed correctly
  competitor_one, competitor_two = pick_competitors(competitor_two)
  clear()
  print(art.logo)

end_game(score)
