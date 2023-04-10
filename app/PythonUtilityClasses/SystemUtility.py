import os
import subprocess
from dataclasses import dataclass


@dataclass
class FileInfo:
    name: str = ""
    size: int = 0
    last_modifies: str = ""
    created: str = ""
    md5: str = ""


class SystemUtility:
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def get_list_of_files(path, pattern):
        result = subprocess.Popen(
            ["find", path, "-name", pattern], stdout=subprocess.PIPE
        ).communicate()[0]
        result = str(result, encoding="utf-8").split("\n")
        result = [item for item in result if item]
        return result

    @staticmethod
    def get_file_info(path):
        file_info = FileInfo()
        file_info.name = path
        file_info.size = os.path.getsize(path)
        file_info.last_modifies = os.path.getmtime(path)
        file_info.created = os.path.getctime(path)
        return file_info

    @staticmethod
    def delete_files(path):
        os.remove(path)


if __name__ == "__main__":
    sysUtil = SystemUtility()
    print(sysUtil.get_list_of_files("./test", "*_contexts"))
    print(sysUtil.get_list_of_files("./test", "*.te"))
