Summary:	A tool to show diffs between rpms
Summary(pl.UTF-8):	Narzędzie do pokazywania różnic między pakietami rpm
Name:		urpmdiff
Version:	2.0.1
Release:	1
License:	GPL
Group:		Development
Source0:	https://abf.rosalinux.ru/software/urpmdiff/archive/%{name}-v%{version}.tar.gz
# Source0-md5:	e3990501d53c5a60c378c443c8793346
URL:		https://abf.rosalinux.ru/software/urpmdiff
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
%setup -q -n %{name}-v%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{perl_vendorarch}/auto/urpmdiff/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/urpmdiff
%{_mandir}/man1/urpmdiff.1*
