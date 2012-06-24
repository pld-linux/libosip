Summary:	The GNU oSIP library
Summary(pl):	Biblioteka GNU oSIP
Name:		libosip
Version:	0.7.9
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://osip.atosc.org/download/%{name}-%{version}.tar.gz
URL:		http://osip.atosc.org/
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is "the GNU oSIP library" (for Omnibus SIP). It has been designed
to provide the Internet Community a simple way to support the Session
Initiation Protocol. SIP is described in the RFC2543 which is
available at http://www.ietf.org/rfc/rfc2543.txt.

%description -l pl
To jest biblioteka GNU oSIP (Omnibus SIP). Zosta�a zaprojektowana, aby
dostarczy� Spo�eczno�ci Internetowej prost� obs�ug� protoko�u SIP.
Protok� SIP (Session Initiation Protocol) jest opisany w RFC2543.

%package devel
Summary:	The GNU oSIP library - development files
Summary(pl):	Pliki dla programist�w u�ywaj�cych GNU oSIP
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Development files for the GNU oSIP library.

%description devel -l pl
Pliki dla programist�w u�ywaj�cych biblioteki GNU oSIP.

%package static
Summary:	The GNU oSIP library - static version
Summary(pl):	Statyczna biblioteka GNU oSIP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of the GNU oSIP library.

%description static -l pl
Statyczna wersja biblioteki GNU oSIP.

%prep
%setup -q

%build
aclocal
%{__automake}
%{__autoconf}
%configure \
	--enable-semaphore 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz doc/*.html
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
