---
title: Halloween Mystery Project 2021 Fall
date: 2021-10-20
author:
- Ezri White
page: logistics
template: overview
site-branch: team
---

## Preface

In this project students will work through a mix of real life puzzles, scavenger hunting, and code puzzles. The code component of this project should not be super complex for students who are relatively caught up with the course and will more likely serve as a review for earlier concepts, dictionaries and show a simple preview of 2D lists. The in-person elements of this project primarily involve searching for QR codes at different UNC and Sitterson landmarks to unlock the next piece of the mystery.

Students should be encouraged to work together on all components of this project except for the code writing.

## Chapter 0 - _The Note_
* Someone has kidnapped kaki! Her security lab partner has given us a note that he found that says:

> CFMMU PXFSX JOEPX 

* The lab partner thinks it is a caesar cipher shifted by one and has given some instructions on how to write code to solve this <a href="/mystery/chapter-zero.html" target="_blank">here</a>.
* Once the code is written, the message turns into: 

> BELLT OWERW INDOW

## Chapter 1 -  _The Bell Tower_
* Under a bench at the bell tower will be a shift number & QR code that opens to <a href="/mystery/chapter-one-train-herb-noble.html" target="_blank">this page</a>.
* The page on the site has a longer piece of Caesar text to decode by the given shift number. This page will also include instructions for the more robust Caesar decoder function that can handle whole chunks of text and any shift number.
* Once decoded this piece of text will read as follows:

> We might need to return to the crime scene... Sitterson itself. Fred Brooks is always watching over the building... from the bottom floor. Perhaps he saw something? Take a look beneath him and see if he left us any clues.

## Chapter 2 -  _The Crime Scene_
* At Sitterson there will be another shift number and QR code taped next to both the portraits of Fred Brooks and Sitterson that take you to <a href="/mystery/chapter-two-vessel-tourist-holiday.html" target="_blank">this page</a>.  
* This page will have more ceaser text to decode but no new function necessary.
* The decoded text will let students know that  

> I think the Teaching Assistants know more than they are saying but they will only talk if you can solve the following questions. Everyone loves the internet but it's time to return to our roots. Try looking in the upper lobby...


> 1. What is the name of UNC's Assistive robot?
2. How is the virtual reality helmet from around 1991 to 1997 described?
3. What is the nickname for the UNC Department of Computer Science DEC BP 11/45?

> "Make an office hours ticket with the answers to the above questions filled into the phrase '1.______ the 2.____ _____ is 3.______' in the description."


* If we see an office hours ticket that contains `Baxter the work horse is sleepy` then the ticket will be closed and the student will be sent an email with the following message:

> I am sorry we couldn’t figure out your issue in office hours! I think there is a book that might have the answer. It’s called the Dictionary of The Art of Printing by William Savage. Last I saw it was on the 8th floor of Davis. 
🍰🍭🕸🕸💻 🐓🍭 🔍💀 🍰🍭 🍁🕸💻⛄🐓🌲🍁, 🌲 👽👻 🔥🍭🕸🕸🌲💀🎃 🌲 🔥🌲⛸⛸ 🔍💀 💅💀🌺🐓. 🔍👽🍁🌈 🔥🦄💀💅 🌈👽🌈🌲 🐓🍭🍭🌈 🐓🦄💀 🍁⛸👽🍰🍰 🌲🐓 🔥👽🍰 🐓👽🌽🥸🦄🐓 🌲💅 🦄👽💅💀🍰 👽🕸🐓 🍁💀💅🐓💀🕸. 🌲 🦄👽🍂💀 🦄🌲🎃🎃💀💅 👽💅🍭🐓🦄💀🕸 🍁⛸🌽💀 🐓🦄💀🕸💀, 👻👽🌈💀 🍰🌽🕸💀 🐓🍭 🔥👽🐓🍁🦄 🍭🌽🐓 😱🍭🕸 🐓🦄💀 🥸🌲👽💅🐓 🔍⛸🌽💀 🍰🐟🌽🌲🎃 🍁🍭👻🌲💅🥸 🍭🌽🐓 🍭😱 🐓🦄💀 🥸🕸🍭🌽💅🎃 🔥🦄🌲⛸💀 💻🍭🌽🕸💀 🐓🦄💀🕸💀

* The emojis in this response will not be explained with the hope that students put 2 & 2 together when they find the cipher in the library.

## Chapter 3 - _The Library_
* On the 8th floor of Davis Library We will plant a book with the key to the emoji cipher and QR code that links to <a href="/mystery/chapter-three-powder-rubbish-medal.html" target="_blank">this page</a>.
* The new page will contain non-encoded instructions for writing a dictionary decoder for the emojis.
* This decoder will use a 1:1 emoji:character dictionary so it will be good review for students. Once the message is decoded from emojis to characters, it also needs to be run through the Caesar cipher with a shift number of 9 (per the weird part about shift end in the TA email). The dictionary is as follows:

~~~ {.python }
 {'👽': 'a', '🔍': 'b', '🍁': 'c', '🎃': 'd', '💀': 'e', '😱': 'f', '🥸': 'g', '🦄': 'h', '🌲': 'i', 
  '🌵': 'j', '🌈': 'k', '⛸': 'l', '👻': 'm', '💅': 'n', '🍭': 'o', '⛄': 'p', '🐟': 'q', '🕸': 'r', 
  '🍰': 's', '🐓': 't', '🌽': 'u', '🍂': 'v', '🔥': 'w', '🌺': 'x', '💻': 'y', '🔦': 'z'}
~~~       

* The emoji message from the TA’s will say the following: 

> sorry to be so cryptic, i am worried i will be next. back when kaki took the class it was taught in hanes art center. i have hidden another clue there, make sure to watch out for the giant blue squid coming out of the ground while youre there

## Chapter 4 - _The Artists_
* To pay respects to 110 semesters past, the students will now visit Hanes Art Center
* There will be a QR code that links to <a href="/mystery/chapter-four-sulphur-ghost-horse.html" target="_blank">this page</a> on/near the blue horn looking sculptures.
* This page will contain a series of 1's and 0's in a 2D list:

> [[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0], [1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1], [0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]]

* There will also be a basic explanation of ASCII art and instructions on how to write the 2D list printer.

* If printed correctly the 2D list will display the following ascii art of the old well and an arrow pointing to one of the benches next to it.

~~~ {.python }
        @ @@ @                                                         @ @@ @        
    @@@ @ @@ @@@ @                                        @        @@@ @ @@ @@@ @    
 @@@ @@ @@@ @@ @@@@ @                 @@@@@@@@@           @     @@@ @@ @@@ @@ @@@@ @ 
@@ @@ @@@ @@@@@@ @ @@@               @@@@@@@@@@@          @    @@ @@ @@@ @@@@@@ @ @@@
   @ @@@ @@@ @ @@ @                  @@@@@@@@@@@          @       @ @@@ @@@ @ @@ @   
          @@                          @ @ @ @ @         @@@@@            @@          
          @@                          @ @ @ @ @          @@@             @@          
          @@                          @ @ @ @ @           @              @@          
          @@                          @ @ @ @ @                          @@          
         @@@@          @@@@@@@      @@@@@@@@@@@@@      @@@@@@@          @@@@         
     @@@@@@@@@@@@       @   @      @@@@@@@@@@@@@@@      @   @       @@@@@@@@@@@@      
~~~ 

## Chapter 5 - _The Culprit_
* Students will find a QR code under a bench near the old well that links to <a href="/mystery/chapter-five-acorn-mail-cliff.html" target="_blank">this page</a>.
* This page displays the answer to the mystery and students will just need to report this to the final survey along with any pictures they took along the way



## Items left before project is ready to go

* Finish instructions for the 2D list printer
* determine what book / section we should put the QR code in davis
* Re-encode TA message once wording is finalized
* make QR codes for all relevant sites
* put QR codes around campus
* add surveys to the different student stops