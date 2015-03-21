#!/bin/python
import argparse
import os

if __name__ == "__main__":
    #get target folder and output file
    parser = argparse.ArgumentParser()
    parser.add_argument("in_folder")
    parser.add_argument("out_file")
    args = parser.parse_args()
    parser.parse_args()

counts = dict() #keeps track of word counts
max_size = 0 #keeps track of maximum word size
punctuation ='\'\"-,.:;!?'
#parse through each word in each file, and add to/increment dict accordingly
for i in os.listdir(args.in_folder):
    with open(args.in_folder+"/"+i) as file:
        for line in file: #Go line by line in case file is huge
            words = line.split()
            for word in words:
                word = word.lstrip(punctuation).rstrip(punctuation).lower()
                if len(word) > max_size:
                    max_size = len(word)
                if word not in counts:
                    counts[word] = 1
                else:
                    counts[word] += 1
#alphebeticalize the dict
word_list = counts.keys()
word_list.sort()
#write to text file
with open(args.out_file,'w')  as out:
    for word in word_list:
        out.write(word+(max_size-len(word))*" "+"\t"+str(counts[word])+"\n")
    


