from src.Hand import Hand
from src.SoundPlayer import play_chips_sound


class Player:
    """
    This class is a base class for all player classes.
    """

    def __init__(self, name: str, chips: int, player_id: int = 0):
        """
        :param name: the name of the player
        :param chips: the amount of chips the player has
        :param player_id: the id of the player
        """

        self.id = player_id
        self.chips = chips
        self.chips_on_table = 0
        self.hand = Hand()
        self.name = name
        self.acted = False
        self.last_action = ''
        self.is_raising = False
        self.is_all_in = False

    def action_all_in(self):
        self.acted = True
        self.last_action = 'all in'
        self.is_all_in = True
        self.put_chips_on_table(self.chips)

    def action_call(self, amount: int):
        """
        :param amount: the amount to call
        """

        if amount <= 0:
            raise ValueError("Call amount must be larger than 0.")

        if self.chips <= 0:
            raise ValueError("Cannot call with 0 or less chips.")

        call_amount = min(amount, self.chips)
        self.acted = True
        self.last_action = 'call'
        self.put_chips_on_table(call_amount)

    def action_check(self, highest_bid: int):
        """
        :param highest_bid: the highest bid at the table
        """

        if self.chips_on_table < highest_bid:
            raise ValueError("Cannot check if highest bid hasn't been called.")

        self.acted = True
        self.last_action = 'check'

    def action_fold(self):
        self.hand.empty()
        self.acted = True
        self.last_action = 'fold'

    def action_raise(self, amount: int, call_amount: int):
        """
        :param amount: the amount to raise
        :param call_amount: the amount to call on the table
        """

        if amount <= call_amount:
            raise ValueError("Cannot raise less or equal than call amount")

        if self.chips < amount:
            raise ValueError("Cannot raise more than the amount of chips the player has.")

        if self.chips <= 0:
            raise ValueError("Cannot raise with 0 or less chips.")

        if amount <= 0:
            raise ValueError("Raise amount must be larger than 0.")

        self.acted = True
        self.last_action = 'raise'
        self.put_chips_on_table(amount)

    def get_amount_to_call(self, highest_bid: int) -> int:
        """
        :param highest_bid: the highest bid at the table
        :return:
        """

        return highest_bid - self.chips_on_table

    def is_folded(self) -> bool:
        return self.hand.is_empty()

    def put_chips_on_table(self, amount: int):
        """
        :param amount: the amount of chips to put on the table
        """

        self.chips -= amount
        self.chips_on_table += amount

        if not self.is_all_in and self.chips <= 0:
            self.action_all_in()

        play_chips_sound()
