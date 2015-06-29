#!/bin/bash

make clean && make

sleep 2

./main teste.pas

sleep 2

python earley.py