
def check_anagram_string(num1, num2):
    """Unify the words in one string"""
    num1 = "".join(num1.split())
    num2 = "".join(num2.split())
    """Count the frequency of the letters in the string"""
    count = {}

    for letter in num1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in num2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False
    return True


def main():
    print(check_anagram_string("johny deep", "peed honyj"))
    print(check_anagram_string("rac", "car"))


if __name__ == '__main__':
    main()

