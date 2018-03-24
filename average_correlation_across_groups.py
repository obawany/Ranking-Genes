import pandas as pd
import os
import logging
import operator
import math


# def average_correlation_gene():
	# combined_file_path = os.path.join(cmn.DL_DIR, cmn.PTEN_COMB_FNAME)
with open("/Users/obawany/Downloads/GDC_Downloads/PTEN_combined.txt") as f:
	file = f.read().splitlines()
	for line in file:
		columns = line.split("\t")
		for cols in columns:
			print(cols[0])
		for line in file[]:
			columns = line.split("\t")
		    gene_Name = line[0]

		    for columns in file[1:]:
		    	print(columns)

	   	numRows = 0
	    sums = [0] * len(columns)


	    for line in f:
	        # Skip empty lines
	        if not line.strip():
	            continue

	        values = line.split("\t")
	        for i in xrange(len(values)):
	            sums[i] += int(values[i])
	        numRows += 1

	    for index, summedRowValue in enumerate(sums):
	        print columns[index], 1.0 * summedRowValue / numRows

    # combined_file_path = os.path.join(cmn.DL_DIR, cmn.PTEN_COMB_FNAME)
    # if os.path.isfile(combined_file_path):
    #     logging.info("Found combined PTEN correlation file, will go ahead and find average correlation values")

    #     df = pd.read_csv(combined_file_path, sep="\t", index_col=0)

    #     average_gene_rank_file = os.path.join(cmn.DL_DIR, cmn.COL_RANK_FNAME)
    #     col_ranks = pd.DataFrame()
    #     i = 0

    #     for col in df.columns:
    #         logging.info("Generating rankings for '%s' ..." % col)

    #         col_rank_dict = {}
    #         for row in df.index:
    #             if not math.isnan(float(df.loc[row][col])):
    #                 col_rank_dict[row] = abs(float(df.loc[row][col]))
    #             else:
    #                 col_rank_dict[row] = 0
    #         col_rank = sorted(col_rank_dict.items(), key=operator.itemgetter(1), reverse=True)
    #         col_ranks.insert(i, col, [t[0] for t in col_rank])
    #         i += 1

    #         logging.info("Done.\n")

    #     logging.info("Writing column rankings to file ...")
    #     col_ranks.to_csv(column_ranks_file, sep="\t")
    #     logging.info("Done.\n")

    # else:
    #     logging.warning("Combined PTEN correlation file not found.")
f.close()

# def run():

#     average_correlation_gene()
