import data_gathering

def main():
    try:
        gathered_data = data_gathering.get_data_from_file('data_files/data.json')
        # gathered_data = data_gathering.get_data_from_api('data_files/input.json')
    except:
        exit("something went wrong, check logs file")

    data_gathering.save_to_file('data.json', data=gathered_data)
    

if __name__ == "__main__":
    main()
