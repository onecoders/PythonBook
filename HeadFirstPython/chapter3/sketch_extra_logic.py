import os

if os.path.exists('sketch.txt'):  
    data = open('sketch.txt')

    #when test the function in shell using as namespace, remember to invoke data.seek(0) to restart from first line

    for each_line in data:
        if not each_line.find(':') == -1:
            (role, line_spoken) = each_line.split(':', 1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')

    data.close()
else:
    print('The data file is missing')
