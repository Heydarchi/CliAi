import sys


class FileWriter:
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def write_file(file_path, content):
        return open(file_path, "w+").write(content)

    @staticmethod
    def write_file_append(file_path, content):
        return open(file_path, "a+").write(content)

    @staticmethod
    def write_list_to_file(file_path, list_of_str):
        return open(file_path, "w+").write("\n".join(list_of_str))


if __name__ == "__main__":
    print(sys.argv)
    fileWriter = FileWriter
    print(fileWriter.write_file(sys.argv[1], "Yohoooooooooooo"))
    listOfStr = []
    listOfStr.append("Haha")
    listOfStr.append("Hehe")
    listOfStr.append("Hoho")
    print(fileWriter.write_list_to_file(sys.argv[1] + "_1", listOfStr))
