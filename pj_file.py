import pathlib

d = dict()

def file_create():
    existin_file()
    file_name = input("Enter the file name: ")
    p = pathlib.Path('python notes') / file_name
    try:
        if not p.exists():
            with open (p , 'w') as f:
                data = input("Enter the data: ")
                f.write(data)
            print("**FILE CREATED SUCCESSFULLY**")
        else:
            print("File already exists")
    except Exception as er:
        print(f"Exception occured: {er}")

def file_read():
    existin_file()
    file_num = int(input("Enter the file number: "))
    p = pathlib.Path(d[file_num])
    if p.exists():
        with open (p, 'r') as f:
            data = f.read()
            print(data)
    else:
        print("File does not exist")

def file_update():
    existin_file()
    file_num = int(input("Enter the file number: "))
    p = pathlib.Path(d[file_num])
    if p.exists():
        print("Press 1 to change the name of your file")
        print("Press 2 to overwrite content in your file")
        print("Press 3 to append data in your file")
        response = int(input("Enter your choice: "))
        match response:
            case 1:
                new_name = input("Enter the new name of your file: ")
                p.rename(p.parent / new_name)
                print("**FILE RENAMED SUCCESSFULLY**")
            case 2:
                with open (p, 'w') as f:
                    data = input("Enter the data: ")
                    f.write(data)
                    print("**FILE UPDATED SUCCESSFULLY**")
            case 3:
                with open (p, 'a') as f:
                    data = input("Enter the data: ")
                    f.write(data)
                    print("**Changes Saved**")
            case _:
                print("Invalid choice.")
    else:
        print("File does not exist")

def file_delete():
    existin_file()
    file_num = int(input("Enter the file number: "))
    p = pathlib.Path(d[file_num])
    if p.exists():
        p.unlink() # Deletes file
        print("**FILE DELETED SUCCESSFULLY**")
    else:
        print("File does not exist")

def existin_file():
    path = pathlib.Path('python notes')
    path.mkdir(exist_ok=True)  # Ensure the folder exists
    items = list(path.rglob('*')) # List of the files in the folder
    for i, item in enumerate(items):
        print(f"{i+1} : {item}")
        d[i+1] = item

print("Press 1 for creating file")
print("Press 2 for reading file")
print("Press 3 for updating file")
print("Press 4 for deleting file")
response = int(input("Enter your choice: "))

match response:
    case 1:
        file_create()
    case 2:
        file_read()
    case 3:
        file_update()
    case 4:
        file_delete()
    case _:
        print("Invalid choice.")

    