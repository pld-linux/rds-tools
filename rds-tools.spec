Summary:	RDS support tools
Summary(pl.UTF-8):	Narzędzia obsługujące RDS
Name:		rds-tools
Version:	2.0.4
Release:	1
License:	BSD or GPL v2
Group:		Networking/Utilities
# or: http://oss.oracle.com/projects/rds/files/sources/ (but sources dir is not browsable)
Source0:	http://www.openfabrics.org/downloads/rds-tools/%{name}-%{version}.tar.gz
# Source0-md5:	a016668f910b9f7f9c60f098a8d8c592
URL:		http://oss.oracle.com/projects/rds/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rds-tools is a collection of support tools for the RDS socket API.

It includes rds-stress, rds-info, and rds-ping.

%description -l pl.UTF-8
rds-tools to zbiór narzędzi obsługujących API gniazd RDS.

Obejmuje rds-stress, rds-info i rds-ping.

%package devel
Summary:	Header files for RDS socket API
Summary(pl.UTF-8):	Pliki nagłówkowe API gniazd RDS
Group:		Development/Libraries
# doesn't require base

%description devel
Header files for RDS socket API.

%description devel -l pl.UTF-8
Pliki nagłówkowe API gniazd RDS.

%prep
%setup -q

%build
%configure
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -Iinclude"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rds-info
%attr(755,root,root) %{_bindir}/rds-ping
%attr(755,root,root) %{_bindir}/rds-stress
%{_mandir}/man1/rds-info.1*
%{_mandir}/man1/rds-ping.1*
%{_mandir}/man1/rds-stress.1*

%files devel
%defattr(644,root,root,755)
%doc docs/rds-architecture.txt
%{_includedir}/net/rds.h
%{_mandir}/man7/rds.7*
%{_mandir}/man7/rds-rdma.7*
