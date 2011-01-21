%define		qtver		4.7.1
%define		kdever		4.5.5

Summary:	Xine backend for Phonon
Summary(pl.UTF-8):	Wtyczka Xine dla Phonona
Name:		phonon-backend-xine
Version:	4.4.4
Release:	1
License:	LGPL 2.1
Group:		Libraries
Source0:	ftp://ftp.kde.org/pub/kde/stable/phonon/%{name}/%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	b127104e67538e573adeed3b2fb3bf55
#URL:		http://
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdebase-workspace-devel >= %{kdever}
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	phonon-devel >= 4.4.4
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	xine-lib-devel >= 2:1.1.15-4
Provides:	qt4-phonon-backend = %{version}
Requires:	xine-decode-ogg
Obsoletes:	kde4-phonon-xine
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xine backend for Phonon.

%description -l pl.UTF-8
Wtyczka Xine dla Phonona.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/plugins/phonon_backend/phonon_xine.so
%{_datadir}/kde4/services/phononbackends/xine.desktop
