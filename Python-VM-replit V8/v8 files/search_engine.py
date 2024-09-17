import tkinter as tk
import requests
from bs4 import BeautifulSoup 
import subprocess

def exit():
    root.destroy()
    subprocess.call(["python", "file_run.py"])


def search_function():
    query = query_inp.get("1.0", tk.END).strip()
    results = wikipedia_search(query)
    display_results(results)

def wikipedia_search(query):
    """
    Searches Wikipedia using its API.

    Args:
        query: The search term.

    Returns:
        A list of search results (dictionaries).
    """

    url = f'https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={query}&format=json'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data['query']['search']
    else:
        print(f"Error: {response.status_code}")
        return []

def display_results(results):
    results_text.delete("1.0", tk.END)  # Clear previous results

    for result in results:
        # Clean the snippet using BeautifulSoup
        soup = BeautifulSoup(result['snippet'], 'html.parser')
        cleaned_snippet = soup.get_text(separator=' ')  # Extract text, using a space as separator

        results_text.insert(tk.END, f"Title: {result['title']}\n")
        results_text.insert(tk.END, f"Snippet: {cleaned_snippet}\n")
        results_text.insert(tk.END, f"URL: https://en.wikipedia.org/wiki/{result['title'].replace(' ', '_')}\n\n")

root = tk.Tk()
root.title("SCRAPE engine")
root.geometry("500x700")
root.configure(bg="cadetblue4")

label = tk.Label(text="Enter Search Query", fg="black", height=3, width=30, bg="cadetblue4", font=25)
label.pack()

query_inp = tk.Text(root, height=1, width=50, font=40)
query_inp.pack(pady=100, padx=20)

go_button = tk.Button(text="SEARCH", fg="black", bg="gray", height=1, width=10, command=search_function)
go_button.pack()

exit_button = tk.Button(text="EXIT", fg="black", bg="red", height=1, width=10, command=exit)
exit_button.pack(side="top", pady = 5, padx=40)

# Create a Text widget to display results
results_text = tk.Text(root, height=15, width=50, wrap=tk.WORD)
results_text.pack(pady=20)

root.mainloop()

# Made by Zach H. 2024
