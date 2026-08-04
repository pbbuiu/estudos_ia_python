
def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    sumHand1 = sum([char if isinstance(char, int) else (0 if char=='A' else 10) for char in hand_1 ])
    print(sumHand1)
    for char in hand_1:
        if char=='A':
            if 11+sumHand1 > 21:
                sumHand1 += 1
            else:
                sumHand1 += 11
    sumHand2 = sum([char if isinstance(char, int) else (0 if char=='A' else 10) for char in hand_2])
    print(sumHand2)
    for char in hand_2:
            if char=='A':
                if 11+sumHand2 > 21:
                    sumHand2 += 1
                else:
                    sumHand2 += 11

    print(sumHand1)
    print(sumHand2)

    if sumHand1 > 21 and sumHand2 <= 21:
        return False
    elif sumHand2 > 21 and sumHand1 <= 21:
        return True
    elif sumHand2 > 21 and sumHand1 > 21:
        return False
    else:
        if (sumHand1 > sumHand2):
            return True
        else:
            return False



print(blackjack_hand_greater_than(hand1, hand2))
