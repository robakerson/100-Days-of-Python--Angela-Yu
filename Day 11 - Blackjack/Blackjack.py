cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
from art import logo
import random
from replit import clear

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
  #automatically replace aces with 1 if we bust with ace in hand
  #if we seek a more robust program this could be handled outside this function but I choose to do it here because we only ever add 1 card at a time
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

def check_blackjack():
  #check if user has blackjack & win immediately
  if player_cards == [10, 11] or player_cards == [11, 10]:
    final_player_score = score_hand(player_cards)
    final_dealer_score = score_hand(dealer_cards)
    print(f"   Your cards: {player_cards}, final score: {final_player_score} ")
    print(f"   Computer's final hand: {dealer_cards}, final score: {final_dealer_score}")
    print("Win with a Blackjack 😎")
    return True
  #check if dealer has blackjack and lose immediately
  if dealer_cards == [10, 11] or dealer_cards == [11, 10]:
    final_player_score = score_hand(player_cards)
    final_dealer_score = score_hand(dealer_cards)
    print(f"   Your cards: {player_cards}, final score: {final_player_score} ")
    print(f"   Computer's final hand: {dealer_cards}, final score: {final_dealer_score}")
    print("Lose, opponent has Blackjack 😱")
    return True

def present_winner(player_cards, dealer_cards):
  dealer_play(dealer_cards)
  final_player_score = score_hand(player_cards)
  final_dealer_score = score_hand(dealer_cards)
  print(f"   Your final hand: {player_cards}, final score: {final_player_score}")
  print(f"   Computer's final hand: {dealer_cards}, final score: {final_dealer_score}")
  if final_player_score > 21:
    print("You went over. You lose 😭")
  elif final_dealer_score > 21:
    print("Opponent went over. You win 😁")
  elif final_player_score > final_dealer_score:
    print("You win 😃")
  elif final_dealer_score > final_player_score:
    print("You lose 😤")
  elif final_dealer_score == final_player_score:
    print("Draw 🙃")

def player_play():
  cur_player_score = score_hand(player_cards)
  print(f"   Your cards: {player_cards}, current score: {cur_player_score} ")
  print(f"   Computer's first card: {dealer_cards[0]}")
  if cur_player_score > 21:
    return
  else:
    draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
  if draw_card =='y':
    player_cards.append(randomcard())
    player_play()


while input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == 'y':
  clear()
  print(logo)
  player_cards = []
  dealer_cards = []
  deal_starting_cards()
  if not check_blackjack():
    player_play()
    present_winner(player_cards, dealer_cards)
