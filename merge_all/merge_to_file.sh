#!/bin/sh
sudo cat ../cyanicHosts.txt | grep -E '^0.0.0.0.*$' >> /etc/hosts.txt
sudo cat ../corporations/* | grep -E '^0.0.0.0.*$' >> /etc/hosts.txt
