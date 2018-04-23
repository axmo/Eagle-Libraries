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

# Finding Libraries

For those searching for CAD libraries i recommend using this search site


 [componentsearchengine](https://componentsearchengine.com)

This can provide CAD libraries for a number of CAD programs such as Altium, Eagle, EasyEDA, KiCad and more. If the part does not exist you can request for it to built. Try to make sure you have the technical documents that is required such as mechanical, specs, datasheets etc.

For example a part in a post on https://electronics.stackexchange.com/ here is the link:

[Digikey site - Manufacturers Part Number BQ78350DBTR-R1](https://componentsearchengine.com/part.php?partID=834563)



