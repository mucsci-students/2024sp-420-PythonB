from prompt_toolkit.completion import Completer, Completion

class RelationCompleter(Completer):
    def get_completions(self, document, complete_event):
        words = document.text.split()
        #print(len(words))
        # Check if there are at least two words in the input
        if len(words) == 2 and document.text_before_cursor.endswith(' '):
            # Yield multiple Completion objects for multiple words
            yield Completion('word1', start_position=0)
            yield Completion('word2', start_position=0)
            yield Completion('word3', start_position=0)
