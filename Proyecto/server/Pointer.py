class Pointer:

    def __init__(self):
        self.index = self.readIndex()

    def nextIndex(self):
        if self.index == 3:
            self.index = 1
        else:
            self.index = self.index + 1

    def readIndex(self):
        with open("pointerstatus.txt", encoding = 'utf-8') as f:       
            index = int(f.read(1))
            f.close()
        return index

    def writeIndex(self):
        with open("pointerstatus.txt",'w', encoding = 'utf-8') as f:       
            f.write(str(self.index))
            f.close()

     