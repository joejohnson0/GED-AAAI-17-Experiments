import os
import sys
import random
import math
import string
import gensim
import gensim.models as gm
from gensim import corpora
from collections import defaultdict
import glob

window_size = int(float(sys.argv[1]))
vector_size = int(float(sys.argv[2]))
min_word_freq = int(float(sys.argv[3]))
save_path = str(sys.argv[4]) # "LM/"
src_file = str(sys.argv[5])
logfile = str(sys.argv[6])

log = open(logfile,"a+")
log.write("------ Word2Vec ------\n")
log.write("Window size: " + str(window_size) + "\n")
log.write("Vector size: " + str(vector_size) + "\n")
log.write("Minimum word frequency: " + str(min_word_freq) + "\n")
log.flush()

# argument 'window' of Word2Vec: maximum distance from the word
one_side_window = int(math.floor(window_size/2))

sentences = []
with open(src_file, "r") as corr:
	sentences = [[tok for tok in line.lower().split()] for line in corr]
	model = gm.Word2Vec(sentences, size=vector_size, window=one_side_window, min_count=min_word_freq, workers=4)
	model.save(save_path + str(vector_size)+"_"+str(window_size)+"_"+str(min_word_freq)+"_mdl")
	dictionary = corpora.Dictionary(sentences)
	dictionary.save_as_text(save_path + str(vector_size)+"_"+str(window_size)+"_"+str(min_word_freq)+"_dict")
	log.write("Dictionary Size: " + str(len(dictionary.values())) + "\n")
	corr.close()

log.write("------ End Word2Vec ------\n")

log.close()