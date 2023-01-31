#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return 0, None
    else:
        len_str = len(sentence)
        first_chr = sentence[0]
        return len_str, first_chr
