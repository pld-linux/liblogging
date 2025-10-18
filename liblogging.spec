#
# Conditional build:
%bcond_without	static_libs	# static libraries
%bcond_with	systemd		# systemd journal driver in stdlog library

Summary:	An easy to use logging library
Summary(pl.UTF-8):	Łatwa w użyciu biblioteka do logowania
Name:		liblogging
Version:	1.0.6
Release:	2
License:	BSD
Group:		Libraries
Source0:	https://download.rsyslog.com/liblogging/%{name}-%{version}.tar.gz
# Source0-md5:	f215c7e7ac6cfd1f5dabdba08c522b29
URL:		http://www.liblogging.org/
BuildRequires:	pkgconfig
%{?with_systemd:BuildRequires:	systemd-devel >= 1:209}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
liblogging is a collection of several components. Namely: stdlog,
rfc3195.

%description -l pl.UTF-8
liblogging to zbiór kilku komponentów: stdlog, rfc3195.

%package rfc3195
Summary:	An easy to use logging library - RFC 3195 logging component
Summary(pl.UTF-8):	Łatwa w użyciu biblioteka do logowania - komponent logowania RFC 3195
Group:		Libraries

%description rfc3195
liblogging is a collection of several components. Namely: stdlog,
rfc3195.

RFC 3195 offers reliable connections between syslog clients and
collectors (servers, daemons).

%description rfc3195 -l pl.UTF-8
liblogging to zbiór kilku komponentów: stdlog, rfc3195.

RFC 3195 oferuje wiarygodne połączenia między klientami sysloga a
serwerami/demonami zbierającymi logi.

%package rfc3195-devel
Summary:	An easy to use logging library - rfc3195 development files
Summary(pl.UTF-8):	Łatwa w użyciu biblioteka do logowania - pliki programistyczne rfc3195
Group:		Development/Libraries
Requires:	%{name}-rfc3195 = %{version}-%{release}

%description rfc3195-devel
This package contains development files for the liblogging-rfc3195
library.

%description rfc3195-devel -l pl.UTF-8
Ten pakiet zawiera pliki programistyczne biblioteki
liblogging-rfc3195.

%package rfc3195-static
Summary:	An easy to use logging library - rfc3195 static library
Summary(pl.UTF-8):	Łatwa w użyciu biblioteka do logowania - biblioteka statyczna rfc3195
Group:		Development/Libraries
Requires:	%{name}-rfc3195-devel = %{version}-%{release}

%description rfc3195-static
This package contains static liblogging-rfc3195 library.

%description rfc3195-static -l pl.UTF-8
Ten pakiet zawiera bibliotekę statyczną liblogging-rfc3195.

%package rfc3195-apidocs
Summary:	API documentation for logging-rfc3195 library
Summary(pl.UTF-8):	Dokumentacja API biblioteki logging-rfc3195
Group:		Documention
BuildArch:	noarch

%description rfc3195-apidocs
API documentation for logging-rfc3195 library.

%description rfc3195-apidocs -l pl.UTF-8
Dokumentacja API biblioteki logging-rfc3195.

%package stdlog
Summary:	An easy to use logging library - stdlog component
Summary(pl.UTF-8):	Łatwa w użyciu biblioteka do logowania - komponent stdlog
Group:		Libraries

%description stdlog
liblogging is a collection of several components. Namely: stdlog,
rfc3195.

The stdlog component of liblogging can be viewed as an enhanced
version of the syslog(3) API. It retains the easy semantics, but makes
the API more sophisticated "behind the scenes" with better support for
multiple threads and flexibility for different log destinations (e.g.
syslog and systemd journal).

%description stdlog -l pl.UTF-8
liblogging to zbiór kilku komponentów: stdlog, rfc3195.

Komponent stdlog można postrzegać jako rozszerzoną wersję API
syslog(3). Zachowuje łatwą semantykę, ale czyni API bardziej
wyszukanym od strony wewnętrznej, z lepszą obsługą wielu wątków oraz
elastycznym wyborem różnych celów (np. syslog i journal z systemd).

%package stdlog-devel
Summary:	An easy to use logging library - stdlog development files
Summary(pl.UTF-8):	Łatwa w użyciu biblioteka do logowania - pliki programistyczne stdlog
Group:		Development/Libraries
Requires:	%{name}-stdlog = %{version}-%{release}

%description stdlog-devel
This package contains development files for the liblogging-stdlog
library.

%description stdlog-devel -l pl.UTF-8
Ten pakiet zawiera pliki programistyczne biblioteki liblogging-stdlog.

%package stdlog-static
Summary:	An easy to use logging library - stdlog static library
Summary(pl.UTF-8):	Łatwa w użyciu biblioteka do logowania - biblioteka statyczna stdlog
Group:		Development/Libraries
Requires:	%{name}-stdlog-devel = %{version}-%{release}

%description stdlog-static
This package contains static liblogging-stdlog library.

%description stdlog-static -l pl.UTF-8
Ten pakiet zawiera bibliotekę statyczną liblogging-stdlog.

%prep
%setup -q

%build
%configure \
	--enable-journal%{!?with_systemd:=no} \
	--enable-rfc3195 \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static}

%{__make}
# V=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	rfc3195 -p /sbin/ldconfig
%postun	rfc3195 -p /sbin/ldconfig

%post	stdlog -p /sbin/ldconfig
%postun	stdlog -p /sbin/ldconfig

%files rfc3195
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/liblogging-rfc3195.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblogging-rfc3195.so.0

%files rfc3195-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblogging-rfc3195.so
%dir %{_includedir}/liblogging
%{_includedir}/liblogging/liblogging.h
%{_includedir}/liblogging/settings.h
%{_includedir}/liblogging/srAPI.h
%{_includedir}/liblogging/syslogmessage.h
%{_pkgconfigdir}/liblogging-rfc3195.pc

%if %{with static_libs}
%files rfc3195-static
%defattr(644,root,root,755)
%{_libdir}/liblogging-rfc3195.a
%endif

%files rfc3195-apidocs
%defattr(644,root,root,755)
%doc rfc3195/doc/html/*.{css,html,png}

%files stdlog
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/stdlogctl
%attr(755,root,root) %{_libdir}/liblogging-stdlog.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblogging-stdlog.so.0
%{_mandir}/man1/stdlogctl.1*

%files stdlog-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblogging-stdlog.so
%dir %{_includedir}/liblogging
%{_includedir}/liblogging/stdlog.h
%{_pkgconfigdir}/liblogging-stdlog.pc
%{_mandir}/man3/stdlog.3*

%if %{with static_libs}
%files stdlog-static
%defattr(644,root,root,755)
%{_libdir}/liblogging-stdlog.a
%endif
