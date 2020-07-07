import os

from conans import ConanFile, tools, CMake
from conans.tools import replace_in_file

class StringprepConan(ConanFile):
    name = "stringprep"
    description = "stringperp library from libidn1"
    version = "20200611"
    license = "LGPL 2.1"
    url = "https://www.gnu.org/software/libidn/"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [False, True]}
    default_options = "shared=True"
    generators = "cmake_find_package"
    exports_sources = "CMakeLists.txt", "rfc3454.*"

    scm_to_conandata = True
    scm={
        "type": "git",
        "url": "https://git.savannah.gnu.org/git/libidn.git",
        "revision": "86e84739c5186faf3722a0f42e1e2db27870b3a5"
    }

    def build(self):
        p = os.path.join(self.build_folder, 'lib')
        for f in ['unistr', 'unitypes']:
            os.rename(os.path.join(p, 'gl', f + '.in.h'), os.path.join(p, f + '.h'))
            
        replace_in_file('lib/stringprep.h', '# include <idn-int.h>', """
#include <stdint.h>
#include <BaseTsd.h>
typedef SSIZE_T ssize_t;
""")
        cmake = CMake(self) # it will find the packages by using our auto-generated FindXXX.cmake files
        cmake.configure([])
        cmake.build()
        
    def package(self):
        install_dir = "conan_install"
        self.copy("stringprep.h", dst="include", src="lib")
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
    
    def package_info(self):
        if self.settings.compiler == "Visual Studio":
            self.cpp_info.libs = ["stringprep.lib"]
        else:
            self.cpp_info.libs = ["stringprep"]