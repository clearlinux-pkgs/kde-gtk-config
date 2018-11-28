#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : kde-gtk-config
Version  : 5.14.4
Release  : 10
URL      : https://download.kde.org/stable/plasma/5.14.4/kde-gtk-config-5.14.4.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.14.4/kde-gtk-config-5.14.4.tar.xz
Source99 : https://download.kde.org/stable/plasma/5.14.4/kde-gtk-config-5.14.4.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: kde-gtk-config-data = %{version}-%{release}
Requires: kde-gtk-config-lib = %{version}-%{release}
Requires: kde-gtk-config-license = %{version}-%{release}
Requires: kde-gtk-config-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : freetype-dev
BuildRequires : gsettings-desktop-schemas
BuildRequires : gtk+-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(atk)
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(pango)
BuildRequires : qtbase-dev mesa-dev

%description
KDE GTK CONFIG v1.7
----------------------
This program it's licensed under GPLv3

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


%package locales
Summary: locales components for the kde-gtk-config package.
Group: Default

%description locales
locales components for the kde-gtk-config package.


%prep
%setup -q -n kde-gtk-config-5.14.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1543392198
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1543392198
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kde-gtk-config
cp COPYING %{buildroot}/usr/share/package-licenses/kde-gtk-config/COPYING
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/kde-gtk-config/COPYING.LIB
pushd clr-build
%make_install
popd
%find_lang kde-gtk-config

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/gtk3_preview
/usr/lib64/libexec/gtk_preview
/usr/lib64/libexec/reload_gtk_apps

%files data
%defattr(-,root,root,-)
/usr/share/icons/hicolor/128x128/apps/kde-gtk-config.png
/usr/share/icons/hicolor/16x16/apps/kde-gtk-config.png
/usr/share/icons/hicolor/22x22/apps/kde-gtk-config.png
/usr/share/icons/hicolor/24x24/apps/kde-gtk-config.png
/usr/share/icons/hicolor/256x256/apps/kde-gtk-config.png
/usr/share/icons/hicolor/32x32/apps/kde-gtk-config.png
/usr/share/icons/hicolor/48x48/apps/kde-gtk-config.png
/usr/share/icons/hicolor/64x64/apps/kde-gtk-config.png
/usr/share/icons/hicolor/8x8/apps/kde-gtk-config.png
/usr/share/icons/hicolor/scalable/apps/kde-gtk-config.svgz
/usr/share/kcm-gtk-module/preview.ui
/usr/share/kservices5/kde-gtk-config.desktop
/usr/share/xdg/cgcgtk3.knsrc
/usr/share/xdg/cgctheme.knsrc

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kcm_kdegtkconfig.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kde-gtk-config/COPYING
/usr/share/package-licenses/kde-gtk-config/COPYING.LIB

%files locales -f kde-gtk-config.lang
%defattr(-,root,root,-)

