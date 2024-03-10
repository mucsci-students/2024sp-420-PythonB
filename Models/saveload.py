import os
import json


class SaveLoad:

    def save(self, data, file_name):
        """
            Save data to a .json file in a folder 'saves_folder'
            :param data : The data to be saved into the .json file.
            :param file_name: The name of the file the user would like to save.

            Preconditions:
            'file_name' must be a valid file name.

            Post-Conditions:
            If saves_folder did not exist, it is created.
            a .json file named 'file_name' will be within saves_folder

            Raises:
            File Overwrite
            Invalid file name



        """
        save_folder = 'save_folder'

        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
            # Patrick: Checks if the save_folder already exists
            # Patrick: If not, the os will create the folder at the projects root.

        file_name = str(file_name + ".json")

        file_path = os.path.join(save_folder, file_name)

        name_exists = os.path.exists(file_path)

        return("Filename : " + file_name)
        if name_exists:
            overwrite = input(f"The file '{file_name}' already exists. Do you want to overwrite it? Y/N ").lower()

            if overwrite == 'y':
                return(f"Overwriting '{file_name}'...")
        else:
            return(f"Saving '{file_name}'")

        with open(file_path, 'w') as f:
            # Ensure json.dump() uses the indent parameter for nicely formatted JSON
            json.dump(data, f, indent=2)

        if name_exists and overwrite != 'y':
            return(f"Aborting save...")
        else:
            return(f"Saving '{file_name}'")
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=2)
                # Patrick: test_data will be replaced with proper diagram data once Diagram is complete

    def load(self, file_name):
        """
        Load a .json file from 'saves_folder' to be viewed/edited.

        :param file_name: The name of the file to be loaded.
        :return data: the loaded data from the desired .json file.

        Pre-conditions:
        'file_name' must be a valid file name
        'file_name' must exist in saves_folder

        Post-Conditions:
        'file_name' is loaded and the current data is printed.
        data is returned.

        """
        save_folder = 'save_folder'
        # Patrick : Makes method aware of the save folder
        
        file_name = str(file_name + ".json")

        file_path = os.path.join(save_folder, file_name)
        file_exists = os.path.exists(file_path)
        if file_exists:
            # Patrick: If file exists, open the file
            with open(file_path, 'r+') as file:
                # Read the content
                data = json.load(file)

                return data
        else:
            # Patrick: If file does not exist, alert user
            raise ValueError ("File does not exist!")
            return None




