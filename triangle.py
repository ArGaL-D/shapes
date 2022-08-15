import sys, getopt


def triangle(size=36, background='-', char='*', reverse=True):
    # Represents half of the total background characters per line
    B = size//2
    # Represents total lines for the triangle
    L = size - B

    # Creates the total lines' triangle
    for i in range(L):
        line = ''

        if not reverse:
            # NORMAL TRIANGLE
            # Generates each line to build the figure
            for j in range(size):
                if j < B:
                    line += background
                elif j < size - B:
                    line += char
                else:
                    line += background
            B -= 1            
        else:
            # REVERSE TRIANGLE
            # 'R' is similar to 'B'... represents number background characters
            R = i
            for j in range(size):
                if j < R:
                    line += background
                elif j < size - R:
                    line += char
                else:
                    line += background                
        print(line)


if __name__ == "__main__":
    arguments_list = sys.argv[1:]
    options = 'hrc:s:b:'

    try:
        # Default triangle options
        c = '*'
        b = ' '
        r = False
        s = 11
        h = False

        # Command line arguments
        arguments, values = getopt.getopt( arguments_list, options )

        for arg, value in arguments:
            if arg in ['-h']:
                h = True
                print('\t-h\tHelp')
                print('\t-b\tBackground character triangle')
                print('\t-c\tTriangle character')
                print('\t-s\tSize of the triangle')
                print('\t-r\tReverse triangle')

            elif arg in ['-r']:
                r = True

            elif arg in ['-c']:
                c = value[0]

            elif arg in ['-s']:
                if value.isnumeric():
                    s = int(value)
                else:
                    print('Only numbers for size [-s]')
                    break
            
            elif arg in ['-b']:
                b = value[0]
        
        if not h:
            triangle(size=s, char=c, background=b, reverse=r)

    except getopt.GetoptError as err:
        print(' [-] Ups... something went worng :(\n','[-]',err)
