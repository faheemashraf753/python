import os

def list_directory_contents(path='/'):
    """
    Print all files and directories in the given path.
    
    :param path: the directory path to list. Defaults to current directory.
    """
    try:
        entries = os.listdir(path)
        print(f"Contents of directory '{path}':")
        for entry in entries:
            print(entry)
    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied accessing '{path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage: list contents of current directory
    list_directory_contents()
    # Or specify another path:
    # list_directory_contents('/path/to/directory')
