def text_to_file(filename, text):
    f_out = open(filename, "w")
    f_out.write(text)
    f_out.close()


def string_reverse(text):
    return text[::-1]
