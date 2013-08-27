try:
    data = open('sketch.txt')

    #when test the function in shell using as namespace, remember to invoke data.seek(0) to restart from first line

    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
        except ValueError:
            pass

    data.close()
except IOError:
    print('The data file is missing')
