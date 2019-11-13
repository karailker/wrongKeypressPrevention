def main():
    keystroke=str(input("Bir tuşa basınız: "))
    while(keystroke != '0'):
        print(findPos(keystroke))
        print(possibilities(findPos(keystroke)))
        keystroke = str(input("Bir tuşa basınız: "))

class Keyboard:

    def __init__(self, param=None):
        if type(param) == str:
            if param == "turkishq":
                self.layout = [
                    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'ğ', 'ü'],
                    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ş', 'i'],
                    ['z', 'x', 'c', 'v', 'b', 'n', 'm', 'ö', 'ç']
                ]
        elif type(param) == list:
            self.layout = list
        elif param is None:
            self.layout = [
                ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
                ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
                ['z', 'x', 'c', 'v', 'b', 'n', 'm']
            ]

def findPos(keystroke):

    # keyboard = Keyboard('turkishq')
    keyboard = Keyboard()

    for i in range(len(keyboard.layout)):
        for j in range(len(keyboard.layout[i])):
            # print(type(englishKeyboardLayout[i][j]))
            if keyboard.layout[i][j] == keystroke:
                return i, j

def possibilities(position):

    pos=[]

    matrix=[]

    i = position[0]
    j = position[1]

    # keyboard = Keyboard('turkishq')
    keyboard = Keyboard()

    print(len(keyboard.layout[i]))

    # if i-1 >= 0 and j-1 > 0:
    #     pos.append(keyboard.layout[i-1][j-1])
    #
    # if i-1 >= 0:
    #     pos.append(keyboard.layout[i-1][j])
    #
    # if i-1 >= 0 and j+1 < len(keyboard.layout[i]):
    #     pos.append(keyboard.layout[i-1][j+1])
    #
    # if j-1 >= 0:
    #     pos.append(keyboard.layout[i][j-1])
    #
    # if i+1 < len(keyboard.layout) and j-1 >= 0:
    #     pos.append(keyboard.layout[i+1][j-1])
    #
    # if i+1 < len(keyboard.layout):
    #     pos.append(keyboard.layout[i+1][j])
    #
    # if j+1 < len(keyboard.layout[i]):
    #     pos.append(keyboard.layout[i][j+1])
    #
    # if i+1 < len(keyboard.layout) and j+1 < len(keyboard.layout[i]):
    #     pos.append(keyboard.layout[i+1][j+1])

    x=i-1
    while(x<i+2):
        y=j-1
        while(y<j+2):
            if x>=0 and x<3 and y>=0:
                matrix.append((x,y))
                try:
                    pos.append(keyboard.layout[x][y])
                except:
                    pass #outofindex
            y+=1
        x+=1

    print(matrix)

    # pos.sort()

    return pos


if __name__ == '__main__':
    main()