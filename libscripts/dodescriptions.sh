## this will print the current folder and create a DESCRIPTION file
## and append files list recursively
## for use in Eagle cad Control panel 
result=${PWD##*/} | printf '%s\n' "${PWD##*/}" >DESCRIPTION | ls -R >>DESCRIPTION 
