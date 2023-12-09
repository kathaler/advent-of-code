from utils import *

class Card:
    def __init__(self, card_number, winning_numbers, numbers):
        self.card_number = card_number
        self.winning_numbers = winning_numbers
        self.numbers = numbers

    def __str__(self):
        return f"Card Number {self.card_number}\n Winning Numbers {self.winning_numbers}\n Numbers: {self.numbers}"
    
    
def get_cards(word_list):
    cards = []
    for l in word_list:
        card_num = l[2].strip(':')
        sep = l.index('|')
        winning_nums = l[2:sep]
        nums = l[sep + 1:]
        cards.append(Card(card_num, winning_nums, nums))       
    return cards

def part1(cards):
    sum = 0
    for card in cards:
        num_win = -1
        for num in card.winning_numbers:
            if num in card.numbers:
                num_win += 1
        if num_win > -1:
            sum += 2**num_win
    return sum
                


word_list = read_lines_to_word_lists("2023/inputs/day4.txt")
cards = get_cards(word_list)
print(part1(cards))