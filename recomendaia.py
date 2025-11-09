"""
RecomendaIA - Intelligent Recommendation Assistant
Author: Davi Sampaio
Institution: Universidade Federal da Bahia (UFBA)
Program: Ciência e Tecnologia

Description:
------------
RecomendaIA is an intelligent assistant that recommends movies, books, or music
based on user preferences using a simple local model simulation. 
The project is designed to later integrate with real LLM APIs 
(OpenAI, Hugging Face, or others) for enhanced reasoning and personalization.

This version runs locally and simulates AI recommendations.
"""

import random

# --- Local database simulation ---
movies = ["Inception", "Interstellar", "The Matrix", "The Social Network", "Ex Machina"]
books = ["1984 - George Orwell", "Sapiens - Yuval Noah Harari", "The Selfish Gene - Richard Dawkins", "Dune - Frank Herbert"]
music = ["Bohemian Rhapsody - Queen", "Imagine - John Lennon", "Clocks - Coldplay", "Blinding Lights - The Weeknd"]

def recommend(category):
    """Returns a random recommendation based on the chosen category."""
    if category == "movies":
        return random.choice(movies)
    elif category == "books":
        return random.choice(books)
    elif category == "music":
        return random.choice(music)
    else:
        return "Sorry, I can only recommend movies, books, or music for now."

def main():
    print("🎧 Welcome to RecomendaIA!")
    print("I can recommend something for you to enjoy.")
    print("Categories: movies | books | music")
    print("-" * 50)

    while True:
        category = input("\nWhat category would you like a recommendation from? ").lower()
        if category in ["exit", "quit"]:
            print("Goodbye! Thanks for using RecomendaIA.")
            break
        print(f"\n Recommendation: {recommend(category)}")

if __name__ == "__main__":
    main()
