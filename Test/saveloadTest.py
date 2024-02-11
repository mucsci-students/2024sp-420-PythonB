from unittest import TestCase, mock
from Models.saveload import SaveLoad


class TestSaveLoad(TestCase):
    @mock.patch('os.makedirs')
    @mock.patch('os.path.exists')
    @mock.patch('builtins.input', return_value='testfile2')
    def test_save_creates_folder_if_not_exists(self, mock_input, mock_exists, mock_makedirs):
        mock_exists.side_effect = [False, True]
        with mock.patch('os.makedirs') as mock_makedirs:
            SaveLoad.save()
            mock_makedirs.assert_called_with('save_folder')

    # Patrick : If save folder does not exist, assert that 'os.makedirs' is called
    @mock.patch('os.makedirs')
    @mock.patch('os.path.exists')
    @mock.patch('builtins.input', return_value='testfile')
    def test_save_does_not_create_folder_if_exists(self, mock_input, mock_exists, mock_makedirs):
        mock_exists.side_effect = [True, False]
        with mock.patch('os.makedirs') as mock_makedirs:
            SaveLoad.save()
            mock_makedirs.assert_not_called()
# Patrick : If folder exists, assert "os.makedirs" is not called.

    @mock.patch('os.path.exists', return_value=True)  # Simulates that the file already exists
    @mock.patch('builtins.input',
                side_effect=['testfile', 'y'])  # Simulates user input for filename and overwrite confirmation
    def test_save_overwrites_if_user_confirms(self, mock_input, mock_exists):
        SaveLoad.save()
        # Assertions to verify the correct behavior
        # Verify the user was prompted for a filename and then for overwrite confirmation
        expected_calls = [mock.call("Enter a valid filename: "),
                          mock.call("The file testfile.json already exists. Do you want to overwrite it? Y/N ")]
        mock_input.assert_has_calls(expected_calls, any_order=False)


