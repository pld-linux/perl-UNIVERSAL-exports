#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	UNIVERSAL
%define		pnam	exports
Summary:	UNIVERSAL::exports - lightweight, universal exporting of variables
Summary(pl):	UNIVERSAL::exports - lekkie, uniwersalne eksportowanie zmiennych
Name:		perl-UNIVERSAL-exports
Version:	0.05
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4378f0e385c47829584486468414fde9
URL:		http://search.cpan.org/dist/UNIVERSAL-exports/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Exporter-Lite >= 0.01
%endif
Requires:	perl-UNIVERSAL-require
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

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# use from perl-UNIVERSAL-require
rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/%{pdir}/require.pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/%{pdir}/exports.pm
%{_mandir}/man3/*
