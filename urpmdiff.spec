%include	/usr/lib/rpm/macros.perl
Summary:	A tool to show diffs between rpms
Summary(pl.UTF-8):	Narzędzie do pokazywania różnic między pakietami rpm
Name:		urpmdiff
Version:	1.1
Release:	2
License:	GPL
Group:		Development
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	eca3b2f8fbc1f46a225fc769f669c30b
Patch0:		%{name}-no-MDK.patch
URL:		http://cvs.mandrakesoft.com/cgi-bin/cvsweb.cgi/soft/urpmdiff
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
urpmdiff shows the differences between two rpms. It's intended to help
packagers to know what has changed between an old and a new version of
an rpm. Its output is reminiscent of the unified diff format.

%description -l pl.UTF-8
urpmdiff pokazuje różnice między dwoma pakietami rpm. Jego zadaniem
jest pomoc osobom pakietującym, aby wiedziały, co zmieniło się między
starą a nową wersją pakietu. Wyjście przypomina format unified diff.

%prep
%setup -q
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
