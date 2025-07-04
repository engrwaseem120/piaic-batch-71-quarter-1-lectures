def copy_image(source_path, destination_path):
    try:
        with open(source_path, 'rb') as source_file:
            with open(destination_path, 'wb') as destination_file:
                while True:
                    chunk = source_file.read(1024)
                    if not chunk:
                        break
                    destination_file.write(chunk)
        print(f"Image copied successfully from '{source_path}' to '{destination_path}'")

    except FileNotFoundError:
        print(f"Error: Source file '{source_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

copy_image("testimage.jpg", "copy_testimage.jpg")