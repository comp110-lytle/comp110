from __future__ import annotations

class ChristmasTreeFarm:
    
    plots: list[int]
    
    def __init__(self, plots: int, initial_planting: int):
        self.plots = []
        for i in range(0,initial_planting):
            self.plots.append(1)
        for i in range(initial_planting, plots):
            self.plots.append(0)
    
    def plant(self, tree_idx: int) -> None:
        self.plots[tree_idx] = 1
    
    def growth(self) -> None:
        for tree_idx in range(0,len(self.plots)):
            if self.plots[tree_idx] > 0:
                self.plots[tree_idx] += 1
    
    def harvest(self, replant: bool) -> int:
        harvest_count = 0
        for tree_idx in range(0,len(self.plots)):
            if self.plots[tree_idx] >= 5:
                harvest_count += 1
                if replant:
                    self.plots[tree_idx] = 1
                else:
                    self.plots[tree_idx] = 0
        return harvest_count
    
    def __add__(self, other_farm: ChristmasTreeFarm) -> ChristmasTreeFarm:
        plot_size: int = len(self.plots) + len(other_farm.plots)
        num_trees: int = 0
        for tree in self.plots:
            if tree > 0:
                num_trees += 1
        for tree in other_farm.plots:
            if tree > 0:
                num_trees += 1
        return ChristmasTreeFarm(plot_size, num_trees)
        