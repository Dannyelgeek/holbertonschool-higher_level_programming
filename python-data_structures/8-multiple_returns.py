#!/usr/bin/python3
def multiple_returns(sentence):
    len_str = len(sentence)
    first_chr = sentence[0]
    if sentence[0] == "":
        return len_str, None
    else:
        return len_str, first_chr 