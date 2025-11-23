import string


def clean(str: str) -> str:
    if len(str) == 0:
        return ""
    else:
        first_chr = str[0]
        rest_str = clean(str[1:])
        if first_chr in string.punctuation + string.whitespace:
            return rest_str
        else:
            return first_chr + rest_str


if __name__ == '__main__':
    print(clean('The big elephant'))
    print(clean("--A man, a plan, a canal: Panama!"))
    print(clean("One"))
    print(clean(""))
