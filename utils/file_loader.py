def load_words_from_file(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]
