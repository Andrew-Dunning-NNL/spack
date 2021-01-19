# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class PyDulwich(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://www.example.com"
    pypi     = "dulwich/dulwich-0.20.15.tar.gz"

    version('0.20.15', sha256='fb1773373ec2af896031f8312af6962a1b8b0176a2de3fb3d84a84ec04498888')

