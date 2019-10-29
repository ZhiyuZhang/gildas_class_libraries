#!/bin/bash -f
sed "s@oldpwd@$PWD@" init.class >> tmp.dat 
sed "s|oldpwd|$PWD|" tmp.dat    >>  ~/.gag/init/init.class 


