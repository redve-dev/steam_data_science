import data_getter

def main():
    try:
        d=data_getter.data_getter('data_files/input.json', True, 'data_files/data.json')
        print(d)
    except:
        print("something went wrong, check logs file")
    

if __name__ == "__main__":
    main()
