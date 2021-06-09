"""Script to automatically create a manifest file for Qiime2
"""
import glob
import os
#Find all of the fastq files in the current directory - assumed to be paired end data.
#The search string being matched can be edited as per the user's specific file structure.
fwd_seq_files = glob.glob("*_R1_val_1.fq")
rev_seq_files = glob.glob("*_R2_val_2.fq")
abs_path = os.getcwd()

fwd_seq_files.sort()
rev_seq_files.sort()

smp = []
for i in fwd_seq_files:
  iname = i[:-8]
  smp.append(iname)

fwd_dict = dict(zip(smp,fwd_seq_files))
rev_dict = dict(zip(smp,rev_seq_files))

header = 'sample-id\tforward-absolute-filepath\treverse-absolute-filepath'
manifest_list = []
manifest_list.append(header)

for id in smp:
  tmp = []
  tmp.append(id)
  fwd_fl = fwd_dict[id]
  fwd_pth = abs_path + '/' + fwd_fl
  tmp.append(fwd_pth)
  rev_fl = rev_dict[id]
  rev_pth = abs_path + '/' + rev_fl
  tmp.append(rev_pth)
  tmpj = "\t".join(tmp)
  manifest_list.append(tmpj)

manifest_j = "\n".join(manifest_list)
manifest_file = open("manifest.txt", "w")
manifest_file.write(manifest_j)
manifest_file.close()
