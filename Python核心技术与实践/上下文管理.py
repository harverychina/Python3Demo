# -*- coding:utf8 -*-
# @Time：2022/1/4 9:32 AM
# @Author： Huang Jeff

class FileManager:
    def __init__(self, name, mode):
        print("__init__")
        self.name = name
        self.mode = mode

    def __enter__(self):
        print("enter")
        self.file = open(self.name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")
        if self.file:
            self.file.close()


if __name__ == "__main__":
    for i in range(10000):
        with open("test.txt", "w") as f:
            f.write("hello")

    with FileManager("text.txt", "w") as f:
        print("准备写文件")
        f.write("hello 2")
