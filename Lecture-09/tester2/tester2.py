def create_and_write_file(filename, text):
    with open(filename, "a") as file:
        file.write(text)

def main():
    print("Hello")
    create_and_write_file("tester2file.txt", "\nThis is a testing text to check if we are able to write data in file")

if __name__ == "__main__":
    main()