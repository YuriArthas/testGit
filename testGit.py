import os
import inspect
import string


class Object(object):
    pass


class SSS(object):
    def __del__(self):
        print("__del__")

class SCOPE(object):
    step=4
    oriOffset=0
    stepCount=0

    @staticmethod
    def getOffset():
        return SCOPE.oriOffset+SCOPE.step*SCOPE.stepCount

    @staticmethod
    def getFuncName():
        return  inspect.stack()[2][3]

    def __init__(self):
        funcName=SCOPE.getFuncName()
        offset=SCOPE.getOffset()

        self.offsetStr=string.ljust('',offset,' ')
        funcStr=self.offsetStr+funcName
        print(funcStr)
        leftBraceStr=self.offsetStr+'{'
        print(leftBraceStr)
        SCOPE.stepCount+=1


    def __del__(self):
        SCOPE.stepCount-=1
        print(self.offsetStr+'}')



def func():
    s=SCOPE()



def main():
    s=SCOPE()

    func()


main();