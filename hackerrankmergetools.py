def merge_the_tools(stri, k):

    while stri:
        si = stri[0:k]
        seen = ''
        for c in si:
            if c not in seen:
                seen += c
        print(seen)
        stri = stri[k:]


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
