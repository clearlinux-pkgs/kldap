#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: da8b975
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kldap
Version  : 23.08.5
Release  : 66
URL      : https://download.kde.org/stable/release-service/23.08.5/src/kldap-23.08.5.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.08.5/src/kldap-23.08.5.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.08.5/src/kldap-23.08.5.tar.xz.sig
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
BuildRequires : openldap-dev
BuildRequires : pkgconfig(libsecret-1)
BuildRequires : qtkeychain-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n kldap-23.08.5
cd %{_builddir}/kldap-23.08.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1708401588
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -std=gnu++98"
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -std=gnu++98"
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -std=gnu++98"
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1708401588
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kldap
cp %{_builddir}/kldap-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kldap/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kldap-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kldap/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/kldap-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kldap/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kldap-%{version}/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/kldap/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3 || :
cp %{_builddir}/kldap-%{version}/README.md.license %{buildroot}/usr/share/package-licenses/kldap/cadc9e08cb956c041f87922de84b9206d9bbffb2 || :
cp %{_builddir}/kldap-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/kldap/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kio_ldap
%find_lang libkldap5
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/kldap.categories
/usr/share/qlogging-categories5/kldap.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KPim5/KLDAP/KLDAP/AddHostDialog
/usr/include/KPim5/KLDAP/KLDAP/Ber
/usr/include/KPim5/KLDAP/KLDAP/LdapClient
/usr/include/KPim5/KLDAP/KLDAP/LdapClientSearch
/usr/include/KPim5/KLDAP/KLDAP/LdapClientSearchConfig
/usr/include/KPim5/KLDAP/KLDAP/LdapClientSearchConfigReadConfigJob
/usr/include/KPim5/KLDAP/KLDAP/LdapClientSearchConfigWriteConfigJob
/usr/include/KPim5/KLDAP/KLDAP/LdapConfigWidget
/usr/include/KPim5/KLDAP/KLDAP/LdapConfigureWidget
/usr/include/KPim5/KLDAP/KLDAP/LdapConnection
/usr/include/KPim5/KLDAP/KLDAP/LdapControl
/usr/include/KPim5/KLDAP/KLDAP/LdapDN
/usr/include/KPim5/KLDAP/KLDAP/LdapDefs
/usr/include/KPim5/KLDAP/KLDAP/LdapObject
/usr/include/KPim5/KLDAP/KLDAP/LdapOperation
/usr/include/KPim5/KLDAP/KLDAP/LdapSearch
/usr/include/KPim5/KLDAP/KLDAP/LdapSearchClientReadConfigServerJob
/usr/include/KPim5/KLDAP/KLDAP/LdapServer
/usr/include/KPim5/KLDAP/KLDAP/LdapUrl
/usr/include/KPim5/KLDAP/KLDAP/Ldif
/usr/include/KPim5/KLDAP/kldap/addhostdialog.h
/usr/include/KPim5/KLDAP/kldap/ber.h
/usr/include/KPim5/KLDAP/kldap/kldap_export.h
/usr/include/KPim5/KLDAP/kldap/ldapclient.h
/usr/include/KPim5/KLDAP/kldap/ldapclientsearch.h
/usr/include/KPim5/KLDAP/kldap/ldapclientsearchconfig.h
/usr/include/KPim5/KLDAP/kldap/ldapclientsearchconfigreadconfigjob.h
/usr/include/KPim5/KLDAP/kldap/ldapclientsearchconfigwriteconfigjob.h
/usr/include/KPim5/KLDAP/kldap/ldapconfigurewidget.h
/usr/include/KPim5/KLDAP/kldap/ldapconfigwidget.h
/usr/include/KPim5/KLDAP/kldap/ldapconnection.h
/usr/include/KPim5/KLDAP/kldap/ldapcontrol.h
/usr/include/KPim5/KLDAP/kldap/ldapdefs.h
/usr/include/KPim5/KLDAP/kldap/ldapdn.h
/usr/include/KPim5/KLDAP/kldap/ldapobject.h
/usr/include/KPim5/KLDAP/kldap/ldapoperation.h
/usr/include/KPim5/KLDAP/kldap/ldapsearch.h
/usr/include/KPim5/KLDAP/kldap/ldapsearchclientreadconfigserverjob.h
/usr/include/KPim5/KLDAP/kldap/ldapserver.h
/usr/include/KPim5/KLDAP/kldap/ldapurl.h
/usr/include/KPim5/KLDAP/kldap/ldif.h
/usr/include/KPim5/KLDAP/kldap_version.h
/usr/lib64/cmake/KPim5Ldap/KPim5LdapConfig.cmake
/usr/lib64/cmake/KPim5Ldap/KPim5LdapConfigVersion.cmake
/usr/lib64/cmake/KPim5Ldap/KPim5LdapTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim5Ldap/KPim5LdapTargets.cmake
/usr/lib64/libKPim5Ldap.so
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
/usr/share/doc/HTML/sr@latin/kioslave5/ldap/index.cache.bz2
/usr/share/doc/HTML/sr@latin/kioslave5/ldap/index.docbook
/usr/share/doc/HTML/sv/kioslave5/ldap/index.cache.bz2
/usr/share/doc/HTML/sv/kioslave5/ldap/index.docbook
/usr/share/doc/HTML/tr/kioslave5/ldap/index.cache.bz2
/usr/share/doc/HTML/tr/kioslave5/ldap/index.docbook
/usr/share/doc/HTML/uk/kioslave5/ldap/index.cache.bz2
/usr/share/doc/HTML/uk/kioslave5/ldap/index.docbook

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKPim5Ldap.so.5.24.5
/V3/usr/lib64/qt5/plugins/kf5/kio/ldap.so
/usr/lib64/libKPim5Ldap.so.5
/usr/lib64/libKPim5Ldap.so.5.24.5
/usr/lib64/qt5/plugins/kf5/kio/ldap.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kldap/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kldap/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/kldap/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kldap/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kldap/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
/usr/share/package-licenses/kldap/cadc9e08cb956c041f87922de84b9206d9bbffb2

%files locales -f kio_ldap.lang -f libkldap5.lang
%defattr(-,root,root,-)

