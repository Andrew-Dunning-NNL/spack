# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class PyAtpublic(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://www.example.com"
    pypi     = "atpublic/atpublic-2.1.2.tar.gz"

    version('2.1.2', sha256='82a2f2c0343ac67913f67cdee8fa4da294a4d6b863111527a459c8e4d1a646c8')

