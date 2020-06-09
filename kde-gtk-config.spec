#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : kde-gtk-config
Version  : 5.19.0
Release  : 40
URL      : https://download.kde.org/stable/plasma/5.19.0/kde-gtk-config-5.19.0.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.19.0/kde-gtk-config-5.19.0.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.19.0/kde-gtk-config-5.19.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: kde-gtk-config-data = %{version}-%{release}
Requires: kde-gtk-config-lib = %{version}-%{release}
Requires: kde-gtk-config-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gsettings-desktop-schemas-dev
BuildRequires : kconfig-dev
BuildRequires : kconfigwidgets-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kdbusaddons-dev
BuildRequires : kguiaddons-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : qtbase-dev mesa-dev

%description
No detailed description available

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
%setup -q -n kde-gtk-config-5.19.0
cd %{_builddir}/kde-gtk-config-5.19.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1591741658
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1591741658
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kde-gtk-config
cp %{_builddir}/kde-gtk-config-5.19.0/COPYING %{buildroot}/usr/share/package-licenses/kde-gtk-config/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/kde-gtk-config-5.19.0/COPYING.LIB %{buildroot}/usr/share/package-licenses/kde-gtk-config/01a6b4bf79aca9b556822601186afab86e8c4fbf
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/lib64/kconf_update_bin/gtk_theme
/usr/lib64/libexec/gtk3_preview
/usr/lib64/libexec/gtk_preview
/usr/lib64/libexec/reload_gtk_apps

%files data
%defattr(-,root,root,-)
/usr/share/kcm-gtk-module/preview.ui
/usr/share/kconf_update/gtkconfig.upd

%files lib
%defattr(-,root,root,-)
/usr/lib64/gtk-3.0/modules/libcolorreload-gtk-module.so
/usr/lib64/qt5/plugins/kf5/kded/gtkconfig.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kde-gtk-config/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/kde-gtk-config/4cc77b90af91e615a64ae04893fdffa7939db84c
