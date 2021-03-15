class block:
    def __init__(self,grid):
        self.grid = grid
    def getmissingvalue(self):
        value = (1+16)*8
        for row in self.grid:
            for num in row:
                if num!='?':
                    value -= int(num)
        return value

def playwithsixteen(matrix):
    misvalue = block(matrix)
    print(misvalue.grid)
    print(misvalue.getmissingvalue())






start =[['1', '2', '3', '4'], ['5', '6', '7', '8'], ['9', '10', '11', '12'], ['13', '?', '15', '16']]
playwithsixteen(start)

