# Example: Change line type parameters

It is possible to change parameters of an Orcaflex model using python. One advantage of this is that many files can be changed rapidly. This folder is an example of how to do that.

In this folder are the following files :

```
change_parameter.py
test_script1.dat
test_script2.dat
```

The models in the test script use the Orcaflex standard vessel and line type.
The script `change_parameter.py` is an example of how you can change Orcaflex files using Python.

#### Exercise: Change parameters using a python script
Using `change_parameter.py`, change the following parameters:

- bending stiffness to 260 kNm
- axial stiffness to 1400 kNm
- change mass to 50 kg/m

To change the mass you will have to discover yourself how to find out what the Orcaflex name of the parameter is. How would you recommend on going about doing this?
