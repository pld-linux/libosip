Summary:	The GNU oSIP library
Name:		libosip
Version:	0.8.3
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
To jest biblioteka zaprojektowana tak, aby dostarczyæ Spo³eczno¶ci
Internetowej prost± obs³ugê protoko³u SIP.

%package devel
Summary:	The GNU oSIP library - development files
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Development files for the GNU oSIP library.

%package static
Summary:	The GNU oSIP library - static version
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description static
Static version of the GNU oSIP library.

%prep
%setup -q

%build
aclocal
automake -a -c
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS BUGS NEWS README TODO

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
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
