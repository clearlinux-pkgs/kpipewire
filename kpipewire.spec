#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : kpipewire
Version  : 5.27.7
Release  : 6
URL      : https://download.kde.org/stable/plasma/5.27.7/kpipewire-5.27.7.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.27.7/kpipewire-5.27.7.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.27.7/kpipewire-5.27.7.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-3.0 LGPL-2.1 LGPL-3.0
Requires: kpipewire-data = %{version}-%{release}
Requires: kpipewire-lib = %{version}-%{release}
Requires: kpipewire-license = %{version}-%{release}
Requires: kpipewire-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(egl)
BuildRequires : extra-cmake-modules pkgconfig(wayland-client)
BuildRequires : extra-cmake-modules qtwayland-dev
BuildRequires : extra-cmake-modules-data
BuildRequires : kwayland-dev
BuildRequires : libepoxy-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(gbm)
BuildRequires : pkgconfig(libavcodec)
BuildRequires : pkgconfig(libavformat)
BuildRequires : pkgconfig(libavutil)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libpipewire-0.3)
BuildRequires : pkgconfig(libswscale)
BuildRequires : plasma-wayland-protocols-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KPipeWire
Offers a set of convenient classes to use PipeWire (https://pipewire.org/) in Qt projects.

%package data
Summary: data components for the kpipewire package.
Group: Data

%description data
data components for the kpipewire package.


%package dev
Summary: dev components for the kpipewire package.
Group: Development
Requires: kpipewire-lib = %{version}-%{release}
Requires: kpipewire-data = %{version}-%{release}
Provides: kpipewire-devel = %{version}-%{release}
Requires: kpipewire = %{version}-%{release}
Requires: pipewire-dev

%description dev
dev components for the kpipewire package.


%package lib
Summary: lib components for the kpipewire package.
Group: Libraries
Requires: kpipewire-data = %{version}-%{release}
Requires: kpipewire-license = %{version}-%{release}

%description lib
lib components for the kpipewire package.


%package license
Summary: license components for the kpipewire package.
Group: Default

%description license
license components for the kpipewire package.


%package locales
Summary: locales components for the kpipewire package.
Group: Default

%description locales
locales components for the kpipewire package.


%prep
%setup -q -n kpipewire-5.27.7
cd %{_builddir}/kpipewire-5.27.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1690900432
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1690900432
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kpipewire
cp %{_builddir}/kpipewire-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kpipewire/3630f1ffcec0e075bf446b88c7b507b1287b571d || :
cp %{_builddir}/kpipewire-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kpipewire/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kpipewire-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kpipewire/fa05e58320cb7c64786b26396f4b992579a628bc || :
cp %{_builddir}/kpipewire-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kpipewire/0b71159e19bef95069e18d17296291916e89b5cd || :
cp %{_builddir}/kpipewire-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kpipewire/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kpipewire-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kpipewire/e458941548e0864907e654fa2e192844ae90fc32 || :
pushd clr-build
%make_install
popd
%find_lang kpipewire5

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/kpipewire.categories
/usr/share/qlogging-categories5/kpipewirerecord.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KPipeWire/DmaBufHandler
/usr/include/KPipeWire/PipeWireRecord
/usr/include/KPipeWire/PipeWireSourceItem
/usr/include/KPipeWire/PipeWireSourceStream
/usr/include/KPipeWire/dmabufhandler.h
/usr/include/KPipeWire/kpipewire_export.h
/usr/include/KPipeWire/kpipewiredmabuf_export.h
/usr/include/KPipeWire/pipewirerecord.h
/usr/include/KPipeWire/pipewiresourceitem.h
/usr/include/KPipeWire/pipewiresourcestream.h
/usr/lib64/cmake/KPipeWire/KPipeWireConfig.cmake
/usr/lib64/cmake/KPipeWire/KPipeWireConfigVersion.cmake
/usr/lib64/cmake/KPipeWire/KPipeWireTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPipeWire/KPipeWireTargets.cmake
/usr/lib64/libKPipeWire.so
/usr/lib64/libKPipeWireDmaBuf.so
/usr/lib64/libKPipeWireRecord.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKPipeWire.so.5
/usr/lib64/libKPipeWire.so.5.27.7
/usr/lib64/libKPipeWireDmaBuf.so.5
/usr/lib64/libKPipeWireDmaBuf.so.5.27.7
/usr/lib64/libKPipeWireRecord.so.5
/usr/lib64/libKPipeWireRecord.so.5.27.7
/usr/lib64/qt5/qml/org/kde/pipewire/libKPipeWireDeclarative.so
/usr/lib64/qt5/qml/org/kde/pipewire/qmldir
/usr/lib64/qt5/qml/org/kde/pipewire/record/libKPipeWireRecordDeclarative.so
/usr/lib64/qt5/qml/org/kde/pipewire/record/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kpipewire/0b71159e19bef95069e18d17296291916e89b5cd
/usr/share/package-licenses/kpipewire/3630f1ffcec0e075bf446b88c7b507b1287b571d
/usr/share/package-licenses/kpipewire/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kpipewire/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/kpipewire/fa05e58320cb7c64786b26396f4b992579a628bc

%files locales -f kpipewire5.lang
%defattr(-,root,root,-)

