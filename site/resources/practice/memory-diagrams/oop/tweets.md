---
title: Practice Memory Diagram
author:
- Alyssa Lytle
page: lessons
template: overview
---

# Snippet

```
    class Profile:
        
        handle: str
        followers: int
        is_private: bool
        
        def __init__(self, handle: str):
            self.handle = handle
            self.followers = 0
            self.is_private = False
            
        def send(self, msg: str) ->  None:
            if not self.is_private:
                print(f"@{self.handle} says {msg}")
                
        def toggle_privacy(self) -> None:
            self.is_private = not self.is_private
            
    a: Profile = Profile("alyssa")
    b: Profile = Profile("tyler")
    a.send("Sup")
    b.toggle_privacy()
    b.send("Heyyy")
```

# Solution
[Video](https://youtu.be/MsxvXjYM8jo?si=SWlxs4pP0qNJljuU)

<img class="img-fluid" src="/static/practice-mem-diagrams/Profile.png" alt=""  /> 