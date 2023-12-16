"""File to define River class"""

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear

class River:
    
    day: int
    bears: list[Bear]
    fish: list[Fish]
    
    def __init__(self, num_fish: int, num_bears:int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def remove_fish(self, amount: int):
        while amount > 0:
            amount -= 1
            self.fish.pop(0)
 
    def bears_eating(self):
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
            
    
    def check_hunger(self):
        new_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                new_bears.append(bear)
        self.bears = new_bears
        
                
    def check_ages(self):
        new_fish: list[Fish] = []
        new_bears: list[Bear] = []
        for bear in self.bears:
            if bear.age <= 5:
                new_bears.append(bear)
        for fish in self.fish:
            if fish.age <= 3:
                new_fish.append(fish)
        self.fish = new_fish
        self.bears = new_bears
    
    def repopulate_fish(self):
        """Adds new fish to fist list."""
        for index in range((len(self.fish) // 2) * 4):
            self.fish.append(Fish())
        
    def repopulate_fish(self):
        num_fish: int = len(self.fish)
        new_fish: int = (num_fish//2) * 4
        for x in range(new_fish):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        num_bears: int = len(self.bears)
        new_bears: int = num_bears//2
        for x in range(new_bears):
            self.bears.append(Bear())
    
    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
            
    def one_river_day(self):
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        for x in range(7):
            self.one_river_day()