#!/usr/bin/env python

f = open('cleaned.txt','r')
f_data = f.read()

list_of_bits = list(f_data)
csv_string = '\n'.join(list_of_bits[:-1])

f_out = open('cleaned.csv', 'w')
f_out.write(csv_string)
f_out.close()
