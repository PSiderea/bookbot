import sys
import stats

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
             
file_path = sys.argv[1]
with open(file_path, "r") as f:
    contents = f.read()



word_count = stats.get_word_count(contents)
char_count = stats.return_character_count(contents)
sorted_chars = stats.sort_chars_by_count(char_count)


def main():
    print("=============  BOOKBOT =============")
    print(f"Analyzing book found at {file_path}...")
    
    print("------------ Word Count ------------")
    print(f"Found {word_count} total words")
    print("--------- Character Count ----------")
    for char_dict in sorted_chars:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['count']}")

    print("=================== END =============")


main()

