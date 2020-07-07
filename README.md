An example of building a static library with using dynamic Visual Studio runtime
```
conan create -k . rion/stable -s compiler="Visual Studio" -s compiler.version=16 -s arch=x86_64 -s compiler.runtime=MD -o *:shared=False
```
