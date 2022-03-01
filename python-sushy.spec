%global _empty_manifest_terminate_build 0
Name:           python-sushy
Version:        3.7.3
Release:        1
Summary:        Sushy is a small Python library to communicate with Redfish based systems
License:        Apache-2.0
URL:            https://docs.openstack.org/sushy/latest/
Source0:        https://files.pythonhosted.org/packages/92/66/1dbbcc8bd0d2c3518c7ab87c26217aadd070d00f8289109c690922ba6c6f/sushy-3.7.3.tar.gz
BuildArch:      noarch

%description
Sushy is a small Python library to communicate with Redfish based systems

%package -n python3-sushy
Summary:        Sushy is a small Python library to communicate with Redfish based systems
Provides:       python-sushy
# Base build requires
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
# General requires
BuildRequires:  python3-dateutil
BuildRequires:  python3-requests
BuildRequires:  python3-stevedore
BuildRequires:  python3-stestr
BuildRequires:  python3-oslotest
# General requires
Requires:       python3-pbr
Requires:       python3-dateutil
Requires:       python3-requests
Requires:       python3-stevedore

%description -n python3-sushy
Sushy is a small Python library to communicate with Redfish based systems

%package help
Summary:        Sushy is a small Python library to communicate with Redfish based systems
Provides:       python3-sushy-doc

%description help
Sushy is a small Python library to communicate with Redfish based systems

%prep
%autosetup -n sushy-%{version}

%build
%py3_build

%install
%py3_install

install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
    find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
    find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
    find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
    find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
    find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%check
%{__python3} setup.py test

%files -n python3-sushy -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Tue Feb 15 2022 OpenStack_SIG <openstack@openeuler.org> - 3.7.3-1
- Upgrade version to 3.7.3 for OpenStack Wallaby

* Fri Aug 06 2021 OpenStack_SIG <openstack@openeuler.org> - 3.7.2-1
- Upgrade version to 3.7.2

* Wed Nov 25 2020 Python_Bot <Python_Bot@openeuler.org>
- Package Spec generated
