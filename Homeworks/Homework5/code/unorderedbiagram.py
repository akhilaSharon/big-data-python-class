import mrjob
from mrjob.job import MRJob
from mrjob.step import MRStep
import re
from itertools import islice, izip
import itertools
import heapq

WORD_RE = re.compile(r'[a-zA-Z]+')
TOPN = 10
class BigramCount(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_words,
                   combiner=self.combiner_count_words,
                   reducer=self.reducer_count_words),
            MRStep(mapper=self.topN_mapper,
                   reducer=self.topN_reducer)
        ]
    
    def mapper_get_words(self, _, line):
        words = WORD_RE.findall(line)
        for i in izip(words, islice(words, 1, None)):
            bigram=(i[0],i[1])
            s_bigram=sorted(bigram)
            yield s_bigram,1
    def combiner_count_words(self, bigram, counts):
        yield bigram, sum(counts)
    def reducer_count_words(self, bigram, counts):
        yield bigram,sum(counts)
    def topN_mapper(self, bigram, counts):
        yield "Top " + str(TOPN), (counts, bigram)
    def topN_reducer(self, _, countsAndBigrams):
        for countAndbigram in heapq.nlargest(TOPN, countsAndBigrams):
            yield _, countAndbigram
        



if __name__ == '__main__':
    BigramCount.run()
    
    