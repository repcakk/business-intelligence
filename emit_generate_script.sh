#!/usr/bin/env bash

set -e

GENERATE_SCRIPT=generate_sample_data.py

echo '#!/usr/bin/env python3

import random

' > $GENERATE_SCRIPT

cat hd-database/*.sql |
    grep -P 'CREATE' |
    sed 's/.*\[\([FW]_.*\)\]/def \1():\n    pass\n/' |
    tee -a $GENERATE_SCRIPT > /dev/null
