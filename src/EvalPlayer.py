from random import randint

from src.AIPlayer import AIPlayer


class EvalPlayer(AIPlayer):
    """
    This class represents an AI player that is capable of evaluating its hand and to make a decision based on that
    evaluation.
    """

    def __init__(self, name: str, chips: int, player_id: int):
        """
        :param name: the name of the player
        :param chips: the amount of chips the player has
        :param player_id: the id of the player
        """

        super().__init__(name, chips, player_id)
        self.raise_bar = 15
        self.call_bar = 10
        self.check_bar = 5
        self.fold_bar = 0

    def act(self, highest_bid: int) -> None:
        """
        This function is called by the game when a player needs to act (when it's their turn). EvalPlayer uses bars for
        deciding which action to take. These bars get adjusted by the player's hand's evaluation, and represent
        probabilities of each action. The player throws a die, then takes an action based on whether the thrown value
        is over or under each bar.

        :param highest_bid: the highest bid on the table
        """

        hand_eval = self.hand.evaluate()
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
        """
        :param amount: the amount to align each bar by (it can be negative)
        """

        self.raise_bar += amount
        self.call_bar += amount
        self.check_bar += amount
        self.fold_bar += amount

    def reset_bars(self) -> None:
        self.raise_bar = 15
        self.call_bar = 10
        self.check_bar = 5
        self.fold_bar = 0
