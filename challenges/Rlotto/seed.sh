#!/bin/bash

nc localhost 1337 &

xterm -e 'nc 46.101.23.188 30865;bash'
