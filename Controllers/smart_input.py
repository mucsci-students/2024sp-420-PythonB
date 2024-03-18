from prompt_toolkit import prompt
from prompt_toolkit.completion import NestedCompleter

completer = NestedCompleter.from_nested_dict({
    'add': {
        'class': None,
        'field': None,
        'method': None,
        'relationship': None
    },
    'delete': {
        'class': None,
        'field': None,
        'method': None,
        'relationship': None
    },
    'rename':{
        'class': None,
        'field': None,
        'method': None
    },
    'list':{
        'class': None,
        'classes': None,
        'relationship': None,
        'relationships': None
    },
    'save': None,
    'load': None,
    'exit': None
    })
text = prompt('>', completer=completer)

