---
title: Practice Memory Diagram
author:
- Alyssa Lytle
page: lessons
template: overview
---

# Snippet

```
    class Playlist:
        
        name: str
        songs: int
        on_repeat: bool
        
        def __init__(self, name: str, songs: int, repeat: bool):
            self.name = name
            self.songs = songs
            self.on_repeat = repeat
        
        def __add__(self, num_songs: int) -> Playlist:
            return Playlist(self.name + "_copy", self.songs + num_songs, self.on_repeat)
        
        def __str__(self) -> str:
            return f"{self.name}: {self.songs} songs"
        
        def playlist_length(self) -> int:
            total: int = 0
            total = self.songs * 3
            if self.on_repeat:
                total *= 2
            return total
        
    p1: Playlist = Playlist("Hits", 9, True)
    p2: Playlist = p1 + 1
    print(p1)
    print(p2.playlist_length())
```

# Solution



<!-- <img class="img-fluid" src="/static/practice-mem-diagrams/playlist_sol.png" alt=""  />  -->