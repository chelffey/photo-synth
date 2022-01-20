# Photo Synthesizer
# purpose: copy, convert and resave iphone photos based on date

import sys
import os, os.path
import filestat

def main():
    '''
    Main function
    '''

    # check args
    if (invalid_args()):
        return
    old_dir = sys.argv[1]
    # new_dir = sys.argv[2]


    # count the files
    count = filestat.count(old_dir)
    if (not count): # if error
        return
    print(f"there are {count} files in the directory '{old_dir}'.")

    print(filestat.classify(old_dir))


    copy_photos()
    convert_photos()
    reorganize_photos()


def invalid_args():
    # check command line arguments are valid
    if (len(sys.argv) != 3):
        print("Incorrect arguments. Usage: python synth.py <old_dir> <new_dir>")
        return True
    old_dir = sys.argv[1]
    new_dir = sys.argv[2]
    if (not os.path.isdir(old_dir)):
        print(f"'{old_dir}' is not a directory. Aborting.")
        return True
    return False


def copy_photos():
    '''
    copies photos across to new directory
    '''
    pass

def convert_photos():
    '''
    converts HEIC format to JPEG, or mp4
    '''
    pass

def reorganize_photos():
    '''
    reorganizes photos so renamed in date and sorted by month
    '''



if __name__ == "__main__":
    # handle arguments
    main()
    