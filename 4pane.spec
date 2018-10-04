%global _disable_rebuild_configure 1
%define oname 4Pane

Summary:	A quad-panel detailed-list file manager for linux
Name:		4pane
Version:	5.0
Release:	1
License:	GPLv3+
Group:		File tools
Url:		http://www.4pane.co.uk
Source0:	https://datapacket.dl.sourceforge.net/project/fourpane/%{version}/4pane-%{version}.tar.gz
BuildRequires:	wxgtku3.0-devel
BuildRequires:	pkgconfig(liblzma)

%description
4Pane is a detailed-list file manager which displays directories and files
in separate panes. Generally two pairs of these twin-panes are displayed at
a time, allowing easy dragging/pasting of files. 4Pane aims to be fast and
fully-featured without bloat.

%files -f %{oname}.lang
%{_bindir}/%{name}
%{_datadir}/%{oname}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/4Pane.appdata.xml
%{_datadir}/icons/hicolor/*/apps/4Pane.*
%{_miconsdir}/%{name}.xpm
%{_iconsdir}/%{name}.xpm
%{_liconsdir}/%{name}.png
%{_datadir}/doc/%{oname}

#----------------------------------------------------------------------------

%prep
%setup -q
cd .build
./autogen.sh

%build
%configure
%make CXX="%{__cxx} %{optflags}"

%install
%makeinstall_std

mv %{buildroot}%{_bindir}/%{oname} %{buildroot}%{_bindir}/%{name}

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=%{name}
GenericName=File Manager
Comment=A four-pane file manager
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
StartupNotify=false
Categories=FileManager;Utility;
EOF

# icons
install -D -m 644 bitmaps/%{oname}Icon48.png %{buildroot}%{_liconsdir}/%{name}.png
install -D -m 644 bitmaps/%{oname}Icon32.xpm %{buildroot}%{_iconsdir}/%{name}.xpm
install -D -m 644 bitmaps/%{oname}Icon16.xpm %{buildroot}%{_miconsdir}/%{name}.xpm

%find_lang %{oname}
