#To add external libraries for Eagle CAD
## For MAC computers:
First create a directory under the /Users/[USERNAME]/ directory
named 

    /external_lbrs

where [USERNAME] is the login name 

## Open up Eagle CAD
In Control Panel goto options-->Directories
goto the Libraries option and add the following:

    $HOME/external_lbrs

note the directories are separated by a colon 
it should read like this
 
     $EAGLEDIR/lbr:$HOME/external_lbrs
or browse to the external_lbrs directory
it will display like this:

    $EAGLEDIR/lbr:/Users/[USERNAME]/external_lbrs
    

where [USERNAME] is replaced with the login name.
Copy custom or third party libraries to external_lbrs

The advantage of using this method is that when Eagle CAD is updated the custom or third party libraries will not be overwritten or lost.

for more details visit my github 
https://github.com/pacav69/Eagle-Libraries

