class Text(object):
    """
    One or more lines of text, padded
    with spaces
    """
    def __init__(self, raw_text, pad_char=' '):
        self.text = self.process_text(raw_text, pad_char)
        self.pad_char = pad_char

    def __str__(self):
        """
        |FORMAT THE TEXT  |
        |IN ROWS LIKE THIS|
        """
        return '\n'.join('|{}|'.format(line) for line in self.text)

    def __iter__(self):
        """
        Iterate over the text and generate the row, column and letter
        for all characters that are not spaces
        """
        for i, line in enumerate(self.text):
            for j, letter in enumerate(line):
                if letter != ' ':
                    yield i, j, letter

    def sanitize(self, valid_letters):
        """
        Sanitize the text by converting every non-supported
        character to the pad character
        """
        results = []
        for line in self.text:
            sanitized = ''.join(self.sanitize_line(line, valid_letters))
            results.append(sanitized)
        self.text = results

    def sanitize_line(self, line, valid_letters):
        """
        Go through the letters of a string.
        If they are in valid_letters + {' '}
        yield the letter. Otherwise, yield the pad character
        """
        valid = valid_letters | {' ', self.pad_char}
        for char in line:
            if char in valid:
                yield char
            else:
                yield self.pad_char
            
    @property
    def rows(self):
        """Number of rows in the text"""
        return len(self.text)

    @property
    def cols(self):
        """Number of columns in the text"""
        return len(self.text[0])

    @classmethod
    def process_text(cls, raw_text, pad_char):
        """
        Do the following to the text:

        1. Strip leading/trailing whitespace
        1. Convert the letters to uppercase
        2. Split the string on newlines
        3. Pad each line to the same length
        """
        # Split the text on newlines and make everything uppercase
        lines = raw_text.strip().upper().split('\n')

        # Find the width of the longest line
        max_width = max(len(line) for line in lines)

        # Pad every line to the correct width
        return [line.ljust(max_width, pad_char) for line in lines]
        

    @classmethod
    def from_file(cls, fname):
        """
        Read text from a file
        """
        with open(fname, 'r') as text_file:
            raw_text = text_file.read()
            return cls(raw_text)
