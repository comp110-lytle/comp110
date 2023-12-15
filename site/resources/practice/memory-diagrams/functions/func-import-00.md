---
title: Practice Memory Diagram
author:
- Created by Kaleb White
- Reviewed by Rosey Anim
- Published by Alyssa Lytle
page: lessons
template: overview
---

# Snippet

<pre>
<code class="python">   def big_func(num: int) -> int:
        a: int = num + 2
        return a

    def bigger_func(num: int) -> int:
        a: int = big_func(num) * 2
        return a

    def biggest_func(num: int) -> int:
        a: int = bigger_func(num) ** 2
        return a

    def main() -> None:
        a: int = 110 
        a = biggest_func(a)
        print(f"Wow! {a} is a big number!")

    if __name__ == "__main__":
        main()
</code></pre>

# Solution

<img class="img-fluid" src="/static/assets/f23/func-import-00-sol.png" alt="The memory diagram is labeled Stack, Heap, and Output, on the left, center, and right of the page. Stack contains five frames, including Globals, main, biggest_func, bigger_func, and big)func, from top to bottom. 
The frame Globals contains four references to function definitions. Function big_func points to lines 1-3 on the heap. bigger_func points to lines 5-7. biggest_func points to lines 9-11. main points to lines 13-16. 
Each frame has a RA (return address) and RV (return value) listed on their left side. For the frame main, the RA is 19 and RV is none. main also contains the variable a, which initially is assigned 110. After the execution of all other frames, a’s value is reassigned to 50176.
The next frame after main is biggest_func. biggest_func has an RA of 15 and an RV of 50176, although the RV will remain blank until the execution of bigger_func and big_func. It is called with the parameter num assigned a value of 110. It also contains the local variable a, which will be blank until just before RV is determined. a’s value will be 50176. As the parameter num is initialized as a result of the function call, it is located above local variable a.
The frame after biggest_func is bigger_func. bigger_func has the same names for local variables and parameters as biggest_func. bigger_func has an RA of 10 and RV of 224. It also contains parameter num with the value 110 and local variable a with the value 224. The value of a and RV will only be found after the execution of big_func. 
The last frame is the function big_func. big_func has an RA of 6 and RV of 112. It also has the parameter num with a value of 110 and local variable a with a value of 112.
After all the frames below main have returned, function main will print out “Wow! 50176 is a big number!”. This sentence is listed under Output, on the right."  />

*Image Description:* The memory diagram is labeled Stack, Heap, and Output, on the left, center, and right of the page. Stack contains five frames, including Globals, main, biggest_func, bigger_func, and big_func, from top to bottom. 

The frame Globals contains four references to function definitions. Function big_func points to lines 1-3 on the heap. bigger_func points to lines 5-7. biggest_func points to lines 9-11. main points to lines 13-16. 

Each frame has a RA (return address) and RV (return value) listed on their left side. For the frame main, the RA is 19 and RV is none. main also contains the variable a, which initially is assigned 110. After the execution of all other frames, a’s value is reassigned to 50176.

The next frame after main is biggest_func. biggest_func has an RA of 15 and an RV of 50176, although the RV will remain blank until the execution of bigger_func and big_func. It is called with the parameter num assigned a value of 110. It also contains the local variable a, which will be blank until just before RV is determined. a’s value will be 50176. As the parameter num is initialized as a result of the function call, it is located above local variable a.

The frame after biggest_func is bigger_func. bigger_func has the same names for local variables and parameters as biggest_func. bigger_func has an RA of 10 and RV of 224. It also contains parameter num with the value 110 and local variable a with the value 224. The value of a and RV will only be found after the execution of big_func. 

The last frame is the function big_func. big_func has an RA of 6 and RV of 112. It also has the parameter num with a value of 110 and local variable a with a value of 112.

After all the frames below main have returned, function main will print out “Wow! 50176 is a big number!”. This sentence is listed under Output, on the right.
