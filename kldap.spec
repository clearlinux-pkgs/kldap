#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: 5424026
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kldap
Version  : 24.12.0
Release  : 79
URL      : https://download.kde.org/stable/release-service/24.12.0/src/kldap-24.12.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.12.0/src/kldap-24.12.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.12.0/src/kldap-24.12.0.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : LDAP access API for KDE
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 LGPL-2.0 MIT
Requires: kldap-data = %{version}-%{release}
Requires: kldap-lib = %{version}-%{release}
Requires: kldap-license = %{version}-%{release}
Requires: kldap-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : openldap-dev
BuildRequires : pkgconfig(libsasl2)
BuildRequires : pkgconfig(libsecret-1)
BuildRequires : qt6base-dev
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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n kldap-24.12.0
cd %{_builddir}/kldap-24.12.0
pushd ..
cp -a kldap-24.12.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1735220641
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
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
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
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
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
export SOURCE_DATE_EPOCH=1735220641
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kldap
cp %{_builddir}/kldap-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kldap/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kldap-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kldap/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/kldap-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kldap/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kldap-%{version}/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/kldap/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3 || :
cp %{_builddir}/kldap-%{version}/README.md.license %{buildroot}/usr/share/package-licenses/kldap/cadc9e08cb956c041f87922de84b9206d9bbffb2 || :
cp %{_builddir}/kldap-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/kldap/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kio_ldap
%find_lang libkldap6
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories6/kldap.categories
/usr/share/qlogging-categories6/kldap.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KPim6/KLDAPCore/KLDAPCore/Ber
/usr/include/KPim6/KLDAPCore/KLDAPCore/LdapActivitiesAbstract
/usr/include/KPim6/KLDAPCore/KLDAPCore/LdapClient
/usr/include/KPim6/KLDAPCore/KLDAPCore/LdapClientSearch
/usr/include/KPim6/KLDAPCore/KLDAPCore/LdapClientSearchConfig
/usr/include/KPim6/KLDAPCore/KLDAPCore/LdapClientSearchConfigReadConfigJob
/usr/include/KPim6/KLDAPCore/KLDAPCore/LdapClientSearchConfigWriteConfigJob
/usr/include/KPim6/KLDAPCore/KLDAPCore/LdapConnection
/usr/include/KPim6/KLDAPCore/KLDAPCore/LdapControl
/usr/include/KPim6/KLDAPCore/KLDAPCore/LdapDN
/usr/include/KPim6/KLDAPCore/KLDAPCore/LdapDefs
/usr/include/KPim6/KLDAPCore/KLDAPCore/LdapModel
/usr/include/KPim6/KLDAPCore/KLDAPCore/LdapObject
/usr/include/KPim6/KLDAPCore/KLDAPCore/LdapOperation
/usr/include/KPim6/KLDAPCore/KLDAPCore/LdapSearch
/usr/include/KPim6/KLDAPCore/KLDAPCore/LdapSearchClientReadConfigServerJob
/usr/include/KPim6/KLDAPCore/KLDAPCore/LdapServer
/usr/include/KPim6/KLDAPCore/KLDAPCore/LdapSortProxyModel
/usr/include/KPim6/KLDAPCore/KLDAPCore/LdapUrl
/usr/include/KPim6/KLDAPCore/KLDAPCore/Ldif
/usr/include/KPim6/KLDAPCore/kldap_core_version.h
/usr/include/KPim6/KLDAPCore/kldapcore/ber.h
/usr/include/KPim6/KLDAPCore/kldapcore/kldap_core_export.h
/usr/include/KPim6/KLDAPCore/kldapcore/ldapactivitiesabstract.h
/usr/include/KPim6/KLDAPCore/kldapcore/ldapclient.h
/usr/include/KPim6/KLDAPCore/kldapcore/ldapclientsearch.h
/usr/include/KPim6/KLDAPCore/kldapcore/ldapclientsearchconfig.h
/usr/include/KPim6/KLDAPCore/kldapcore/ldapclientsearchconfigreadconfigjob.h
/usr/include/KPim6/KLDAPCore/kldapcore/ldapclientsearchconfigwriteconfigjob.h
/usr/include/KPim6/KLDAPCore/kldapcore/ldapconnection.h
/usr/include/KPim6/KLDAPCore/kldapcore/ldapcontrol.h
/usr/include/KPim6/KLDAPCore/kldapcore/ldapdefs.h
/usr/include/KPim6/KLDAPCore/kldapcore/ldapdn.h
/usr/include/KPim6/KLDAPCore/kldapcore/ldapmodel.h
/usr/include/KPim6/KLDAPCore/kldapcore/ldapobject.h
/usr/include/KPim6/KLDAPCore/kldapcore/ldapoperation.h
/usr/include/KPim6/KLDAPCore/kldapcore/ldapsearch.h
/usr/include/KPim6/KLDAPCore/kldapcore/ldapsearchclientreadconfigserverjob.h
/usr/include/KPim6/KLDAPCore/kldapcore/ldapserver.h
/usr/include/KPim6/KLDAPCore/kldapcore/ldapsortproxymodel.h
/usr/include/KPim6/KLDAPCore/kldapcore/ldapurl.h
/usr/include/KPim6/KLDAPCore/kldapcore/ldif.h
/usr/include/KPim6/KLDAPWidgets/KLDAPWidgets/AddHostDialog
/usr/include/KPim6/KLDAPWidgets/KLDAPWidgets/LdapActivitiesAbstractPlugin
/usr/include/KPim6/KLDAPWidgets/KLDAPWidgets/LdapConfigWidget
/usr/include/KPim6/KLDAPWidgets/KLDAPWidgets/LdapConfigureWidgetNg
/usr/include/KPim6/KLDAPWidgets/kldap_widgets_version.h
/usr/include/KPim6/KLDAPWidgets/kldapwidgets/addhostdialog.h
/usr/include/KPim6/KLDAPWidgets/kldapwidgets/kldapwidgets_export.h
/usr/include/KPim6/KLDAPWidgets/kldapwidgets/ldapactivitiesabstractplugin.h
/usr/include/KPim6/KLDAPWidgets/kldapwidgets/ldapconfigurewidgetng.h
/usr/include/KPim6/KLDAPWidgets/kldapwidgets/ldapconfigwidget.h
/usr/lib64/cmake/KPim6LdapCore/KPim6LdapCoreConfig.cmake
/usr/lib64/cmake/KPim6LdapCore/KPim6LdapCoreConfigVersion.cmake
/usr/lib64/cmake/KPim6LdapCore/KPim6LdapCoreTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim6LdapCore/KPim6LdapCoreTargets.cmake
/usr/lib64/cmake/KPim6LdapWidgets/KPim6LdapWidgetsConfig.cmake
/usr/lib64/cmake/KPim6LdapWidgets/KPim6LdapWidgetsConfigVersion.cmake
/usr/lib64/cmake/KPim6LdapWidgets/KPim6LdapWidgetsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim6LdapWidgets/KPim6LdapWidgetsTargets.cmake
/usr/lib64/libKPim6LdapCore.so
/usr/lib64/libKPim6LdapWidgets.so

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kioworker6/ldap/index.cache.bz2
/usr/share/doc/HTML/ca/kioworker6/ldap/index.docbook
/usr/share/doc/HTML/de/kioworker6/ldap/index.cache.bz2
/usr/share/doc/HTML/de/kioworker6/ldap/index.docbook
/usr/share/doc/HTML/en/kioworker6/ldap/index.cache.bz2
/usr/share/doc/HTML/en/kioworker6/ldap/index.docbook
/usr/share/doc/HTML/es/kioworker6/ldap/index.cache.bz2
/usr/share/doc/HTML/es/kioworker6/ldap/index.docbook
/usr/share/doc/HTML/et/kioworker6/ldap/index.cache.bz2
/usr/share/doc/HTML/et/kioworker6/ldap/index.docbook
/usr/share/doc/HTML/fr/kioworker6/ldap/index.cache.bz2
/usr/share/doc/HTML/fr/kioworker6/ldap/index.docbook
/usr/share/doc/HTML/gl/kioworker6/ldap/index.cache.bz2
/usr/share/doc/HTML/gl/kioworker6/ldap/index.docbook
/usr/share/doc/HTML/it/kioworker6/ldap/index.cache.bz2
/usr/share/doc/HTML/it/kioworker6/ldap/index.docbook
/usr/share/doc/HTML/ko/kioworker6/ldap/index.cache.bz2
/usr/share/doc/HTML/ko/kioworker6/ldap/index.docbook
/usr/share/doc/HTML/nl/kioworker6/ldap/index.cache.bz2
/usr/share/doc/HTML/nl/kioworker6/ldap/index.docbook
/usr/share/doc/HTML/pt/kioworker6/ldap/index.cache.bz2
/usr/share/doc/HTML/pt/kioworker6/ldap/index.docbook
/usr/share/doc/HTML/pt_BR/kioworker6/ldap/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kioworker6/ldap/index.docbook
/usr/share/doc/HTML/ru/kioworker6/ldap/index.cache.bz2
/usr/share/doc/HTML/ru/kioworker6/ldap/index.docbook
/usr/share/doc/HTML/sl/kioworker6/ldap/index.cache.bz2
/usr/share/doc/HTML/sl/kioworker6/ldap/index.docbook
/usr/share/doc/HTML/sr/kioworker6/ldap/index.cache.bz2
/usr/share/doc/HTML/sr/kioworker6/ldap/index.docbook
/usr/share/doc/HTML/sr@latin/kioworker6/ldap/index.cache.bz2
/usr/share/doc/HTML/sr@latin/kioworker6/ldap/index.docbook
/usr/share/doc/HTML/sv/kioworker6/ldap/index.cache.bz2
/usr/share/doc/HTML/sv/kioworker6/ldap/index.docbook
/usr/share/doc/HTML/tr/kioworker6/ldap/index.cache.bz2
/usr/share/doc/HTML/tr/kioworker6/ldap/index.docbook
/usr/share/doc/HTML/uk/kioworker6/ldap/index.cache.bz2
/usr/share/doc/HTML/uk/kioworker6/ldap/index.docbook

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKPim6LdapCore.so.6.3.0
/V3/usr/lib64/libKPim6LdapWidgets.so.6.3.0
/V3/usr/lib64/qt6/plugins/kf6/kio/ldap.so
/usr/lib64/libKPim6LdapCore.so.6
/usr/lib64/libKPim6LdapCore.so.6.3.0
/usr/lib64/libKPim6LdapWidgets.so.6
/usr/lib64/libKPim6LdapWidgets.so.6.3.0
/usr/lib64/qt6/plugins/kf6/kio/ldap.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kldap/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kldap/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/kldap/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kldap/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kldap/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
/usr/share/package-licenses/kldap/cadc9e08cb956c041f87922de84b9206d9bbffb2

%files locales -f kio_ldap.lang -f libkldap6.lang
%defattr(-,root,root,-)

