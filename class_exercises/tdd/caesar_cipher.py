def caesar_cipher(p_message,p_shift):
    if p_shift > 26:
        p_shift = p_shift % 26
    elif p_shift < -26:
        p_shift = p_shift % 26
    coded_message = ""
    for letter in p_message:
        if letter.lower() in "abcdefghijklmnopqwstuvwxyz":
            num = ord(letter.lower())
            num = num + p_shift
            if num > ord("z"):
                num = num - 26
            elif num < ord("a"):
                num = num + 26
            char = chr(num)
            if letter.isupper():
                coded_message = coded_message + char.upper()
            else:
                coded_message = coded_message + char
        else:
            coded_message = coded_message + letter
    return coded_message

if __name__ == '__main__':
    print(caesar_cipher("HelLo",3))