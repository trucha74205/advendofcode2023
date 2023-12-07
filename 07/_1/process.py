import time
from functools import cmp_to_key

start_time = time.time()

file_path = "input.txt"
total_sum = 0

hands = []

card_ranks = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2
}


def getHandRank(card_count):
    count_values = list(card_count.values())
    count_values.sort(reverse=True)
    if len(count_values) == 1:
        return 7  # 5 the same
    elif len(count_values) == 5:
        return 1  # all different -> high card
    elif len(count_values) == 2:
        if count_values[0] == 4 or count_values[1] == 4:
            return 6  # 4 the same
        else:
            return 5  # full house
    elif len(count_values) == 3:
        if count_values[0] == 3 or count_values[1] == 3 or count_values[2] == 3:
            return 4  # 3 the same
        else:
            return 3  # one pair
    elif len(count_values) == 4:
        return 2  # 1 pair
    else:
        return -1


def countCards(cards):
    card_count = {}
    for card in cards:
        card_count[card] = card_count.get(card, 0) + 1
    return card_count


def compareHands(hand1, hand2):
    cards1 = hand1[0]
    cards2 = hand2[0]

    card_count1 = countCards(cards1)
    card_count2 = countCards(cards2)

    hand_rank1 = getHandRank(card_count1)
    hand_rank2 = getHandRank(card_count2)

    if hand_rank1 != hand_rank2:
        return hand_rank1 - hand_rank2

    for i in range(5):
        if cards1[i] != cards2[i]:
            return card_ranks[cards1[i]] - card_ranks[cards2[i]]

    return 0


with open(file_path, "r") as file:
    for line in file:
        hands.append(line.strip().split(" "))

sorted_hands = sorted(hands, key=cmp_to_key(compareHands))

for index, hand in enumerate(sorted_hands):
    total_sum += (index + 1) * int(hand[1])

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Time taken: {elapsed_time} seconds")
print(f"Sum of all hands bids: {total_sum}")
