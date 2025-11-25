def card_value(c):
    if c == 'A':
        return 1
    if c == 'J':
        return 11
    if c == 'Q':
        return 12
    if c == 'K':
        return 13
    return int(c)

def solve():
    N = int(input().strip())

    p1_cards, p2_cards = [], []
    for _ in range(N):
        C1, S1, C2, S2 = input().strip().split()
        p1_cards.append((card_value(C1), int(S1)))
        p2_cards.append((card_value(C2), int(S2)))

    suit_priority = list(map(int, input().strip().split()))
    # Higher priority = smaller index
    suit_rank = {suit: i for i, suit in enumerate(suit_priority)}

    def sort_deck(deck):
        # Sort by value ascending, then by suit priority (lower rank first)
        return sorted(deck, key=lambda x: (x[0], suit_rank[x[1]]))

    p1 = sort_deck(p1_cards)
    p2 = sort_deck(p2_cards)
    hand = []
    turn = 1  # 1 = Vaishnavi, 2 = Suraj

    def higher_priority(suit_a, suit_b):
        # True if suit_a has higher priority than suit_b
        return suit_rank[suit_a] < suit_rank[suit_b]

    while True:
        # check if game ended
        if not p1 and not p2:
            print("TIE")
            return
        elif not p1:
            print("LOSER")
            return
        elif not p2:
            print("WINNER")
            return

        # current player's deck
        deck = p1 if turn == 1 else p2
        card = deck.pop(0)  # play top card

        if not hand:
            hand.append(card)
            turn = 2 if turn == 1 else 1
            continue

        top_val, top_suit = hand[-1]
        if card[0] == top_val and higher_priority(card[1], top_suit):
            # current player wins the hand
            hand.append(card)
            # rearrange hand
            hand = sorted(hand, key=lambda x: (x[0], suit_rank[x[1]]))
            # add to bottom of winner’s deck
            deck.extend(hand)
            hand = []
            # same player continues
        else:
            hand.append(card)
            turn = 2 if turn == 1 else 1