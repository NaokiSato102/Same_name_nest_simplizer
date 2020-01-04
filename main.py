#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import glob
import os

print('sys.argv         \n   ', sys.argv)
print('type(sys.argv)   \n   ', type(sys.argv))
print('len(sys.argv)    \n   ', len(sys.argv))

print()

for i in range(len(sys.argv)):
	print("sys.argv[{}]      \n   {}\n".format(i, sys.argv[i] ) )
	print("type(sys.argv[{}])\n   {}\n".format(i, type(sys.argv[i] ) ) )



l = glob.glob(sys.argv[1]+'/*')
for i in l:
	print(i)

	j = os.path.basename(i)
	print(os.path.basename(i) )

	k = glob.glob(i+"\\"+j )
	print(k)

	if(k ):
		print("ダブり")
	else:
		print("ダブってない")