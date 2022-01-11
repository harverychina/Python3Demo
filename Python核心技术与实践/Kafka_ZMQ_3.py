# -*- coding:utf8 -*-
# @Time：2022/1/11 9:17 AM
# @Author： Huang Jeff

import time
import zmq


def run():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:6666")
    socket.setsockopt_string(zmq.SUBSCRIBE, '')

    cnt = 1

    while True:
        time.sleep(1)
        socket.send_string("server cnt {}".format(cnt))
        print("send {}".format(cnt))
        cnt += 1


if __name__ == "__main__":
    run()
