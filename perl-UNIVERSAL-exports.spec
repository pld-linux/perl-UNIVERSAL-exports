#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	UNIVERSAL
%define	pnam	exports
Summary:	UNIVERSAL::exports - lightweight, universal exporting of variables
Summary(pl):	UNIVERSAL::exports - lekkie, uniwersalne eksportowanie zmiennych
Name:		perl-UNIVERSAL-exports
Version:	0.03
Release:	1
License:	?
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7672d8e740d99c3af612205e6fde8644
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{!?_without_tests:1}0
BuildRequires:	perl-Exporter-Lite >= 0.01
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an alternative to Exporter intended to provide a universal,
lightweight subset of its functionality. It uses Exporter::Lite, so
look there for details.

%description -l pl
Ten modu³ jest alternatyw± dla Exportera maj±c± udostêpniæ
uniwersalny, lekki podzbiór jego funkcjonalno¶ci. U¿ywa modu³u
Exporter::Lite, z którego mo¿na poznaæ wiêcej szczegó³ów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
