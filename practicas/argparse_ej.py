import argparse
import os.path


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--file1", help="primer archivo")
    parser.add_argument("-o", "--file2", help="segundo archivo")

    args = parser.parse_args()

    if os.path.exists(args.file1):
        with open(args.file1,'r') as firstfile:
            with open(args.file2,'w') as secondfile:
	
            # read content from first file
                for line in firstfile:
                    
                # append content to second file
                    secondfile.write(line)
    else:
        raise FileNotFoundError