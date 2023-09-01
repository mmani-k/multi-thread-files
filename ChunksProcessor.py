import concurrent
import concurrent.futures

from FileReader import FileReader


class ChunksProcessor:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file_reader = FileReader()
        self.batch_count = 0

    def process_chunks(self, batches):
        with concurrent.futures.ThreadPoolExecutor(len(batches)) as executor:
            batch_num = [0]
            future_to_chunks = {(executor.submit(self.process_batch_of_chunks,
                                             batch, batch_num[-1]),
                                                 batch_num.append(batch_num[-1] + 1))[0]:
                                    batch for batch in batches}
            count = 0
            for future in concurrent.futures.as_completed(future_to_chunks):
                res = future_to_chunks[future]
                try:
                    data = future.result()
                except Exception as exc:
                    print('%r generated an exception: %s' % (res, exc))
                else:
                    count += data
            return count
        return 0
    def process_batch_of_chunks(self, batch, batch_num):
        return self.file_reader.read_the_file_in_chunks(self.file_name, batch)


