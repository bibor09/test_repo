import random


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self, deck):
        card = deck.deal()
        if card:
            self.hand.append(card)

    def show_hand(self):
        print(f"{self.name}'s hand:")
        for card in self.hand:
            print(card)


def main():
    deck = Deck()
    deck.shuffle()

    players = []
    num_players = 4
    for i in range(num_players):
        name = f"Player {i+1}"
        player = Player(name)
        players.append(player)

    num_cards_to_deal = 5
    for _ in range(num_cards_to_deal):
        for player in players:
            player.draw_card(deck)

    for player in players:
        player.show_hand()


# if __name__ == "__main__":
#     main()
