# coding:utf8

# with的用法和类的写法

class TestWith():
    def __enter__(self):
        print("run")

    def __exit__(self, exc_type, exc_val, exc_tb):
        # print("exit")
        if exc_tb is None:
            print("正常结束")
        else:
            print("has error %s" % exc_tb)

# 异常检查手段 with
with TestWith():
    print("Test is running")
    raise NameError('test')
