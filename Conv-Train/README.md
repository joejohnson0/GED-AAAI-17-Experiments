This is the baseline "T-Conv" in the paper.

It does not contain error-generator component, but uses data generated from the "BiLSTM" experiments.

You need to first run BiLSTM step 1 as is described in the readme of "Att-Ling-Train/", and then copy these files from its "Att-Ling-Train/data/" directory to the "corpus/" directory here:

&lt;min_word_freq&gt;_acl.oov.txt, acl_min_&lt;min_word_freq&gt;.src.txt, acl_min_&lt;min_word_freq&gt;.lbl.txt

in which '&lt;min_word_freq&gt;' is the minimum word frequency set in BiLSTM, which is 2 and is hard-coded.

And then do:

"python run.py"

to begin training.
