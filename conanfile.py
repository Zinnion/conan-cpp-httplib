#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os

class CppHttpLibConan(ConanFile):
    name = "cpp-httplib"
    version = "0.2.1"
    url = "https://github.com/zinnion/conan-cpp-httplib"
    description = "A single file C++11 header-only HTTP/HTTPS server and client library"
    license = "MIT"
    no_copy_source = True
    build_policy = "always"
    requires = "OpenSSL/1.1.1b@zinnion/stable", "zlib/1.2.11@zinnion/stable"

    def source(self):
        source_url = "https://github.com/maurodelazeri/cpp-httplib"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, "sources")

    def package_id(self):
        self.info.header_only()

    def package(self):
        self.copy(pattern="LICENSE")
        self.copy(pattern="*.[i|h]pp", dst="include", keep_path=True)
