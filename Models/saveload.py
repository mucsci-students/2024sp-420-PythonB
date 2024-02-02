import os
import json


class SaveLoad:

    @staticmethod
    def save():

        test_data = {
            "contacts": [
                {
                    "id": 1,
                    "name": "John Doe",
                    "email": "johndoe@example.com",
                    "phone": "555-1234",
                    "tags": ["friend", "colleague"]
                },
                {
                    "id": 2,
                    "name": "Jane Smith",
                    "email": "janesmith@example.com",
                    "phone": "555-5678",
                    "tags": ["family"]
                }
            ],
            "products": [
                {
                    "id": 101,
                    "name": "Widget",
                    "price": 19.99,
                    "in_stock": True
                },
                {
                    "id": 102,
                    "name": "Gadget",
                    "price": 29.99,
                    "in_stock": False
                }
            ]
        }
        # Patrick : Once we have the ability to convert the Diagram to a JSON text format,
        # Patrick : this test data will be removed.
        save_folder = 'save_folder'

        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
            # Patrick: Checks if the save_folder already exists
            # Patrick: If not, the os will create the folder at the projects root.

        file_name = input("Enter a valid filename: ") + ".json"

        file_path = os.path.join(save_folder, file_name)

        name_exists = True
        # Patrick: This will be replaced with os.path.exists(file_name).
        # Patrick: This is in place, so we can easily test.

        print("Filename : " + file_name)
        if name_exists:
            overwrite = input(f"The file {file_name} already exists. Do you want to overwrite it? Y/N ")

            if overwrite == 'Y' or overwrite == 'y':
                print(f"Overwriting {file_name}...")

                with open(file_path, 'w') as f:
                    json.dump(test_data, f)
                    # Patrick: test_data will be replaced with proper diagram data once Diagram is complete

            else:
                print(f"Aborting save...")
        else:
            print(f"Saving {file_name}")
            with open(file_path, 'w') as f:
                json.dump(test_data, f)
                # Patrick: test_data will be replaced with proper diagram data once Diagram is complete
