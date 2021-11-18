#!/usr/bin/env python

# import sys because we need to read and write data to STDIN and STDOUT
import sys

# reading entire line from STDIN (standard input)
for line in sys.stdin:
    # to remove leading and trailing whitespace
    line = line.strip()
    # identify the date from the line
    yearMonthDay = int(line[15:23])
    # identify the temperature from the line
    temperature = int(line[87:92])
    # identify the quality flag from the line
    quality = int(line[92:93])

    if (temperature != 9999 and
            (quality == 0 or quality == 1 or quality == 4 or quality == 5 or
            quality == 9)):
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        print('%d\t%d' % (yearMonthDay, temperature))
