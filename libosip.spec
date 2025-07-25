Summary:	The GNU oSIP library
Summary(pl.UTF-8):	Biblioteka GNU oSIP
Name:		libosip
Version:	0.9.7
Release:	4
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnu.org/gnu/osip/%{name}-%{version}.tar.gz
# Source0-md5:	1c97d2bbc042ba318b1ad422b6109537
Patch0:		%{name}-docbook2man.patch
Patch1:		%{name}-nolibs.patch
URL:		http://www.fsf.org/software/osip/osip.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool >= 1:1.4.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is "the GNU oSIP library" (for Omnibus SIP). It has been designed
to provide the Internet Community a simple way to support the Session
Initiation Protocol. SIP is described in the RFC2543 which is
available at http://www.ietf.org/rfc/rfc2543.txt.

%description -l pl.UTF-8
To jest biblioteka GNU oSIP (Omnibus SIP). Została zaprojektowana, aby
dostarczyć Społeczności Internetowej prostą obsługę protokołu SIP.
Protokół SIP (Session Initiation Protocol) jest opisany w RFC2543.

%package devel
Summary:	The GNU oSIP library - development files
Summary(pl.UTF-8):	Pliki dla programistów używających GNU oSIP
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for the GNU oSIP library.

%description devel -l pl.UTF-8
Pliki dla programistów używających biblioteki GNU oSIP.

%package static
Summary:	The GNU oSIP library - static version
Summary(pl.UTF-8):	Statyczna biblioteka GNU oSIP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of the GNU oSIP library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki GNU oSIP.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

rm -f acinclude.m4

%build
%{__libtoolize}
%{__aclocal} -I scripts
%{__autoconf}
%{__automake}
%configure \
	--enable-semaphore \
	--enable-pthread \
	--%{?debug:en}%{!?debug:dis}able-debug

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_mandir}/man{1,3}
mv -f $RPM_BUILD_ROOT%{_mandir}/man3/osip.{1,3}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_mandir}/man3/*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
