try:
    with open('my_file.txt') as mf:
        file_data = mf.read()
    print(file_data)
except FileNotFoundError:
    print('File not found!')
except PermissionError:
    print("Do not open!")
except Exception as err:
    print('Processing of any exceptions',str(err))