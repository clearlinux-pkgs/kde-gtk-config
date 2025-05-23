#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v26
# autospec commit: 99a7985
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : kde-gtk-config
Version  : 6.3.5
Release  : 126
URL      : https://download.kde.org/stable/plasma/6.3.5/kde-gtk-config-6.3.5.tar.xz
Source0  : https://download.kde.org/stable/plasma/6.3.5/kde-gtk-config-6.3.5.tar.xz
Source1  : https://download.kde.org/stable/plasma/6.3.5/kde-gtk-config-6.3.5.tar.xz.sig
Source2  : D7574483BB57B18D.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0
Requires: kde-gtk-config-data = %{version}-%{release}
Requires: kde-gtk-config-lib = %{version}-%{release}
Requires: kde-gtk-config-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kdecoration-dev
BuildRequires : libICE-dev
BuildRequires : libSM-dev
BuildRequires : libX11-dev
BuildRequires : libXScrnSaver-dev
BuildRequires : libXau-dev
BuildRequires : libXcomposite-dev
BuildRequires : libXcursor-dev
BuildRequires : libXdamage-dev
BuildRequires : libXdmcp-dev
BuildRequires : libXext-dev
BuildRequires : libXfixes-dev
BuildRequires : libXft-dev
BuildRequires : libXi-dev
BuildRequires : libXinerama-dev
BuildRequires : libXmu-dev
BuildRequires : libXpm-dev
BuildRequires : libXrandr-dev
BuildRequires : libXrender-dev
BuildRequires : libXres-dev
BuildRequires : libXt-dev
BuildRequires : libXtst-dev
BuildRequires : libXv-dev
BuildRequires : libXxf86vm-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : qt6base-dev
BuildRequires : sassc
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KDE GTK Configurator
This project aims to provide a smooth experience for the users of GNOME/GTK applications on Plasma Desktop.

%package data
Summary: data components for the kde-gtk-config package.
Group: Data

%description data
data components for the kde-gtk-config package.


%package lib
Summary: lib components for the kde-gtk-config package.
Group: Libraries
Requires: kde-gtk-config-data = %{version}-%{release}
Requires: kde-gtk-config-license = %{version}-%{release}

%description lib
lib components for the kde-gtk-config package.


%package license
Summary: license components for the kde-gtk-config package.
Group: Default

%description license
license components for the kde-gtk-config package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) D7574483BB57B18D' gpg.status
%setup -q -n kde-gtk-config-6.3.5
cd %{_builddir}/kde-gtk-config-6.3.5
pushd ..
cp -a kde-gtk-config-6.3.5 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1747162823
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
export SOURCE_DATE_EPOCH=1747162823
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kde-gtk-config
cp %{_builddir}/kde-gtk-config-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/kde-gtk-config/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e || :
cp %{_builddir}/kde-gtk-config-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kde-gtk-config/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kde-gtk-config-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kde-gtk-config/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kde-gtk-config-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kde-gtk-config/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/kde-gtk-config-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kde-gtk-config/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/kde-gtk-config-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kde-gtk-config/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/kde-gtk-config-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kde-gtk-config/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/kde-gtk-config-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kde-gtk-config/7d9831e05094ce723947d729c2a46a09d6e90275 || :
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
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/V3/usr/lib64/kconf_update_bin/gtk_theme
/V3/usr/lib64/kconf_update_bin/remove_deprecated_gtk4_option
/V3/usr/lib64/libexec/gtk3_preview
/usr/lib64/kconf_update_bin/gtk_theme
/usr/lib64/kconf_update_bin/remove_deprecated_gtk4_option
/usr/lib64/libexec/gtk3_preview

%files data
%defattr(-,root,root,-)
/usr/share/kcm-gtk-module/preview.ui
/usr/share/kconf_update/gtkconfig.upd
/usr/share/kconf_update/remove_window_decorations_from_gtk_css.sh
/usr/share/qlogging-categories6/kde-gtk-config.categories
/usr/share/themes/Breeze/window_decorations.css

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/gtk-3.0/modules/libcolorreload-gtk-module.so
/V3/usr/lib64/gtk-3.0/modules/libwindow-decorations-gtk-module.so
/V3/usr/lib64/qt6/plugins/kf6/kded/gtkconfig.so
/usr/lib64/gtk-3.0/modules/libcolorreload-gtk-module.so
/usr/lib64/gtk-3.0/modules/libwindow-decorations-gtk-module.so
/usr/lib64/qt6/plugins/kf6/kded/gtkconfig.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kde-gtk-config/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/kde-gtk-config/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/kde-gtk-config/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e
/usr/share/package-licenses/kde-gtk-config/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/kde-gtk-config/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kde-gtk-config/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kde-gtk-config/e712eadfab0d2357c0f50f599ef35ee0d87534cb
