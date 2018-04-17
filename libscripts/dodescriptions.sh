## this will print the current folder and create a DESCRIPTION file
## and append files list recursively
## for use in Eagle cad Control panel 
# to run goto external_lbrs directory and type 
# ./libscripts/dodescriptions.sh
result=${PWD##*/} | printf '%s\n' "${PWD##*/}" >DESCRIPTION | ls -R >>DESCRIPTION 
