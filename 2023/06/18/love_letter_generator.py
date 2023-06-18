import random


# Function to get a list of words from the user
def get_word_list(word_type):
    word_list = []
    print(f"Enter {word_type}s (one word per line). Enter 'done' when finished.")
    while True:
        word = input()
        if word.lower() == "done":
            break
        word_list.append(word)
    return word_list


# Function to generate a love letter
def generate_love_letter():
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    adv = random.choice(adverbs)
    verb = random.choice(verbs)
    structure = random.choice(sentence_structures)

    love_letter = structure.format(adj=adj, noun=noun, adv=adv, verb=verb)
    return love_letter


# Main program
if __name__ == "__main__":
    print("Welcome to the Love Letter Generator!")
    print("Please enter some words to be used in the love letter:")
    print()
    adjectives = get_word_list("Adjective")
    nouns = get_word_list("Noun")
    adverbs = get_word_list("Adverb")
    verbs = get_word_list("Verb")

    sentence_structures = [
        "You are {adj}, {adj}, and {adj} {noun} that {adv} {verb} my life.",
        "There are no words to describe how {adj} you are to me.",
        "With every breath I take, I {verb} you with all my {noun}.",
        "My {noun} for you is {adj} and {adj}, like a {noun} that never fades.",
    ]

    print()
    print("Generating your love letter...")
    print("Here's your Love Letter:")
    print(generate_love_letter())
