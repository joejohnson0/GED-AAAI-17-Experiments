This is the "SVM" baseline.

To run training, you've got to have kenlm and liblinear.

It does not contain error-generator component, but uses data generated from the "BiLSTM" experiments.

You need to first run BiLSTM step 1 as is described in the readme of "Att-Ling-Train/", and then copy these files from its "Att-Ling-Train/data/" directory to the this directory:

&lt;min_word_freq&gt;_acl.oov.txt, acl_min_&lt;min_word_freq&gt;.src.txt, acl_min_&lt;min_word_freq&gt;.lbl.txt

in which '&lt;min_word_freq&gt;' is the minimum word frequency set in BiLSTM, which is 2 and is hard-coded.


Step 1: train n-gram model

1. put acl.txt which is error-free version of the corpus in klm-train

2. run the following commands:

cat "acl.txt" | python process.py | PATH_YOU_INSTALLED_KENLM/kenlm/bin/lmplz -o 3 > "acl.arpa"

PATH_YOU_INSTALLED_KENLM/kenlm/bin/build_binary "acl.arpa" "acl.klm"

Step 2: train svm

1. copy acl.klm from "klm-train/" to this directory

2. do "python run.py"
