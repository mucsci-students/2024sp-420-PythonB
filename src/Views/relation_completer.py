"""
This module contains a custom completer class for generating completion suggestions
for relation types in a document.

The RelationCompleter class provides completion suggestions for relation types such
as "aggregation", "composition", "generalization", and "inheritance" based on the
context of the input text.
"""

from prompt_toolkit.completion import Completer, Completion

class RelationCompleter(Completer):
    def get_completions(self, document, complete_event):
        """
        Generate completion suggestions based on the current document.

        Args:
            document (Document): The document representing the current input text.
            complete_event: The event that triggered the completion.

        Yields:
            Completion: A completion suggestion based on the input.
        """
        words = document.text.split()
        relations = ["aggregation", "composition", "realization", "inheritance"]
        # Suggestions for space with no other values
        if len(words) == 2 and document.text_before_cursor.endswith(' '):
            for relation in relations:
                yield Completion(relation, start_position=0)
        # Suggestion for 3rd input with values already entered
        if len(words) == 3 and not document.text_before_cursor.endswith(' '):
            for relation in relations:
                # Autocompletion for partialy completed words
                if relation.startswith(words[2]) and relation != words[2]:
                    yield Completion(relation, start_position=-len(words[2]))
