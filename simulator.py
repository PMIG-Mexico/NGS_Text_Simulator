#!/usr/bin/python
import numpy as np
import string
import random
from random import shuffle

def TextNGSimulator(text,k,coverage,coverageSD,errorRate,nonCallingRate,reverseRate):
	text=str(text)
	kmers=[text[x:x+k] for x in range(0,len(text)-k+1)]
	reads=[]
	for kmer in kmers:
		readcoverage=np.random.randint(coverage-coverageSD,coverage+coverageSD)
		for i in range(0,readcoverage):
			luckyread=np.random.random()
			nonCalling=np.random.random()
			if luckyread > errorRate and nonCalling > nonCallingRate :
				reads.append(kmer)
			elif luckyread<errorRate:
				lucky=list(kmer)
				lucky[np.random.randint(0,len(kmer))]=random.choice(string.ascii_lowercase)				
				reads.append("".join(lucky))
			elif nonCalling < nonCallingRate:
				asteriscksNumber=np.random.randint(0,len(kmer))
				nonCallingRead=list(kmer)
				for astericks in range(0,asteriscksNumber):
					nonCallingRead[np.random.randint(0,len(kmer))]='*'
				reads.append("".join(nonCallingRead))				
		shuffle(reads)
		for x in range(0,int(reverseRate*len(reads))):
			reads[x]=reads[x][::-1]
	return(reads)
