#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v27
# autospec commit: 65cf152
#
# Source0 file verified with key 0x11968C44928CAEFC (bshah@mykolab.com)
#
Name     : kpipewire
Version  : 6.4.0
Release  : 67
URL      : https://download.kde.org/stable/plasma/6.4.0/kpipewire-6.4.0.tar.xz
Source0  : https://download.kde.org/stable/plasma/6.4.0/kpipewire-6.4.0.tar.xz
Source1  : https://download.kde.org/stable/plasma/6.4.0/kpipewire-6.4.0.tar.xz.sig
Source2  : 11968C44928CAEFC.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-3.0 LGPL-2.1 LGPL-3.0
Requires: kpipewire-data = %{version}-%{release}
Requires: kpipewire-lib = %{version}-%{release}
Requires: kpipewire-license = %{version}-%{release}
Requires: kpipewire-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : libepoxy-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(gbm)
BuildRequires : pkgconfig(libavcodec)
BuildRequires : pkgconfig(libavfilter)
BuildRequires : pkgconfig(libavformat)
BuildRequires : pkgconfig(libavutil)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libpipewire-0.3)
BuildRequires : pkgconfig(libswscale)
BuildRequires : pkgconfig(libva)
BuildRequires : pkgconfig(libva-drm)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : plasma-wayland-protocols-dev
BuildRequires : qt6base-dev
BuildRequires : qt6wayland-dev
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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 11968C44928CAEFC' gpg.status
%setup -q -n kpipewire-6.4.0
cd %{_builddir}/kpipewire-6.4.0
pushd ..
cp -a kpipewire-6.4.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1750182086
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
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
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
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
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1750182086
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kpipewire
cp %{_builddir}/kpipewire-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kpipewire/3630f1ffcec0e075bf446b88c7b507b1287b571d || :
cp %{_builddir}/kpipewire-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kpipewire/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kpipewire-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kpipewire/fa05e58320cb7c64786b26396f4b992579a628bc || :
cp %{_builddir}/kpipewire-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kpipewire/0b71159e19bef95069e18d17296291916e89b5cd || :
cp %{_builddir}/kpipewire-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kpipewire/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kpipewire-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kpipewire/e458941548e0864907e654fa2e192844ae90fc32 || :
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
%find_lang kpipewire6
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories6/kpipewire.categories
/usr/share/qlogging-categories6/kpipewirerecord.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KPipeWire/DmaBufHandler
/usr/include/KPipeWire/PipeWireBaseEncodedStream
/usr/include/KPipeWire/PipeWireEncodedStream
/usr/include/KPipeWire/PipeWireRecord
/usr/include/KPipeWire/PipeWireSourceItem
/usr/include/KPipeWire/PipeWireSourceStream
/usr/include/KPipeWire/dmabufhandler.h
/usr/include/KPipeWire/kpipewire_export.h
/usr/include/KPipeWire/kpipewire_version.h
/usr/include/KPipeWire/kpipewiredmabuf_export.h
/usr/include/KPipeWire/pipewirebaseencodedstream.h
/usr/include/KPipeWire/pipewireencodedstream.h
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
/V3/usr/lib64/libKPipeWire.so.6.4.0
/V3/usr/lib64/libKPipeWireDmaBuf.so.6.4.0
/V3/usr/lib64/libKPipeWireRecord.so.6.4.0
/V3/usr/lib64/qt6/qml/org/kde/pipewire/libKPipeWireplugin.so
/V3/usr/lib64/qt6/qml/org/kde/pipewire/monitor/libKPipeWireMonitorDeclarative.so
/V3/usr/lib64/qt6/qml/org/kde/pipewire/record/libKPipeWireRecordplugin.so
/usr/lib64/libKPipeWire.so.6
/usr/lib64/libKPipeWire.so.6.4.0
/usr/lib64/libKPipeWireDmaBuf.so.6
/usr/lib64/libKPipeWireDmaBuf.so.6.4.0
/usr/lib64/libKPipeWireRecord.so.6
/usr/lib64/libKPipeWireRecord.so.6.4.0
/usr/lib64/qt6/qml/org/kde/pipewire/KPipeWire.qmltypes
/usr/lib64/qt6/qml/org/kde/pipewire/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/pipewire/libKPipeWireplugin.so
/usr/lib64/qt6/qml/org/kde/pipewire/monitor/KPipeWireMonitorDeclarative.qmltypes
/usr/lib64/qt6/qml/org/kde/pipewire/monitor/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/pipewire/monitor/libKPipeWireMonitorDeclarative.so
/usr/lib64/qt6/qml/org/kde/pipewire/monitor/qmldir
/usr/lib64/qt6/qml/org/kde/pipewire/qmldir
/usr/lib64/qt6/qml/org/kde/pipewire/record/KPipeWireRecord.qmltypes
/usr/lib64/qt6/qml/org/kde/pipewire/record/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/pipewire/record/libKPipeWireRecordplugin.so
/usr/lib64/qt6/qml/org/kde/pipewire/record/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kpipewire/0b71159e19bef95069e18d17296291916e89b5cd
/usr/share/package-licenses/kpipewire/3630f1ffcec0e075bf446b88c7b507b1287b571d
/usr/share/package-licenses/kpipewire/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kpipewire/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/kpipewire/fa05e58320cb7c64786b26396f4b992579a628bc

%files locales -f kpipewire6.lang
%defattr(-,root,root,-)

