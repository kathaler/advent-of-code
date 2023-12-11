from utils import *

class Card:
    def __init__(self, card_number, winning_numbers, numbers, copies = 1):
        self.card_number = card_number
        self.winning_numbers = winning_numbers
        self.numbers = numbers
        self.copies = copies

    def __str__(self):
        return f"Card Number {self.card_number}\n Winning Numbers {self.winning_numbers}\n Numbers: {self.numbers}\n Copies: {self.copies}"
    
    def add_copy(self):
        self.copies += 1
    
    
def get_cards(word_list):
    cards = []
    for l in word_list:
        card_num = l[1].strip(':')
        sep = l.index('|')
        winning_nums = l[2:sep]
        nums = l[sep + 1:]
        cards.append(Card(card_num, winning_nums, nums))       
    return cards

def get_num_wins(card): 
    num_win = -1
    for num in card.winning_numbers:
        if num in card.numbers:
            num_win += 1
    return num_win

def count_copies(cards):
    sum = 0
    for card in cards:
        sum += card.copies
    return sum

def part1(cards):
    sum = 0
    for card in cards:
        num_win = get_num_wins(card)
        if num_win > -1:
            sum += 2**num_win
    return sum

def part2(cards):
    for i, card in enumerate(cards):
        num_win = get_num_wins(card) + 1
        for j in range(card.copies): 
            temp = i + 1
            while temp <= len(cards) and temp - i <= num_win:
                cards[temp].add_copy()
                temp += 1
    return count_copies(cards)


word_list = read_lines_to_word_lists("2023/inputs/day4.txt")
cards = get_cards(word_list)
print(part1(cards))
print(part2(cards))