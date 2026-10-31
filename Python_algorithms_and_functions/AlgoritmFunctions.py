from collections import Counter


def spaghetti_sort(input_sort):
    """Sort the list using spaghetti sort"""
    r = []
    while input_sort:
        m = max(input_sort)
        input_sort.remove(m)
        r.insert(0, m)
    return r


def patience_sort(input_list):
    p, r = [], []
    for x in input_list:
        for s in p:
            if s[-1] > x:
                s.append(x)
                break
        else:
            p.append([x])
    while p:
        s = min(p, key=lambda s: s[-1])
        r.append(s.pop())
        if not s:
            p.remove(s)
    return r


def check_anagram_string(num1: str, num2: str) -> bool:
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


def is_anagram(s1: str, s2: str) -> bool:
    clean = lambda s: "".join(s.split()).lower()
    return Counter(clean(s1)) == Counter(clean(s2))


def main():
    random_list = [45, 2, 15, 78, 2, 10]
    print("patience sort algorithm:", patience_sort(random_list))
    print("spaghetti sort algorithm:", spaghetti_sort(random_list))

    print(check_anagram_string("johnny deep", "peed honnyj"))
    print(check_anagram_string("rac", "car"))
    print(check_anagram_string("listen", "sitent"))
    print(is_anagram("flower power", " reowp owerfl"))
    print(is_anagram("flower power", " reowp oeprfl"))


if __name__ == '__main__':
    main()
