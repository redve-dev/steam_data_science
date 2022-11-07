from data_getter import data_getter

def main():
    try:
        gathered_data = data_getter(input_file='data_files/input.json', LoadFromFile=False, data_path='data_files/data.json')
        # print(gathered_data)
    except:
        exit("something went wrong, check logs file")

    gathered_data.save_to_file('tf2_data.json')
    

if __name__ == "__main__":
    main()
