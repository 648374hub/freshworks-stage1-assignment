import os
import json
import sys
from time import time

# TTL = 60  #sec



def create(data, key, value):
    if key in data:
        print('Key Already Exist!')
        return -1
    else:
        data[key] = value
        print("Data Successfully Saved.")
        return 1

def delete(data, key):
    if key in data:
        data.pop(key)
        print("Data Successfully Deleted")
        return 1
    else:
        print("Key not found!")
        return -1

def retrive(data, key):
    if key in data:
        print(f"{key}: {data[key]}")
        return 1
    else:
        print('Key not found!')
        return -1


def main():
    arg = sys.argv
    if len(arg) < 4:
        print("Invalid Input!")
        print('Please Enter: "username" "operation" "key" "Value"(optional)')
        return -1
    dir_list = os.listdir()
    if arg[1] + '.json' not in dir_list:
        d = {"time": time()}
    else:
        fp = open(f'{arg[1]}.json')
        d = json.load(fp)
        if time() - d['time'] > d['TTL']:
            d = {"time": time(), "TTL": d["TTL"]}
        fp.close()
    if arg[2] == 'create':
        if len(arg) < 5:
            print('Invalid Input!')
            print('"Username" "create" "Key" "value" "TTL"(optional)')
        else:
            if len(arg) > 5:
                if arg[5].isnumeric():
                    d["TTL"] = int(arg[5])
                else:
                    print("TTL is not Valid!")
                    return -1
            else:
                d["TTL"] = sys.maxsize
            create(d, arg[3], arg[4])
    elif arg[2] == 'retrive':
        retrive(d, arg[3])
    elif arg[2] == 'delete':
        delete(d, arg[3])
    else:
        print('Invalid operation!')
        print("Available operation is: 1. create 2. retrive 3. delete")

    fp = open(f'{arg[1]}.json', 'w')
    json.dump(d, fp, indent=2)
    fp.close()


if __name__ == '__main__':
    main()
