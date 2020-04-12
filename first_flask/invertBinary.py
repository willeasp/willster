def rotateBinary (filename, rotation):
    image = open(filename)                              # opens file to read from
    lines = image.readlines()                       

    arr = []                                        # 2D list that stores each character (arr[row][column])

    for line in lines:
        arr.append([c for c in line if c != "\n"])  # stores characters
    image.close()

    writefile = filename.replace(".txt", "_invert.txt") 

    writeImage = open(writefile, "w")               # creates file to write to, takes original filename and adds "_invert" to the end

    for x in range(len(arr[0])):
        for y in range(len(arr)):
            if rotation is "r":
                writeImage.write(arr[-y-1][x])          # writes to file
            if rotation is "l":
                writeImage.write(arr[y][-x-1])          # writes to file

        writeImage.write("\n")


