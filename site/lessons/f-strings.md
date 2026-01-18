---
title: f-Strings
author:
- Alyssa Lytle
page: lessons
template: overview
---

# f-strings

*f-strings* are a helpful way to embed expressions directly into strings!

Without f-strings: 

```
    print("They are " + str(30 + 1))
```

With f-strings: 

```
    print(f"They are {30 + 1}")
```

Both will output the string:

<pre><div class="terminal">
They are 31
</div>
</pre>

Note that you didn't have to convert `30+1` from an `int` into a `str` using `str(30 + 1)`. The f-string handles that for you implicitly!

That's it! It's just another syntax to help you write strings!

## Practice

Try re-writing the following as an f-string:

```
    student: str = "Dave"
    course: int = 110
    message: str = "Hello " + student + " welcome to Comp " + str(course) "!"
```

### Answer


```
    student: str = "Dave"
    course: int = 110
    message: str = f"Hello {student} welcome to Comp {course}!"
```