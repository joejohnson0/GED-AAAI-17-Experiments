This is the baseline "T-Conv" in the paper.

It does not contain error-generator component, but uses data generated from the "BiLSTM" experiments.

You need to first run BiLSTM step 1 as is described in the readme of "Att-Ling-Train/", and then copy these files from its "Att-Ling-Train/data/" directory to the "corpus/" directory here:

'<min_word_freq>_acl.oov.txt', 'acl_min_<min_word_freq>.src.txt', 'acl_min_<min_word_freq>.lbl.txt'

in which '<min_word_freq>' is the minimum word frequency set in BiLSTM, which is 2 and is hard-coded.

And then do:

"python run.py"

to begin training.
