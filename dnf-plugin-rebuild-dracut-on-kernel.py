## Copyright 2021 Andrzej Pacanowski
##
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
##
##     http://www.apache.org/licenses/LICENSE-2.0
##
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.

## Place this file under /usr/lib/python3.9/site-packages/dnf-plugins/

import subprocess

from dnfpluginsextras import _, logger
import dnf


class DracutRebuild(dnf.Plugin):
    """
    Simple plugin that checks if new kernel is installed and runs akmod / dracut for it.
    This helps to fix missing nvidia.ko in lsinitrd image. (Plymouth cannot display on external
      screen without this image).
    """
    name = 'DracutRebuild'

    def __init__(self, base, cli):
        self.base = base

    def _akmod(self, kernels):
         subprocess.check_call([
                 'akmods',
                 '--force',
                 '--kernels',
                 *kernels
             ]
        )

    def _dracut(self, kernels):
        for kernel in kernels:
            subprocess.check_call([
                    'dracut',
                    '--force',
                    '--kver',
                    kernel
                ]
            )

    def _check_nvidia_ko(self, kernels):
        for kernel in kernels:
            output = subprocess.check_output([
                    'lsinitrd',
                    f'/boot/initramfs-{kernel}.img'
                ], universal_newlines=True
            )
            if 'nvidia.ko' in output:
                logger.info("%s: Successfuly built for %s", self.name, kernel)
            else:
                logger.critical("%s: ERROR not built for %s", self.name, kernel)

    def transaction(self):
        if not self.base.transaction:
            return

        kernels = [
            f"{package.version}-{package.release}.{package.arch}" for package in filter(
                lambda e: e.name == "kernel",
                self.base.transaction.install_set
            )
        ]

        if kernels:
            logger.info("%s: Kernels for which to rebuild initrd %s", self.name, kernels)
            self._akmod(kernels)
            self._dracut(kernels)
            self._check_nvidia_ko(kernels)

