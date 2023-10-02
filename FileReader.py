import os
class FileReader:

    def read_the_file_in_chunks(self, file_name, chunk_bounds):
        """
        Opening the file in each thread so as to access the file
        handle in a thread-safe manner. This is very inefficient
        in local file system, but in AWS S3, there is support for accessing
        ranges of files in a thread-safe manner. This application is
        just a local demo replica of code that works in S3
        """
        file_name = file_name
        f = open(file_name, "r")
        f.seek(chunk_bounds[0])
        chunk = f.read(chunk_bounds[1] - chunk_bounds[0])
        # chunk =  str(f.read(chunk_bounds[1] - chunk_bounds[1]))
        count = {chunk.count('\n')}
        print(f"bounds : {chunk_bounds} {chunk}")

        return chunk.count('\n')


