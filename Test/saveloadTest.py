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

