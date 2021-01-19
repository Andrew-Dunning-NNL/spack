# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class PyFtfy(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://www.example.com"
    pypi     = "ftfy/ftfy-5.8.tar.gz"

    version('5.8', sha256='51c7767f8c4b47d291fcef30b9625fb5341c06a31e6a3b627039c706c42f3720')

