cmake_minimum_required(VERSION 3.0.0)

project(stringprep LANGUAGES C)

add_library(stringprep
  lib/stringprep.c
  lib/profiles.c
  lib/nfkc.c
  lib/gl/unistr/u8-check.c
  rfc3454.c
)
target_compile_definitions(stringprep PRIVATE LIBIDN_BUILDING)
target_include_directories(stringprep PRIVATE
  ${CMAKE_SOURCE_DIR}
  ${CMAKE_SOURCE_DIR}/lib
  ${CMAKE_SOURCE_DIR}/lib/gl
)

if(MSVC)
  target_compile_definitions(stringprep PRIVATE _CRT_SECURE_NO_WARNINGS _GENERATED_STDINT_H)
  target_include_directories(stringprep PRIVATE ${CMAKE_SOURCE_DIR}/windows/include)
endif()
