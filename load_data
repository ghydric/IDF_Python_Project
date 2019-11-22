# can do txt and dat file load  
# arguments:  filename w/ extension (default is empty.txt)  
# returns: contents (of file)  
def load_data(filename='empty.txt'):
    file_action = 'r'
    contents = ""
    if 'dat' in filename.split('.')[1]:
        file_action = 'rb'
    try:
        f = open(filename, file_action)
        if file_action == 'rb':
            contents = pickle.load(f)
        else:
            contents = f.read()
    except:
        print("Error in loading file")
    f.close()
    return contents
# takes file name and data to save, and saves to specified file  
# arguments: filename (w/ extension) (default=empty.txt) and save_data (default="")  
# returns: nothing  
def save_data(filename='empty.txt', save_data=""):
    file_action = 'w'
    # checks to see if it's a dat file
    if 'dat' in filename.split('.')[1]:
        file_action = 'wb'
    f = open(filename, file_action)
    if file_action == 'wb':
        pickle.dump(save_data, f)
    else:
        f.write(save_data)
    f.close()
