#!/bin/sh
cat ../cyanicHosts.txt | grep -E '^0.0.0.0.*$' >> merged.txt
cat ../corporations/* | grep -E '^0.0.0.0.*$' >> merged.txt
echo Done
