
def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()

        words = word_count(file_contents)
        char_dict = char_count(file_contents)

        print(book_report(char_dict, words))
        

def word_count(text):
    count = 0
    words = text.split()
    for word in words:
        count += 1
    return count

def char_count(text):
    chars_present = {}

    for char in text.lower():
        if char in chars_present:
            chars_present[char] += 1
        else:
            chars_present[char] = 1
    return chars_present

def book_report(char_dict, words):
    sorted_dict = sorted(convert_dict_to_list(char_dict), reverse=True, key=sort_on)
    
    report = ["--- Begin report of books/frankenstein.txt ---"]
    report.append(f"{words} words found in the document")

    for item in sorted_dict:
        if item["char"].isalpha():
            report.append(f"The '{item["char"]}' character was found {item["count"]} times")

    report.append("--- End report ---")
    return report

def convert_dict_to_list(dict):
    converted_dict = []

    for k,v in dict.items():
        converted_dict.append({"char" : k, "count" : v})
    return converted_dict

def sort_on(dict):
    return dict["count"]

main()