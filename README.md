# Python multi-thread read of local files Demo

This is to simulate a demo of a feature available in AWS s3 to read files in chunks parallelly. Since multi-thread access of the local file handle is not allowed, the file handle had to be created for each thread, which introduces an inefficiency.

The total file size is split into chunk-boundaries and each chunk is read parallelly in a different thread, a total of 5 chunks are read at a time to keep it close to AWS lambdas, which allows only 6 threads to run at a time.

Though python is limited by GIL - Global Interpreter Lock, which allows only one thread to run at  a time, since file or S3 IO read is a blocking IO, it lets other threads to run while a thread is blocked on reading the file or S3.
