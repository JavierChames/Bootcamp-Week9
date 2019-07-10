# def count(quote, vowels):

    # return [i for i, current_char_of_string in enumerate(quote) if current_char_of_string in vowels ]

    # location = 0
    # result = []
    # tmp = 0
    # for character in quote:
    #     if character in vowels:
    #         result.append(tmp)
    #     tmp += 1
    # return result


quote = "some people drink from the fountain of knowledge, others just gargle."
vowels = "aeiou"
print([i for i, current_char_of_string in enumerate(quote) if current_char_of_string in vowels ])
