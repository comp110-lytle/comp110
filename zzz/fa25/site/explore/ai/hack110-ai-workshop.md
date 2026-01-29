---
title: AI Workshop
author:
   - Dika Manne
page: explore
template: overview
---


### Training Model Code


```{.python .numberLines startFrom="1"}
   # train_model.py
   import spacy


   # Load the English NLP model
   nlp = spacy.load("en_core_web_sm")


   # Sample training data (replace this with your own dataset)
   training_data = [
       ("Hello, how are you?", {"intent": "greeting"}),
       ("Tell me a joke.", {"intent": "joke"}),
       # Add more training examples with intents
   ]


   # Train the spaCy NLP model
   for text, annotations in training_data:
       doc = nlp(text)
       for word in doc:
           # You can customize this part based on your chatbot's requirements
           if word.is_alpha:
               annotations.setdefault("entities", []).append((word.idx, word.idx + len(word.text), "WORD"))


   # Save the trained model (you'd typically save it to a file for later use)
   nlp.to_disk("chatbot_model")
```


### Main Flask Application Code


```{.python .numberLines startFrom="1"}
   # app.py
   from flask import Flask, render_template, request
   import spacy


   app = Flask(__name__)


   # Load the spaCy NLP model
   nlp = spacy.load("chatbot_model")  # Load the trained model


   @app.route('/')
   def home():
       return render_template('index.html')


   @app.route('/chat', methods=['POST'])
   def chat():
       user_input = request.form['user_input']


       # Process user input using the trained spaCy NLP model
       doc = nlp(user_input)
       # Extract entities or perform other NLP tasks as needed


       # You can customize this part based on your chatbot's requirements
       bot_response = "I'm a simple chatbot, and I don't understand much yet!"


       return render_template('index.html', user_input=user_input, bot_response=bot_response)


   if __name__ == '__main__':
       app.run(debug=True)
```




### HTML File


```{.python .numberLines startFrom="1"}
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <link rel="stylesheet" href="static/style.css">
       <title>Chatbot Workshop</title>
   </head>
   <body>
       <div class="container">
           <div class="chat-container">
               <div class="chat-box">
                   <div class="user-message">{{ user_input }}</div>
                   <div class="bot-message">{{ bot_response }}</div>
               </div>
           </div>
           <div class="user-input">
               <form action="/chat" method="post">
                   <input type="text" name="user_input" placeholder="Type your message...">
                   <button type="submit">Send</button>
               </form>
           </div>
       </div>
   </body>
   </html>
```


### CSS File


```{.python .numberLines startFrom="1"}
   body {
       font-family: Arial, sans-serif;
   }


   .container {
       max-width: 600px;
       margin: auto;
   }


   .chat-container {
       border: 1px solid #ccc;
       border-radius: 5px;
       overflow: hidden;
       margin-bottom: 10px;
   }


   .chat-box {
       padding: 10px;
   }


   .user-message {
       background-color: #e0f7fa;
       border-radius: 5px;
       margin-bottom: 5px;
   }


   .bot-message {
       background-color: #f0f0f0;
       border-radius: 5px;
       margin-bottom: 5px;
   }


   .user-input {
       display: flex;
   }


   input {
       flex: 1;
       padding: 10px;
       border: 1px solid #ccc;
       border-radius: 5px 0 0 5px;
   }


   button {
       padding: 10px;
       border: 1px solid #ccc;
       border-radius: 0 5px 5px 0;
       background-color: #4caf50;
       color: white;
       cursor: pointer;
   }


   button:hover {
       background-color: #45a049;
   }
```