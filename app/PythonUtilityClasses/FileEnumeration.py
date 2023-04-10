from SystemUtility import *


class FileEnumeration:
    def __init__(self, path) -> None:
        self.path = path
        self.list_contexts = []
        self.list_te_files = []
        self.enumerate_policy_files(self.path)

    def enumerate_policy_files(self, path):
        self.list_contexts = SystemUtility.get_list_of_files("./test", "*_contexts")
        self.list_te_files = SystemUtility.get_list_of_files("./test", "*.te")


if __name__ == "__main__":
    fl_enum = FileEnumeration(".")
    print("-- List of *_contexts files:")
    print(fl_enum.list_contexts)
    print("-- List of *.te files:")
    print(fl_enum.list_te_files)
