# This is a sample Python script.
import os.path
from time import sleep

from ChunksProcessor import ChunksProcessor

"""
Demo application to read a local file from disk in parallel manner using python
multi-threading and do some simple processing.
"""

def divide_chunks(a, n):
    lst = []
    for i in range(0, len(a), n):
        lst.append(a[i: i + n])
    return lst


if __name__ == '__main__':

    """
    This code was originally created for reading chunks of a very large file
    from AWS S3 and process the chunks parallelly using multi-threading in lambda.
    Here we are trying to simulate the same behaviour using a local file. But the local 
    file handle does support parallel seeks and reads. Local file handles are not 
    thread safe and hence closing this file and opening it again in the submodules,
    so each thread gets its own handle. It is not very efficient, but for demo purpose
    it is done this way
    """
    file_name = "files/sample-file.txt"
    f = open(file_name, "r")
    file_size = os.path.getsize(file_name)
    f.close()
    # print(f"file size: {file_size}")
    chunks = [*range(200, file_size, 200)]
    chunks.append(file_size)
    start_pos = [0]
    lst = [((start_pos[-1], elem), start_pos.append(elem))[0] for elem in chunks]
    batches = divide_chunks(lst, 5)
    print(batches)
    cp = ChunksProcessor(file_name)
    count = 0
    for batch in batches:
        count += cp.process_chunks(batch)

    print(f"Total number of lines {count}")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
