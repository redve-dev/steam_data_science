import unittest
import data_gathering

class tests(unittest.TestCase):
    def test_invalid_input_file(self):
        self.assertRaises(OSError, data_gathering.get_data_from_api, input_file='this_file_does_not_exist')

    def test_write_to_file_without_permissions(self):
        self.assertRaises(PermissionError, data_gathering.save_to_file, path='no_permissions_to_write/data.json', data='{"random":"json"}')

    def test_reading_invalid_data_file(self):
        self.assertRaises(OSError, data_gathering.get_data_from_file, path='this_file_does_not_exist')

def main():
    unittest.main()

if __name__ == "__main__":
    main()
