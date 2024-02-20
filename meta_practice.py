def solution(text, width):
    split_text = text.split()
    char_counts = []
    output = ['*************']
    for val in split_text:
        char_counts.append(len(val))

    print(split_text)
    print(char_counts)

    i = 0
    prev_word = None
    current_line = ''
    counter = width
    while i > 0:
        current_word = split_text[i]

        # handle end of sentence/new sentence
        if prev_word is None or prev_word[-1] in ['.', '?', '!']:
            current_line = current_line + '  '

        # add word
        if len(current_word) <= counter:
            current_line = current_line + current_word
            counter -= len(val)
            prev_word = val
            i += 1

        # add space ahead of next word on new line
        elif len(val) > counter:
            while counter > 0:
                current_line = current_line + ' '
                counter = - 1

        # new line, add current line to output
        if counter <= 0:
            output.append(current_line)
            current_line = ''
            counter = width

    return output


text = "Hi! This is the article you have to format properly. Could you do that for me, please?"
width = 16

print(solution(text,width))