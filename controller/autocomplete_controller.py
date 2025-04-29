from service.autocomplete_service import AutocompleteService

class AutocompleteController:
    def __init__(self):
        self.service = AutocompleteService()

    def add_word(self, word):
        self.service.insert(word)

    def get_suggestions(self, prefix):
        return self.service.get_suggestions(prefix)
