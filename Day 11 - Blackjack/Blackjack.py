cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
from art import logo
import random

player_cards = []
dealer_cards = []

def randomcard():
  return cards[random.randint(0,12)]

def deal_starting_cards():
  player_cards.append(randomcard())
  player_cards.append(randomcard())
  dealer_cards.append(randomcard())
  dealer_cards.append(randomcard())

def score_hand(hand):
  score = 0
  for cards in hand:
    score += cards
  if score > 21 and 11 in hand:
    for element in range(len(hand)):
      if hand[element] == 11:
        hand[element] = 1
        return score - 10
  else:
    return score

def dealer_play(hand):
  while score_hand(hand) < 17:
    hand.append(randomcard())

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")

if play == 'y':
  print(logo)
  deal_starting_cards()

while play == 'y':
  cur_player_score = score_hand(player_cards)
  print(f"   Your cards: {player_cards}, current score: {cur_player_score} ")
  print(f"   Computer's first card: {dealer_cards[0]}")
  play = input("Type 'y' to get another card, type 'n' to pass: ")
  if play:
    player_cards.append(randomcard())
