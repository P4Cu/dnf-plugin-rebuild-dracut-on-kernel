# dnf-plugin-rebuild-dracut-on-kernel
Plugin for dnf that triggers immediate rebuild of dracut/akmods after installation of new kernel.

This is very useful for Nvidia laptop users that enabled disk encryption as it allows to display over HDMI on boot.
Without run of akmods/dracut new initrd image will not have Nvidia.ko module and you won't be able to display over HDMI till reboot (annoying).

# installation
Currently only copy installation is supported.
```
sudo cp dnf-plugin-rebuil-dracut-on-kernel.py /usr/lib/python3.9/site-packages/dnf-plugins/
sudo chown root:root /usr/lib/python3.9/site-packages/dnf-plugins/dnf-plugin-rebuil-dracut-on-kernel.py
sudo chmod 644 /usr/lib/python3.9/site-packages/dnf-plugins/dnf-plugin-rebuil-dracut-on-kernel.py
```
TODO: package
