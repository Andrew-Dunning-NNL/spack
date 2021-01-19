# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class PyDvc(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://www.example.com"
    pypi     = "dvc/dvc-1.11.10.tar.gz"

    version('1.11.10', sha256='6b53ebf1bd5619836f131181402bb21f7b44109166e9db8f8d6a0d8c7ce9458d')

