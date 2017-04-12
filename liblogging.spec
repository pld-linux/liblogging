Summary:	An easy to use logging library
Name:		liblogging
Version:	1.0.4
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://download.rsyslog.com/liblogging/%{name}-%{version}.tar.gz
# Source0-md5:	034083ef1424a566fdeefc56a719691f
URL:		http://www.liblogging.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
liblogging (the upstream project) is a collection of several
components. Namely: stdlog, journalemu, rfc3195.

%package stdlog
Summary:	An easy to use logging library - stdlog component
Group:		Libraries

%description stdlog
liblogging (the upstream project) is a collection of several
components. Namely: stdlog, journalemu, rfc3195. The stdlog component
of liblogging can be viewed as an enhanced version of the syslog(3)
API. It retains the easy semantics, but makes the API more
sophisticated "behind the scenes" with better support for multiple
threads and flexibility for different log destinations (e.g. syslog
and systemd journal).

%package stdlog-devel
Summary:	An easy to use logging library - stdlog development files
Group:		Development/Libraries
Requires:	%{name}-stdlog = %{version}-%{release}

%description stdlog-devel
This package contains development files for the %{name}-stdlog
package.

%prep
%setup -q

%build
%configure \
	--disable-static \
	--disable-rfc3195 \
	--disable-journal

%{__make} V=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_bindir}/stdlogctl \
	$RPM_BUILD_ROOT%{_mandir}/man1/stdlogctl.1*

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post stdlog -p /sbin/ldconfig
%postun stdlog -p /sbin/ldconfig

%files stdlog
%defattr(644,root,root,755)
%{_libdir}/liblogging-stdlog.so.*

%files stdlog-devel
%defattr(644,root,root,755)
%doc ChangeLog
%{_includedir}/liblogging
%{_libdir}/liblogging-stdlog.so
%{_pkgconfigdir}/liblogging-stdlog.pc
%{_mandir}/man3/stdlog.3*
