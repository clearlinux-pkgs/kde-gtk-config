#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : kde-gtk-config
Version  : 5.27.0
Release  : 81
URL      : https://download.kde.org/stable/plasma/5.27.0/kde-gtk-config-5.27.0.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.27.0/kde-gtk-config-5.27.0.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.27.0/kde-gtk-config-5.27.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0
Requires: kde-gtk-config-data = %{version}-%{release}
Requires: kde-gtk-config-lib = %{version}-%{release}
Requires: kde-gtk-config-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kdecoration-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
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
%setup -q -n kde-gtk-config-5.27.0
cd %{_builddir}/kde-gtk-config-5.27.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1676683046
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1676683046
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
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/lib64/kconf_update_bin/gtk_theme
/usr/lib64/kconf_update_bin/remove_deprecated_gtk4_option
/usr/lib64/libexec/gtk3_preview

%files data
%defattr(-,root,root,-)
/usr/share/kcm-gtk-module/preview.ui
/usr/share/kconf_update/gtkconfig.upd
/usr/share/kconf_update/remove_window_decorations_from_gtk_css.sh
/usr/share/themes/Breeze/window_decorations.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/gtk-3.0/modules/libcolorreload-gtk-module.so
/usr/lib64/gtk-3.0/modules/libwindow-decorations-gtk-module.so
/usr/lib64/qt5/plugins/kf5/kded/gtkconfig.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kde-gtk-config/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/kde-gtk-config/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/kde-gtk-config/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e
/usr/share/package-licenses/kde-gtk-config/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/kde-gtk-config/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kde-gtk-config/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kde-gtk-config/e712eadfab0d2357c0f50f599ef35ee0d87534cb
