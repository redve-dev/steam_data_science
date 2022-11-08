from data_gathering import get_data_from_api, get_data_from_file, save_to_file

def main():
    try:
        gathered_data = get_data_from_file('data_files/data.json')
        # gathered_data = get_data_from_api('data_files/input.json')
    except:
        exit("something went wrong, check logs file")

    save_to_file('data.json', data=gathered_data)
    

if __name__ == "__main__":
    main()
