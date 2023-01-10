class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *player_args):
        currently_added = []
        for player in player_args:
            if player not in self.players:
                currently_added.append(player)
                self.players.append(player)
        names = [player.name for player in currently_added]
        return f'Successfully added: {", ".join(names)}'

    def add_supply(self, *supply_args):
        for supply in supply_args:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.__find_if_player_exists(player_name)
        idx, supply = self.__find_supply_by_type(sustenance_type)
        # energy_units = [supply.energy for supply in self.supplies if supply.name == sustenance_type][-1]
        # all_foods = [food for food in self.supplies if food.name == "Food"]
        # all_drinks = [drink for drink in self.supplies if drink.name == "Drink"]

        if player is None:
            return
        if sustenance_type != "Drink" and sustenance_type != "Food":
            return

        # if sustenance_type == "Drink" and not all_drinks:
        # WHICH SUPPLY ????????? Food or Drink
        if sustenance_type == "Drink" and not supply:
            raise Exception("There are no drink supplies left!")

        # if sustenance_type == "Food" and not all_foods:
        if sustenance_type == "Food" and not supply:
            raise Exception("There are no food supplies left!")

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        # if player.stamina + energy_units > 100:
        if player.stamina + supply.energy > 100:
            player.stamina = 100
        else:
            # player.stamina += energy_units
            player.stamina += supply.energy
        self.supplies.pop(idx)
        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player1 = self.__find_if_player_exists(first_player_name)
        player2 = self.__find_if_player_exists(second_player_name)
        if player1.stamina == 0:
            return f"Player {player1.name} does not have enough stamina."
        if player2.stamina == 0:
            return f"Player {player2.name} does not have enough stamina."
        if player1.stamina == 0 and player2.stamina == 0:
            return f"Player {player1.name} does not have enough stamina.\n" + \
                   f"Player {player2.name} does not have enough stamina."

        if player1.stamina > player2.stamina:
            player1, player2 = player2, player1

        player2.stamina -= player1.stamina / 2
        if player2.stamina <= 0:
            player2.stamina = 0
            return f"Winner: {player1.name}"

        player1.stamina -= player2.stamina / 2
        if player1.stamina <= 0:
            player1.stamina = 0
            return f"Winner: {player2.name}"
        if player1.stamina < player2.stamina:
            return f"Winner: {player2.name}"
        return f"Winner: {player1.name}"

    def next_day(self):
        for player in self.players:
            if (player.stamina - player.age * 2) < 0:
                player.stamina = 0
            else:
                player.stamina -= player.age * 2
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = ""
        for player in self.players:
            result += str(player) + "\n"
        result.strip()
        for supply in self.supplies:
            result += supply.details() + "\n"
        result.strip()
        return result

    def __find_if_player_exists(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

    def __find_supply_by_type(self, sustenance_type):
        for idx in range(len(self.supplies) - 1, -1, -1):
            supply = self.supplies[idx]
            if supply.__class__.__name__ == sustenance_type:
                return idx, supply
        return -1, None

