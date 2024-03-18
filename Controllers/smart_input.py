from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter



# Example options
options = ['help', 
           'add class', 'delete class', 'rename class',
            'list class', 'list classes', 'list relationship', 'list relationships' 
            'add field','rename field', 'delete field',
            'add method','delete method','rename method',
            'add parameter', 'delete parameter', 'rename parameter'
            'add relationship', 'delete relationship',
            'save', 'load', 'exit']
completer = WordCompleter(options)

while True:
    user_input = prompt('Enter something: ', completer=completer)
    print('You entered:', user_input)





'''


# Function to detect Tab key presses
def tab_pressed():
    tab_count = 1
    last_tab_time = time.time()
    while True:
        if keyboard.is_pressed('tab'):
            if tab_count == 1:
                print("Attempting to auto suggest")
                tab_count += 1
            elif time.time() - last_tab_time < 0.5 and tab_count > 1:  # Within a 0.5-second window
                print("Attempting to bring list of all possible commands")
                tab_count += 1

            last_tab_time = time.time()
        time.sleep(0.1)  # Adjust sleep time as needed

# Start the thread for detecting Tab key presses
tab_thread = threading.Thread(target=tab_pressed)
tab_thread.daemon = True
tab_thread.start()

text = input("Type Here: ")




class SmartInput:
    def __init__(self, commands: list[str]):
        self.commands = commands
        self.setup()

    def suggest_code(self, partial_command):
        suggestions = []
        for command in self.commands:
            if command.startswith(partial_command):
                suggestions.append(command)
        return suggestions  

    def setup(self):
        keyboard.on_press(self.on_key)

    def on_key(self, event):
        if event.name == "tab":
            print("Tab key pressed!")

# Example usage:
smart_input = SmartInput([])
user_input = input("Enter something: ")

'''
'''
possible_commands = ["print", "input", "if", "for", "while", "def", "class", "import", "return"]
suggester = SmartInput(possible_commands)

partial_command = "i"  # Partial command entered by the user
suggestions = suggester.suggest_code(partial_command)
print("Suggestions based on partial command '{}':".format(partial_command))
for suggestion in suggestions:
    print(suggestion)

'''

