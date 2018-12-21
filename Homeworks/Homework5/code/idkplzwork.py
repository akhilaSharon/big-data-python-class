import heapq 
from mrjob.job import MRJob 
from mrjob.step import MRStep 
TOPN = 10 
class WordCountTopN(MRJob):
    def mapper(self, _, line):
        for word in line.strip().lower().split():
            if str.isalpha(word):
                yield word, 1 
    def reducer(self, word, counts):
        yield word, sum(counts)
    def topN_mapper(self, word, count):
        yield "Top" + str(TOPN), (count, word)
    def topN_reducer(self, _, countsAndWords):
        for countAndWord in heapq.nlargest(TOPN, countsAndWords):
            yield _, countAndWord
    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer),
            MRStep(mapper=self.topN_mapper,
                   reducer=self.topN_reducer)
        ]
if __name__ == "__main__":
    WordCountTopN.run()