#!/usr/bin/env bash

set -e

GENERATE_SCRIPT=generate_sample_data.py

echo '#!/usr/bin/env python3

import datetime
import random


# Generic generators

# TODO

# Table generators
def inhibit_emission(values):
    return values[0] == "()"

' > $GENERATE_SCRIPT

cat hd-database/*.sql |
    sort |
    grep -P 'CREATE' |
    sed 's/.*\[\([FW]_.*\)\]/def \1():\
    insert_statement = "INSERT INTO \1 values\\n  {}\\n;"\
\
    values = []\
    for i in range(10):\
        values_line = "()".format(\
        )\
        values.append(values_line)\
\
    if inhibit_emission(values): return\
    print(insert_statement.format("\\n, ".join(values)))\
/' |
    tee -a $GENERATE_SCRIPT > /dev/null

echo '

# Main function

def main():' >> $GENERATE_SCRIPT
cat hd-database/*.sql |
    sort |
    grep -P 'CREATE' |
    sed 's/.*\[\([FW]_.*\)\]/    \1()/' |
    tee -a $GENERATE_SCRIPT > /dev/null

echo -n '

if __name__ == "__main__":
    main()
' >> $GENERATE_SCRIPT
