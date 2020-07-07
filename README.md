This Conan recipe builds stringprep library from LibIDN-1.

The recipe was designed on Windows and for Windows, so there is no any guarantee it will work for anything else.
But patches are welcome as always.

An example of building a static library with using dynamic Visual Studio runtime
```
conan create -k . rion/stable -s compiler="Visual Studio" -s compiler.version=16 -s arch=x86_64 -s compiler.runtime=MD -o *:shared=False
```
