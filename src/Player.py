from src.Hand import Hand


class Player:
    def __init__(self, name: str, chips: int):
        self.chips = chips
        self.chips_on_table = 0
        self.hand = Hand()
        self.name = name

    def action_all_in(self):
        self.put_chips_on_table(self.chips)

    def action_call(self, amount: int):
        if amount <= 0:
            raise ValueError("Call amount must be larger than 0.")

        if self.chips <= 0:
            raise ValueError("Cannot call with 0 or less chips.")

        call_amount = min(amount, self.chips)
        self.put_chips_on_table(call_amount)

    def action_check(self):
        pass

    def action_fold(self):
        self.hand.empty()

    def action_raise(self, amount: int):
        if self.chips < amount:
            raise ValueError("Cannot raise more than the amount of chips the player has.")

        if self.chips <= 0:
            raise ValueError("Cannot raise with 0 or less chips.")

        if amount <= 0:
            raise ValueError("Raise amount must be larger than 0.")

        self.put_chips_on_table(amount)

    def put_chips_on_table(self, amount: int):
        self.chips -= amount
        self.chips_on_table += amount
