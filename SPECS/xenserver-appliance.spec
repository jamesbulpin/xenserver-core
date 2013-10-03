Summary: Configuration for the XenServer appliance
Name: xenserver-appliance
Version: 0.1
Release: 1
URL:  http://github.com/jamesbulpin/xenserver-appliance
Source0: https://github.com/jamesbulpin/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
License: GPL
Group: Applications/System
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Requires: xenserver-appliance-xsconsole xenserver-appliance-dom0console
 
%description
Configuration files, splash screens, logos and other items needed to
make a xenserver-core system into a turnkey appliance that can be
installed from ISO.

%package xsconsole
Summary: Display xsconsole on tty1
Group: System/Hypervisor
Requires: xenserver-core xsconsole mingetty

%description xsconsole
Display xsconsole on tty1

%package dom0console
Summary: VNC console for dom0
Group: System/Hypervisor
Requires: vncterm

%description dom0console
VNC console for dom0

%prep
%setup -q

%build
 
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/%{_sbindir}
mkdir -p %{buildroot}/usr/lib/xen/bin
mkdir -p %{buildroot}/etc/init

install -m 0755 xsconsole/usr/sbin/run-boot-xsconsole %{buildroot}%{_sbindir}/run-boot-xsconsole
install -m 0755 dom0console/usr/lib/xen/bin/dom0term.sh %{buildroot}/usr/lib/xen/bin/dom0term.sh
install -m 0644 xsconsole/etc/init/xsconsole.conf %{buildroot}/etc/init/xsconsole.conf
install -m 0644 xsconsole/etc/init/start-xsconsoles.conf %{buildroot}/etc/init/start-xsconsoles.conf
install -m 0755 dom0console/usr/sbin/vncterm-wrapper %{buildroot}%{_sbindir}/vncterm-wrapper
install -m 0644 dom0console/etc/init/dom0term.conf %{buildroot}/etc/init/dom0term.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post xsconsole
sed -e's@^ACTIVE_CONSOLES=.*@ACTIVE_CONSOLES=/dev/tty[2-6]@' -i /etc/sysconfig/init
sed '/^XSCONSOLES=/d' -i /etc/sysconfig/init
echo "XSCONSOLES=/dev/tty1" >> /etc/sysconfig/init

%files
%defattr(-,root,root)

%files xsconsole
%defattr(-,root,root)
%{_sbindir}/run-boot-xsconsole
/etc/init/start-xsconsoles.conf
/etc/init/xsconsole.conf

%files dom0console
%defattr(-,root,root)
/usr/lib/xen/bin/dom0term.sh
/usr/sbin/vncterm-wrapper
/etc/init/dom0term.conf

%changelog
* Thu Oct 03 2013 James Bulpin <james.bulpin@eu.citrix.com> - 0.1-1
- Initial package

