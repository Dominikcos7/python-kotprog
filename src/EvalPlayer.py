from random import randint

from src.AIPlayer import AIPlayer
from src.Card import Card
from src.Hand import Hand
from src.enums.Rank import Rank
from src.enums.Suit import Suit


class EvalPlayer(AIPlayer):
    def __init__(self, name: str, chips: int, player_id: int):
        super().__init__(name, chips, player_id)
        self.raise_bar = 15
        self.call_bar = 10
        self.check_bar = 5
        self.fold_bar = 0
        self.eval_fill_cards = [Card(Suit.HEART, Rank.ACE), Card(Suit.SPADE, Rank.KING), Card(Suit.CLUB, Rank.EIGHT)]

    def act(self, highest_bid: int) -> None:
        if len(self.hand.cards) >= 5:
            hand = self.hand
        else:
            hand = Hand()
            hand.cards = [card for card in self.hand.cards]
            hand.cards.extend(self.eval_fill_cards)

        hand_eval = hand.evaluate()
        if hand_eval < 1500:
            self.align_bars(-14)
        elif hand_eval < 3000:
            self.align_bars(-9)
        elif hand_eval < 5000:
            self.align_bars(-5)
        elif hand_eval > 6000:
            self.align_bars(4)

        action = randint(0, 20)
        while True:
            try:
                print(self.name)
                print(action)
                print(self.raise_bar)
                print(self.call_bar)
                print(self.check_bar)
                print(self.fold_bar)
                if action > self.raise_bar:
                    amount = min(self.chips, randint(1, 100))
                    print(f"{self.name} raised, highest_bid: {highest_bid}")
                    self.action_raise(amount, highest_bid)
                    break
                elif action > self.call_bar:
                    print(f"{self.name} called, highest_bid: {highest_bid}")
                    amount = self.get_amount_to_call(highest_bid)
                    self.action_call(amount)
                    break
                elif action > self.check_bar:
                    print(f"{self.name} checked, highest_bid: {highest_bid}")
                    self.action_check(highest_bid)
                    break
                else:
                    print(f"{self.name} folded, highest_bid: {highest_bid}")
                    self.action_fold()
                    break
            except ValueError:
                action -= 5

        self.reset_bars()

    def align_bars(self, amount: int) -> None:
        self.raise_bar += amount
        self.call_bar += amount
        self.check_bar += amount
        self.fold_bar += amount

    def reset_bars(self) -> None:
        self.raise_bar = 15
        self.call_bar = 10
        self.check_bar = 5
        self.fold_bar = 0
