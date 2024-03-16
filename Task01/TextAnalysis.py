import re
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def analyze_text(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    # Number of Words
    words = re.findall(r'\w+', text)
    num_words = len(words)

    # Unique Words
    unique_words = set(words)
    num_unique_words = len(unique_words)

    # Most Frequent Word
    word_counts = Counter(words)
    most_frequent_word = word_counts.most_common(1)[0][0]

    # Average Word Length
    total_word_length = sum(len(word) for word in words)
    avg_word_length = total_word_length / num_words

    # Number of Sentences
    sentences = re.split(r'[.!?]', text)
    num_sentences = len(sentences)

    # Longest Sentence
    longest_sentence = max(sentences, key=lambda x: len(x.split()))

    # Shortest Sentence
    shortest_sentence = min(sentences, key=lambda x: len(x.split()))

    # Percentage of Uppercase Letters
    total_letters = sum(c.isalpha() for c in text)
    uppercase_letters = sum(c.isupper() for c in text)
    percentage_uppercase = (uppercase_letters / total_letters) * 100 if total_letters > 0 else 0

    # List 5 Most Frequent Bigrams
    words_lower = [word.lower() for word in words]
    bigrams = [tuple(words_lower[i:i+2]) for i in range(len(words_lower)-1)]
    most_frequent_bigrams = Counter(bigrams).most_common(5)

    # Word Cloud Generation
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    # Output
    output = {
        "Number of Words": num_words,
        "Unique Words": num_unique_words,
        "Most Frequent Word": most_frequent_word,
        "Average Word Length": avg_word_length,
        "Number of Sentences": num_sentences,
        "Longest Sentence": longest_sentence,
        "Shortest Sentence": shortest_sentence,
        "Percentage of Uppercase Letters": percentage_uppercase,
        "List 5 Most Frequent Bigrams": most_frequent_bigrams
    }

    # Plot Word Cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig('wordcloud.png')

    return output

file_path = 'E:\delete_now\hack\Cypher 2.0 - Hackathon Pre-Round\Cypher-2.0---Hackathon-Pre-Round\Task01\scan.txt' 
output = analyze_text(file_path)
print(output)