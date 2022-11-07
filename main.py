import data_getter

def main():
    try:
        d=data_getter.data_getter('data_files/input.json', True, 'data_files/data.json')
        print(d)
    except:
        exit("something went wrong, check logs file")

    d.save_to_file('no_permissions_to_write')
    

if __name__ == "__main__":
    main()
