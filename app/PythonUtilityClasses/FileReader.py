import sys


class FileReader:
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def read_file(file_path):
        return open(file_path).read()

    @staticmethod
    def read_file_lines(file_path):
        return open(file_path).readlines()

    @staticmethod
    def remove_comments(lines):
        filtered_lines = []
        for line in lines:
            if "#" in line:
                _str = line[0 : line.index("#")].strip()
                if len(_str):
                    filtered_lines.append(_str + "\n")
            else:
                filtered_lines.append(line)
        return filtered_lines


if __name__ == "__main__":
    print(sys.argv)
    fileReader = FileReader()
    print(fileReader.read_file(sys.argv[1]))
