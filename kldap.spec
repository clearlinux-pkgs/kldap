#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kldap
Version  : 21.04.2
Release  : 32
URL      : https://download.kde.org/stable/release-service/21.04.2/src/kldap-21.04.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.04.2/src/kldap-21.04.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/21.04.2/src/kldap-21.04.2.tar.xz.sig
Summary  : LDAP access API for KDE
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 LGPL-2.0 MIT
Requires: kldap-data = %{version}-%{release}
Requires: kldap-lib = %{version}-%{release}
Requires: kldap-license = %{version}-%{release}
Requires: kldap-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(libsasl2)
BuildRequires : extra-cmake-modules-data
BuildRequires : kdoctools-dev
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : libsecret-dev
BuildRequires : openldap-dev
BuildRequires : qtbase-dev
BuildRequires : qtkeychain-dev

%description
# KLDAP #
Allows LDAP accessing with a convenient Qt style C++ API.

%package data
Summary: data components for the kldap package.
Group: Data

%description data
data components for the kldap package.


%package dev
Summary: dev components for the kldap package.
Group: Development
Requires: kldap-lib = %{version}-%{release}
Requires: kldap-data = %{version}-%{release}
Provides: kldap-devel = %{version}-%{release}
Requires: kldap = %{version}-%{release}

%description dev
dev components for the kldap package.


%package doc
Summary: doc components for the kldap package.
Group: Documentation

%description doc
doc components for the kldap package.


%package lib
Summary: lib components for the kldap package.
Group: Libraries
Requires: kldap-data = %{version}-%{release}
Requires: kldap-license = %{version}-%{release}

%description lib
lib components for the kldap package.


%package license
Summary: license components for the kldap package.
Group: Default

%description license
license components for the kldap package.


%package locales
Summary: locales components for the kldap package.
Group: Default

%description locales
locales components for the kldap package.


%prep
%setup -q -n kldap-21.04.2
cd %{_builddir}/kldap-21.04.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1623355422
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 -std=gnu++98"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1623355422
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kldap
cp %{_builddir}/kldap-21.04.2/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kldap/29fb05b49e12a380545499938c4879440bd8851e
cp %{_builddir}/kldap-21.04.2/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kldap/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
cp %{_builddir}/kldap-21.04.2/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kldap/8287b608d3fa40ef401339fd907ca1260c964123
cp %{_builddir}/kldap-21.04.2/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kldap/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/kldap-21.04.2/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/kldap/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
pushd clr-build
%make_install
popd
%find_lang kio_ldap
%find_lang libkldap5

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kservices5/ldap.protocol
/usr/share/kservices5/ldaps.protocol
/usr/share/qlogging-categories5/kldap.categories
/usr/share/qlogging-categories5/kldap.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KLDAP/KLDAP/AddHostDialog
/usr/include/KF5/KLDAP/KLDAP/Ber
/usr/include/KF5/KLDAP/KLDAP/LdapClient
/usr/include/KF5/KLDAP/KLDAP/LdapClientSearch
/usr/include/KF5/KLDAP/KLDAP/LdapClientSearchConfig
/usr/include/KF5/KLDAP/KLDAP/LdapClientSearchConfigReadConfigJob
/usr/include/KF5/KLDAP/KLDAP/LdapClientSearchConfigWriteConfigJob
/usr/include/KF5/KLDAP/KLDAP/LdapConfigWidget
/usr/include/KF5/KLDAP/KLDAP/LdapConfigureWidget
/usr/include/KF5/KLDAP/KLDAP/LdapConnection
/usr/include/KF5/KLDAP/KLDAP/LdapControl
/usr/include/KF5/KLDAP/KLDAP/LdapDN
/usr/include/KF5/KLDAP/KLDAP/LdapDefs
/usr/include/KF5/KLDAP/KLDAP/LdapObject
/usr/include/KF5/KLDAP/KLDAP/LdapOperation
/usr/include/KF5/KLDAP/KLDAP/LdapSearch
/usr/include/KF5/KLDAP/KLDAP/LdapSearchClientReadConfigServerJob
/usr/include/KF5/KLDAP/KLDAP/LdapServer
/usr/include/KF5/KLDAP/KLDAP/LdapUrl
/usr/include/KF5/KLDAP/KLDAP/Ldif
/usr/include/KF5/KLDAP/kldap/addhostdialog.h
/usr/include/KF5/KLDAP/kldap/ber.h
/usr/include/KF5/KLDAP/kldap/kldap_export.h
/usr/include/KF5/KLDAP/kldap/ldapclient.h
/usr/include/KF5/KLDAP/kldap/ldapclientsearch.h
/usr/include/KF5/KLDAP/kldap/ldapclientsearchconfig.h
/usr/include/KF5/KLDAP/kldap/ldapclientsearchconfigreadconfigjob.h
/usr/include/KF5/KLDAP/kldap/ldapclientsearchconfigwriteconfigjob.h
/usr/include/KF5/KLDAP/kldap/ldapconfigurewidget.h
/usr/include/KF5/KLDAP/kldap/ldapconfigwidget.h
/usr/include/KF5/KLDAP/kldap/ldapconnection.h
/usr/include/KF5/KLDAP/kldap/ldapcontrol.h
/usr/include/KF5/KLDAP/kldap/ldapdefs.h
/usr/include/KF5/KLDAP/kldap/ldapdn.h
/usr/include/KF5/KLDAP/kldap/ldapobject.h
/usr/include/KF5/KLDAP/kldap/ldapoperation.h
/usr/include/KF5/KLDAP/kldap/ldapsearch.h
/usr/include/KF5/KLDAP/kldap/ldapsearchclientreadconfigserverjob.h
/usr/include/KF5/KLDAP/kldap/ldapserver.h
/usr/include/KF5/KLDAP/kldap/ldapurl.h
/usr/include/KF5/KLDAP/kldap/ldif.h
/usr/include/KF5/kldap_version.h
/usr/lib64/cmake/KF5Ldap/KF5LdapConfig.cmake
/usr/lib64/cmake/KF5Ldap/KF5LdapConfigVersion.cmake
/usr/lib64/cmake/KF5Ldap/KF5LdapTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Ldap/KF5LdapTargets.cmake
/usr/lib64/libKF5Ldap.so
/usr/lib64/qt5/mkspecs/modules/qt_Ldap.pri

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kioslave5/ldap/index.cache.bz2
/usr/share/doc/HTML/ca/kioslave5/ldap/index.docbook
/usr/share/doc/HTML/de/kioslave5/ldap/index.cache.bz2
/usr/share/doc/HTML/de/kioslave5/ldap/index.docbook
/usr/share/doc/HTML/en/kioslave5/ldap/index.cache.bz2
/usr/share/doc/HTML/en/kioslave5/ldap/index.docbook
/usr/share/doc/HTML/es/kioslave5/ldap/index.cache.bz2
/usr/share/doc/HTML/es/kioslave5/ldap/index.docbook
/usr/share/doc/HTML/et/kioslave5/ldap/index.cache.bz2
/usr/share/doc/HTML/et/kioslave5/ldap/index.docbook
/usr/share/doc/HTML/fr/kioslave5/ldap/index.cache.bz2
/usr/share/doc/HTML/fr/kioslave5/ldap/index.docbook
/usr/share/doc/HTML/gl/kioslave5/ldap/index.cache.bz2
/usr/share/doc/HTML/gl/kioslave5/ldap/index.docbook
/usr/share/doc/HTML/it/kioslave5/ldap/index.cache.bz2
/usr/share/doc/HTML/it/kioslave5/ldap/index.docbook
/usr/share/doc/HTML/ko/kioslave5/ldap/index.cache.bz2
/usr/share/doc/HTML/ko/kioslave5/ldap/index.docbook
/usr/share/doc/HTML/nl/kioslave5/ldap/index.cache.bz2
/usr/share/doc/HTML/nl/kioslave5/ldap/index.docbook
/usr/share/doc/HTML/pt/kioslave5/ldap/index.cache.bz2
/usr/share/doc/HTML/pt/kioslave5/ldap/index.docbook
/usr/share/doc/HTML/pt_BR/kioslave5/ldap/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kioslave5/ldap/index.docbook
/usr/share/doc/HTML/ru/kioslave5/ldap/index.cache.bz2
/usr/share/doc/HTML/ru/kioslave5/ldap/index.docbook
/usr/share/doc/HTML/sr/kioslave5/ldap/index.cache.bz2
/usr/share/doc/HTML/sr/kioslave5/ldap/index.docbook
/usr/share/doc/HTML/sv/kioslave5/ldap/index.cache.bz2
/usr/share/doc/HTML/sv/kioslave5/ldap/index.docbook
/usr/share/doc/HTML/uk/kioslave5/ldap/index.cache.bz2
/usr/share/doc/HTML/uk/kioslave5/ldap/index.docbook

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Ldap.so.5
/usr/lib64/libKF5Ldap.so.5.17.2
/usr/lib64/qt5/plugins/kf5/kio/ldap.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kldap/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kldap/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/kldap/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kldap/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kldap/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3

%files locales -f kio_ldap.lang -f libkldap5.lang
%defattr(-,root,root,-)

