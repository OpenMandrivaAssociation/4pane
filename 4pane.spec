%define oname 4Pane

Summary:	A quad-panel detailed-list file manager for linux
Name:		4pane
Version:	2.0
Release:	2
License:	GPLv3+
Group:		File tools
Url:		http://www.4pane.co.uk
Source0:	http://sourceforge.net/projects/fourpane/files/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	wxgtku2.8-devel
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
%{_miconsdir}/%{name}.xpm
%{_iconsdir}/%{name}.xpm
%{_liconsdir}/%{name}.png
%{_datadir}/doc/%{oname}

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x --disable-desktop
%make CXX="g++ %{optflags}"

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

