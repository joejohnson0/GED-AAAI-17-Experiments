To perform experiments on BiLSTM+Ling as described in the paper, you need to:

1. put a file named "acl_5_50_.txt" in "data/" directory, which contains error-free sentences with length of no longer than 50.

2. run "python run.py"

This does the following things for you:

1. generate artificial error

2. train the model

3. test your model on the last 10000 sentence of "acl_5_50.txt"


"acl_5_50.txt" is too large. Write to me and I'll email it to you.


Step 2 and 3 is parallel. But you can seperate Step 1 and the other two.


To run only step 1, comment out this part in "worker.py":

for word_emb_size in word_emb_sizes:
	for rnn_size in rnn_sizes:
		subprocess.Popen(["python","sub_worker.py",str(vocab_size),str(word_emb_size),str(rnn_size),save_path,nEpochs,str(max_seq_len)])


To run only step 2 and 3 (with step 1 done of course), comment out ONLY these lines in "worker.py":

os.system("mkdir " + save_path)

error_gen_cmd = "python error_gen.py {} {} {} {}".format(text_oov_file, dict_file, str(maxLine), save_path)
os.system(error_gen_cmd)

word2index_cmd = "python word2index.py {} {} {}".format(save_path, reverse_dict_file, str(maxLine))
os.system(word2index_cmd)
