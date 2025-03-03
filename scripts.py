import os
from collections import Counter
import socket

# Function to count words in a file
def count_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        words = text.split()
        return len(words)

# Function to find top 3 frequent words
def top_3_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        words = text.split()
        word_counts = Counter(words)
        return word_counts.most_common(3)

# Function to handle contractions
def handle_contractions(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        words = text.replace("'", " ").split()
        word_counts = Counter(words)
        return word_counts.most_common(3)

# Function to get the IP address
def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

# Main script logic
if __name__ == "__main__":
    # Define file paths
    file1 = "/home/data/IF-1.txt"
    file2 = "/home/data/AlwaysRememberUsThisWay-1.txt"

    # Count words in each file
    word_count1 = count_words(file1)
    word_count2 = count_words(file2)
    grand_total = word_count1 + word_count2

    # Find top 3 words in IF-1.txt
    top3_if1 = top_3_words(file1)

    # Handle contractions and find top 3 words in AlwaysRememberUsThisWay-1.txt
    top3_always = handle_contractions(file2)

    # Get the IP address
    ip_address = get_ip_address()

    # Write results to result.txt
    output_dir = "/home/data/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(f"{output_dir}/result.txt", "w") as result_file:
        result_file.write(f"Word count in IF-1.txt: {word_count1}\n")
        result_file.write(f"Word count in AlwaysRememberUsThisWay-1.txt: {word_count2}\n")
        result_file.write(f"Grand total word count: {grand_total}\n")
        result_file.write(f"Top 3 words in IF-1.txt: {top3_if1}\n")
        result_file.write(f"Top 3 words in AlwaysRememberUsThisWay-1.txt (after handling contractions): {top3_always}\n")
        result_file.write(f"IP address of the container: {ip_address}\n")

    # Print the contents of result.txt to the console
    with open(f"{output_dir}/result.txt", "r") as result_file:
        print(result_file.read())