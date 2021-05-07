%global _empty_manifest_terminate_build 0
Name:		python-sushy
Version:	1.6.0
Release:	1
Summary:	Sushy is a small Python library to communicate with Redfish based systems
License:	Apache-2.0
URL:		https://docs.openstack.org/sushy
Source0:	https://files.pythonhosted.org/packages/71/86/c8796820f6fe5c3641b0e47ef0922b5ee42ce22e40872550387b2fc17d71/sushy-1.6.0.tar.gz
BuildArch:	noarch
%description
About Sushy
===========

Sushy is a Python library to communicate with `Redfish`_ based systems.

The goal of the library is to be extremely simple, small, have as few
dependencies as possible and be very conservative when dealing with BMCs
by issuing just enough requests to it (BMCs are very flaky).

Therefore, the scope of the library has been limited to what is supported
by the `OpenStack Ironic <https://wiki.openstack.org/wiki/Ironic>`_
project. As the project grows and more features from `Redfish`_ are
needed we can expand Sushy to fullfil those requirements.

* Free software: Apache license
* Documentation: https://docs.openstack.org/sushy/latest/
* Usage: https://docs.openstack.org/sushy/latest/reference/usage.html
* Source: https://git.openstack.org/cgit/openstack/sushy
* Bugs: https://storyboard.openstack.org/#!/project/960

.. _Redfish: http://www.dmtf.org/standards/redfish




%package -n python2-sushy
Summary:	Sushy is a small Python library to communicate with Redfish based systems
Provides:	python-sushy
BuildRequires:	python2-devel
BuildRequires:	python2-setuptools
Requires:	python2-pbr
Requires:	python2-requests
Requires:	python2-six
%description -n python2-sushy
About Sushy
===========

Sushy is a Python library to communicate with `Redfish`_ based systems.

The goal of the library is to be extremely simple, small, have as few
dependencies as possible and be very conservative when dealing with BMCs
by issuing just enough requests to it (BMCs are very flaky).

Therefore, the scope of the library has been limited to what is supported
by the `OpenStack Ironic <https://wiki.openstack.org/wiki/Ironic>`_
project. As the project grows and more features from `Redfish`_ are
needed we can expand Sushy to fullfil those requirements.

* Free software: Apache license
* Documentation: https://docs.openstack.org/sushy/latest/
* Usage: https://docs.openstack.org/sushy/latest/reference/usage.html
* Source: https://git.openstack.org/cgit/openstack/sushy
* Bugs: https://storyboard.openstack.org/#!/project/960

.. _Redfish: http://www.dmtf.org/standards/redfish




%package help
Summary:	Development documents and examples for sushy
Provides:	python2-sushy-doc
%description help
About Sushy
===========

Sushy is a Python library to communicate with `Redfish`_ based systems.

The goal of the library is to be extremely simple, small, have as few
dependencies as possible and be very conservative when dealing with BMCs
by issuing just enough requests to it (BMCs are very flaky).

Therefore, the scope of the library has been limited to what is supported
by the `OpenStack Ironic <https://wiki.openstack.org/wiki/Ironic>`_
project. As the project grows and more features from `Redfish`_ are
needed we can expand Sushy to fullfil those requirements.

* Free software: Apache license
* Documentation: https://docs.openstack.org/sushy/latest/
* Usage: https://docs.openstack.org/sushy/latest/reference/usage.html
* Source: https://git.openstack.org/cgit/openstack/sushy
* Bugs: https://storyboard.openstack.org/#!/project/960

.. _Redfish: http://www.dmtf.org/standards/redfish




%prep
%autosetup -n sushy-1.6.0

%build
%py2_build

%install
%py2_install
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

%files -n python2-sushy -f filelist.lst
%dir %{python2_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Fri May 07 2021 OpenStack_SIG <openstack@openeuler.org>
- Package Spec generated
