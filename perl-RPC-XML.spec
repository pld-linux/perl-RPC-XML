#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	RPC
%define		pnam	XML
Summary:	RPC::XML - an implementation of XML-RPC for Perl
Summary(pl.UTF-8):	RPC::XML - implementacja standardu XML-RPC dla Perla
Name:		perl-RPC-XML
Version:	0.76
Release:	3
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	731aaf588e6bd45b3a9cece8d4223e48
Patch0:		mod_perl2.patch
URL:		http://www.blackperl.com/RPC::XML/
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-libwww
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

# these are provided by mod_perl's Apache2::compat
%define		_noautoreq	perl(Apache) perl(Apache::Constants) perl(Apache::File)

%description
The RPC::XML package for Perl is an implementation of the XML-RPC
standard as defined at <http://www.xmlrpc.com/spec/>. It is written in
pure Perl without use or need of C (or XS) linkage. It does (at
present) require the XML::Parser and LWP CPAN modules for operation.
Version 0.60 will switch to XML::LibXML in place of XML::Parser.

%description -l pl.UTF-8
Pakiet RPC::XML jest implementacją standardu XML-RPC zdefiniowanego na
<http://www.xmlrpc.com/spec/>. Jest napisany wyłącznie w Perlu, bez
łączenia z C (ani XS). Aktualnie wymaga do działania modułów
XML::Parser i LWP z CPAN. Wersja 0.60 bedzie u?ywa? XML::LibXML zamiast
XML::Parser.

%package Apache
Summary:	RPC server as an Apache/mod_perl content handler
Summary(pl.UTF-8):	Serwer RPC jako procedura obsługi treści Apache/mod_perl
Group:		Applications/Networking

%description Apache
RPC server as an Apache/mod_perl content handler.

%description Apache -l pl.UTF-8
Serwer RPC jako procedura obsługi treści Apache/mod_perl.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -P0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc ChangeLog README
%dir %{perl_vendorlib}/RPC
%{perl_vendorlib}/RPC/XML
%{perl_vendorlib}/RPC/XML.pm
%{_mandir}/man3/*
%exclude %{_mandir}/man3/Apache*
%{_mandir}/man1/*

%files Apache
%defattr(644,root,root,755)
%doc README.apache2
%{perl_vendorlib}/Apache/RPC
%{_mandir}/man3/Apache*
