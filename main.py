def main():
    print("--- Being report of books/frankenstein.txt ---")
    print(f"{count_words(file_contents)} word were found in the document")

    char_count = count_char(file_contents)
    sorted_char_count = dict(sorted(char_count.items())) 
    #print(type(char_count))
    for k,v in sorted_char_count.items():
        print(f"The '{k}' character was found {v} times")

def count_char(text):
    freq = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char.isalpha() == True:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
    return freq

def count_words(text):
    l = text.split()
    return len(l)

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    
main()
