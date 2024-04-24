---
title: Practice Memory Diagram
author:
- Alyssa Lytle
page: lessons
template: overview
---

# Snippet

*(I updated this snippet to make it a better example.)*

```
    class Team:
            
        team_name: str
        players: list[str]
            
        def __init__(self, inp_name: str, inp_players: list[str] = []):
            self.team_name = inp_name
            self.players = inp_players
        
        def add_player(self, player_name: str)-> None:
            self.players.append(player_name)
            
        def __str__(self) -> str:
            info: str = f"{self.team_name}: {self.players}"
            return info
                
    teammates: list[str] = ["Alyssa", "Jayden"]
    team0: Team = Team("Rockets", teammates)
    team1: Team = Team("Wombats")
    team1.add_player("Chiara")
    team1.add_player("Shefali")
    print(team1)
```

# Solution
<!-- [Solution Video](https://youtu.be/boGourwMcNc)
<img class="img-fluid" src="/static/assets/f23/team_sol.png" alt=""  /> -->
