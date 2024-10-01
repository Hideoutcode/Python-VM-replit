import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup


#background










#End chatbot

def chatbot():
  def send_message():
    user_input = entry.get()
    entry.delete(0, tk.END)  # Clear the entry field
    chat_history.config(state="normal")
    chat_history.insert(tk.END, "You: " + user_input + "\n")
    chat_history.config(state="disabled")

    response = get_response(user_input)
    chat_history.config(state="normal")
    chat_history.insert(tk.END, "Wikibot: " + response + "\n")
    chat_history.config(state="disabled")

    # Scroll to the bottom to see the latest message
    chat_history.see(tk.END)

  def get_response(user_input):
    user_input = user_input.lower()

    # Keyword dictionary (for simple responses)
    responses = {
      
      "who is your creator?": "Random Dude IDK",
       "What version is Wikibot?":"Wikibot is version 0.0.10",
        "hello": "Hello! How can I assist you?",
      "who made you": "The United States Government. \n\n\n\nJust kidding :) I am made by regular python programmer",
      "are you alive?": "Yes.",
      "no":"Why then, No questions? Silly. I can do more than questions! Jokes?, Facts, Riddles? You name it!",
      "yes":"Great! Ask any questions and I will try my best to come up with a answer for you!",

      "can you help me with something?": "Sure thing what is it that you need?",
      "hola":"I do not speak spanish, how may I help you",
      "wikibot?": "Yes, I am Wikibot, How may I help you?",
      "wikibot":"Hello! How can I help you today?",
     "Wikibot":"Hello, how may I help you?",
      "hello": "Hello there!, how may I be of service?",
      "hi": "Hi! How can I help?",
      "how are you": "I am incapable of feelings, but thanks for asking. How are you?",
      "what's your name": "As a chatbot, I do not have a formal name, but you can call me WikiBot.",
      "bye": "Goodbye! Have a nice day.",
      "goodbye": "Goodbye! Have a nice day.",
      "what is the meaning of life": "The meaning of life is a question that has been pondered by philosophers and theologians for centuries. There is no one definitive answer, and it is a matter of personal interpretation.",
      "what is the capital of france": "The capital of France is Paris.",
      "what is the weather like today": "I am sorry, I do not have access to real-time information, such as the weather. You can check a weather website or app for the latest forecast.",
      "tell me a joke": "Why don't scientists trust atoms? Because they make up everything! 😄",
      "what is the population of the earth": "The current estimated population of the Earth is around 8 billion people.",
      "what is the largest planet": "Jupiter is the largest planet in our solar system.",
      "what is the smallest planet": "Mercury is the smallest planet in our solar system.",
      "what is the hottest planet": "Venus is the hottest planet in our solar system.",
      "what is the coldest planet": "Uranus is the coldest planet in our solar system.",
      "what is the sun made of": "The Sun is primarily composed of hydrogen and helium.",
      "how many planets are there in the solar system": "There are eight planets in our solar system: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune.",
      "what is the speed of light": "The speed of light in a vacuum is approximately 299,792,458 meters per second.",
      "what is the capital of the united states": "The capital of the United States is Washington, D.C.",
      "what is the largest country in the world": "Russia is the largest country in the world by land area.",
      "what is the smallest country in the world": "Vatican City is the smallest country in the world by land area.",
      "what is the tallest mountain in the world": "Mount Everest is the tallest mountain in the world.",
      "what is the deepest ocean trench": "The Mariana Trench is the deepest ocean trench in the world.",
      "what is the largest ocean": "The Pacific Ocean is the largest ocean on Earth.",
      "what is the smallest ocean": "The Arctic Ocean is the smallest ocean on Earth.",
      "what is the longest river in the world": "The Nile River is the longest river in the world.",
      "what is the highest waterfall in the world": "Angel Falls is the highest waterfall in the world.",
      "what is the largest desert in the world": "The Antarctic Polar Desert is the largest desert in the world.",
      "what is the hottest desert in the world": "The Lut Desert in Iran is considered the hottest desert in the world.",
      "what is the largest rainforest in the world": "The Amazon Rainforest is the largest rainforest in the world.",
      "what is the most populous country in the world": "China is the most populous country in the world.",
      "what is the least populous country in the world": "Vatican City is the least populous country in the world.",
      "what is the richest country in the world": "The answer depends on how you define 'richest'.  By GDP per capita, Luxembourg is often considered the richest country.",
      "what is the poorest country in the world": "The answer depends on how you define 'poorest'.  By GDP per capita, Burundi is often considered one of the poorest countries.",
      "what is the currency of the united states": "The currency of the United States is the US dollar.",
      "what is the currency of europe": "The euro is the official currency of 19 out of the 27 member states of the European Union.",
      "what is the official language of the united states": "The United States does not have an official language at the federal level, but English is widely spoken and considered the de facto official language.",
  "good": "Great! I'm glad to hear that.\n how can I be of service?",
    "bad": "How can I make your day better?",
    "okay": "How may I be of service?",
      "fine":"How may I be of service?",
      "great":"How may I be of service?",
      "who are you":"ERROR SHUTDOWN SHUTDOWN",
      "who are you?":"ERROR SHUTDOWN SHUTDOWN",
      ".":"?"
      
    }
      
    
    

    for keyword, response in responses.items():
      if keyword in user_input:
        return response

    #Scrape wikipedia database foor info
    try:
      wikipedia_response = requests.get(f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={user_input}&format=json")
      wikipedia_data = wikipedia_response.json()
      results = wikipedia_data['query']['search']

      all_snippets = ""
      for result in results:
          wiki_page_title = result['title']
          wiki_page_snippet = result['snippet']
          soup = BeautifulSoup(wiki_page_snippet, 'html.parser')
          cleaned_snippet = soup.get_text()
          all_snippets += f"Here is what I found,Hope it helps!: \n\n**{wiki_page_title}**\n\n{cleaned_snippet}\n\n"

      return all_snippets

    except Exception as e:
      return "I could not find any information on that topic, try another?"

  def clear_chat_history():
    chat_history.config(state="normal")  # Enable the text area
    chat_history.delete("1.0", tk.END)  # Clear the text area
    chat_history.config(state="disabled")  # Disable the text area

  root = tk.Tk()
  root.title("PyPI WikiBot")
  root.resizable(False, False)
  
  
 

  # Chat History Text Area, for clear
  chat_history = tk.Text(root, state="disabled", wrap=tk.WORD)
  chat_history.pack(pady=10)

  # Input Frame, tk 
  input_frame = tk.Frame(root)
  input_frame.pack()

  entry = tk.Entry(input_frame, width=50)
  entry.pack(side="left", padx=10, pady=10)
  

  # Send Button
  send_button = tk.Button(input_frame, text="Send", command=send_message)
  send_button.pack(side="left")

  # Clear Button
  clear_button = tk.Button(input_frame, text="Clear", command=clear_chat_history)  # Use the clear_chat_history function
  clear_button.pack(side="left")

  root.bind("<Return>", lambda event: send_message())  # Enter key for sending
  root.bind("<C>", lambda event: clear_chat_history())

  root.mainloop()

chatbot()