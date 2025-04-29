from model.trie_node import TrieNode

class AutocompleteService:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word.lower():
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end_of_word = True
        node.frequency += 1

    def get_suggestions(self, prefix):
        node = self.root
        for ch in prefix.lower():
            if ch not in node.children:
                return []
            node = node.children[ch]

        suggestions = []

        def dfs(current_node, path):
            if current_node.is_end_of_word:
                suggestions.append((path, current_node.frequency))
            for ch, next_node in current_node.children.items():
                dfs(next_node, path + ch)

        dfs(node, prefix.lower())
        suggestions.sort(key=lambda x: (-x[1], x[0]))
        return [word for word, _ in suggestions]
