"""Translate a word into pig-latin"""

VOWELS = ["a", "e", "i", "o", "u"]


def main():
    """
    Get the user input and print the translated word.

    :return:
    """

    word_to_translate = input("Please enter a word to translate.\n")
    output = translate(word_to_translate)
    print(output)


def translate(word_to_translate):
    """
    Perform the translation into pig latin

    :param word_to_translate: The word to translate
    :return: The translated word.
    """
    for vowel in VOWELS:
        if word_to_translate.lower().startswith(vowel):
            return word_to_translate[1:] + word_to_translate[0] + "way"

    return f"{word_to_translate[1:]}{word_to_translate[0]}ay"


if __name__ == '__main__':
    main()
