from src.Hand import Hand


class Player:
    def __init__(self, name: str, chips: int, player_id: int = 0, is_human: bool = False):
        self.id = player_id
        self.is_human = is_human
        self.chips = chips
        self.chips_on_table = 0
        self.hand = Hand()
        self.name = name
        self.acted = False
        self.last_action = ''

    def action_all_in(self):
        self.put_chips_on_table(self.chips)
        self.acted = True
        self.last_action = 'all in'

    def action_call(self, amount: int):
        if amount <= 0:
            raise ValueError("Call amount must be larger than 0.")

        if self.chips <= 0:
            raise ValueError("Cannot call with 0 or less chips.")

        call_amount = min(amount, self.chips)
        self.put_chips_on_table(call_amount)
        self.acted = True
        self.last_action = 'call'

    def action_check(self, highest_bid: int):
        if self.chips_on_table < highest_bid:
            raise ValueError("Cannot check if highest bid hasn't been called.")

        self.acted = True
        self.last_action = 'check'

    def action_fold(self):
        self.hand.empty()
        self.acted = True
        self.last_action = 'fold'

    def action_raise(self, amount: int):
        if self.chips < amount:
            raise ValueError("Cannot raise more than the amount of chips the player has.")

        if self.chips <= 0:
            raise ValueError("Cannot raise with 0 or less chips.")

        if amount <= 0:
            raise ValueError("Raise amount must be larger than 0.")

        self.put_chips_on_table(amount)
        self.acted = True
        self.last_action = 'raise'

    def is_folded(self) -> bool:
        return self.hand.is_empty()

    def put_chips_on_table(self, amount: int):
        self.chips -= amount
        self.chips_on_table += amount
