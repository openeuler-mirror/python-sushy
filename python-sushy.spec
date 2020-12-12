%global _empty_manifest_terminate_build 0
Name:		python-sushy
Version:	3.4.1
Release:	1
Summary:	Sushy is a small Python library to communicate with Redfish based systems
License:	Apache Software License
URL:		https://docs.openstack.org/sushy/latest/
Source0:	https://files.pythonhosted.org/packages/bb/f6/6695ca9760ffffb94cb65826c5ad6930c2ec81ab1b211f08879770627281/sushy-3.4.1.tar.gz
BuildArch:	noarch

Requires:	python3-pbr
Requires:	python3-dateutil
Requires:	python3-requests
Requires:	python3-stevedore

%description
Sushy is a Python library to communicate with Redfish based systems.
The goal of the library is to be extremely simple, small, have as few
dependencies as possible and be very conservative when dealing with BMCs
by issuing just enough requests to it (BMCs are very flaky).

%package -n python3-sushy
Summary:	Sushy is a small Python library to communicate with Redfish based systems
Provides:	python-sushy
BuildRequires:	python3-devel
BuildRequires:	python3-pbr
BuildRequires:	python3-pip
BuildRequires:	python3-setuptools
%description -n python3-sushy
Sushy is a Python library to communicate with Redfish based systems.
The goal of the library is to be extremely simple, small, have as few
dependencies as possible and be very conservative when dealing with BMCs
by issuing just enough requests to it (BMCs are very flaky).

%package help
Summary:	Development documents and examples for sushy
Provides:	python3-sushy-doc
%description help
Sushy is a Python library to communicate with Redfish based systems.
The goal of the library is to be extremely simple, small, have as few
dependencies as possible and be very conservative when dealing with BMCs
by issuing just enough requests to it (BMCs are very flaky).

%prep
%autosetup -n sushy-3.4.1

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

%files -n python3-sushy -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Wed Nov 25 2020 Python_Bot <Python_Bot@openeuler.org>
- Package Spec generated
