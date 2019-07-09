def count(quote, vowels):

    final = [each for each in quote if each in vowels]
    mylist = [
        i for i, current_char_of_string in enumerate(quote)
        if current_char_of_string in vowels
    ]
    return (mylist)

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
print(count(quote, vowels))
