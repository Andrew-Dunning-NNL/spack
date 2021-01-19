# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class PyFluflLock(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://www.example.com"
    pypi     = "flufl.lock/flufl.lock-5.0.4.tar.gz"

    version('5.0.4', sha256='09ffef831d57c4d182e398e97bb74ad8c8ffbd1710175a5a0b0f057095db12f1')

