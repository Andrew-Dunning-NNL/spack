# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class PyFlattenDict(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://www.example.com"
    pypi     = "flatten-dict/flatten-dict-0.3.0.tar.gz"

    version('0.3.0', sha256='0ccc43f15c7c84c5ef387ad19254f6769a32d170313a1bcbf4ce582089313d7e')

