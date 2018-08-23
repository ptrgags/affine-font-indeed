def process_text(raw_text):
    """
    Given raw text (e.g. from a file)
    split on newlines so we have an array
    of lines of text
    """
    return raw_text.strip().split('\n')

def all_upper(text):
    """
    Make every line of text in an array uppercase
    """
    return [line.upper() for line in text]

def pad_input(text):
    """
    Pad all strings in an array so they are the same length,
    justified left.
    """
    width = max(len(line) for line in text)
    return [line.ljust(width) for line in text]

def display_text(text):
    """
    Display each line of text with vertical bars around it
    to denote the size of the text
    """
    for line in text:
        print '|{}|'.format(line)

raw = """
Hello World
My Name is Peter
This is a fractal
"""

display_text(pad_input(all_upper(process_text(raw))))
