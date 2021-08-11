#!/bin/bash

pfd=$(ls *.pfd -t | head -n1)
bestprof=$(ls *.bestprof -t | head -n1)

~/work/shared/PSC/magnetar/testdata/get_TOAs.py -t $bestprof -n 4 $pfd
