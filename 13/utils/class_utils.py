# coding:utf-8
# 第13课 Python模块化

def ddd():
    pass

class Encoder(object):
    def encode(self, s):
        return s[::-1]


class Decoder(object):
    def decode(self, s):
        return ' '.join(reversed(list(s)))
