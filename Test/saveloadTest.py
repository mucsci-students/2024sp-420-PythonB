import json
import unittest
from unittest.mock import patch, mock_open
from saveload import SaveLoad


class TestSaveLoad(unittest.TestCase):
    def setUp(self):
        self.sl = SaveLoad()
        self.test_data = {"key": "value"}
        self.file_name = "testfile"
        self.full_path = f"save_folder/{self.file_name}.json"

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists", return_value=False)
    @patch("os.makedirs")
    def test_save_new_file(self, mock_makedirs, mock_exists, mock_open):
        self.sl.save(self.test_data, self.file_name)
        mock_makedirs.assert_called_once_with('save_folder')
        # Pat: Check that the file was opened in write mode
        mock_open.assert_called_once_with(self.full_path, 'w')

        # Pat: Check that the correct data was written
        written_content = "".join(call.args[0] for call in mock_open().write.call_args_list)
        self.assertEqual(written_content, json.dumps(self.test_data))

    @patch("builtins.input", return_value='y')
    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.exists", side_effect=[True, True])  # First for folder, second for file
    def test_save_overwrite_file(self, mock_exists, mock_open, mock_input):
        self.sl.save(self.test_data, self.file_name)
        mock_open.assert_called_once_with(self.full_path, 'w')
        mock_input.assert_called_once_with(f"The file {self.file_name}.json already exists. Do you want to overwrite it? Y/N ")

    @patch("builtins.input", return_value='n')
    @patch("os.path.exists", side_effect=[True, True])
    @patch("builtins.print")
    def test_save_abort_overwrite(self, mock_print, mock_exists, mock_input):
        self.sl.save(self.test_data, self.file_name)
        mock_print.assert_called_with(f"Aborting save...")
        mock_input.assert_called_once()

    @patch("os.path.exists", return_value=True)
    @patch("builtins.open", new_callable=mock_open, read_data=json.dumps({"key": "value"}))
    def test_load_existing_file(self, mock_open, mock_exists):
        sl = SaveLoad()
        file_name = "existing_file.json"

        # Load data from the file
        data = sl.load(file_name)

        # Assertions
        self.assertEqual(data, self.test_data)
        mock_open.assert_called_once_with(f"save_folder/{file_name}", 'r+')

    @patch("os.path.exists", return_value=False)
    @patch("builtins.print")
    def test_load_nonexistent_file(self, mock_print, mock_exists):
        self.sl.load(f"{self.file_name}.json")
        mock_print.assert_called_with("File does not exist!")




