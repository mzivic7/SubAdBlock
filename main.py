import os
import chardet

# load config
try:
    with open("config.conf") as file:   # open settings file
        conf = file.readlines()   # read settings
        txt_encoding = conf[0].replace("\n", "")   # read first line and remove newline
        bellow = eval(conf[0].replace("\n", ""))   # read second line and remove newline
        filetypes = conf[2].replace("\n", "")   # read third line and remove newline
        filetypes = filetypes.split(", ")   # convert string to list
        keywords = conf[3].replace("\n", "")   # read fourth line and remove newline
        keywords = keywords.split(", ")   # convert string to list
except:
    print("Error: config.conf file is missing or is invalid!")
    exit()

# get list of all subtitles
file_list_all = os.listdir(os.getcwd())   # get list of all files in dir
file_list = []   # empty list to store only subitle names
for name in file_list_all:   # for all names in list
    if any(x in name for x in filetypes):   # if name has extension from filetypes list:
        file_list.append(name)   # append this name to subtitle list

# loop over all subtitles
for filename in file_list:   # for each subtitle file in dir
    
    # auto-detect encoding
    if txt_encoding == "auto":   # if it is set to auto-detect encoding
        with open(filename, 'rb') as file:   # open file in binary
            file_info = chardet.detect(file.read())   # get info about file
            txt_encoding = file_info["encoding"]   # get encoding type
            
    # clean subtitle
    mem = False
    try:
        with open(filename, 'r', encoding=txt_encoding) as file:  # open file
            lines = file.readlines()   # get list of lines
            with open(filename, 'w', encoding=txt_encoding) as file:   # open file
                for line in lines:   # for each line
                    if bellow is True:
                        if mem is True:   # if above line is deleted:
                            if line != "\n" and line != " \n":   # if current line is not empty or whitespace:
                                line = ""   # delete all text   
                            if line == "\n" or line == " \n": mem = False   # reset mem if ther eis no text
                    if any(x in line for x in keywords):   # if keyword is in it:
                        line = " \n"   # delete all text but leave space and newline
                        mem = True   # in next iterration check line bellow
                    file.write(line)   # write that line to file
    
    # exception:
    except:
        print("Error: file encoding type is wrong!")
        print("File: " + filename)
        print("Encoding: "+ txt_encoding)
        if txt_encoding == "auto":
            print("Confidence: "+ str(file_info["confidence"]))
        print()
        

