Name: dnf-plugin-rebuild-dracut-on-kernel
Version: 0.0.1
Release: 1%{?dist}
Summary: Plugin for dnf that triggers immediate rebuild of dracut/akmods after installation of new kernel.
License: ASL 2.0
URL: https://github.com/P4Cu/dnf-plugin-rebuild-dracut-on-kernel
BuildArch: noarch

Requires: dnf
BuildRequires: python3-devel

Source0: %{name}-%{version}.tar.gz

%description
This is very useful for Nvidia laptop users that enabled disk encryption as it allows to display
over HDMI on boot.  Without run of akmods/dracut new initrd image will not have Nvidia.ko
module and you won't be able to display over HDMI till reboot (annoying).

%prep

%install
mkdir -p %{buildroot}%{python3_sitelib}/dnf-plugins/
cp -a dnf-plugin-rebuild-dracut-on-kernel.py %{buildroot}%{python3_sitelib}/dnf-plugins/dnf-plugin-rebuild-dracut-on-kernel.py

%check

%files
%{python3_sitelib}/dnf-plugins/

%changelog
* Sun Sep 12 2021 Andrzej Pacanowski <Andrzej.Pacanowski@gmail.com> -
- Initial implementation based on what I'm using on my machines.

%post

