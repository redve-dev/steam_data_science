import unittest
from data_getter import data_getter

class tests(unittest.TestCase):
    def test_invalid_input_file(self):
        self.assertRaises(OSError, data_getter, input_file='this_path_doesnt_exist.json')

    def test_write_to_file_without_permissions(self):
        d = data_getter(input_file='', LoadFromFile=True, data_path='data_files/data.json')
        self.assertRaises(PermissionError, d.save_to_file, path='no_permissions_to_write/data.json')

    def test_reading_invalid_data_file(self):
        self.assertRaises(OSError, data_getter,input_file='', LoadFromFile=True, data_path='this_file_does_not_exist')

def main():
    unittest.main()

if __name__ == "__main__":
    main()
