%include	/usr/lib/rpm/macros.perl
%define		pdir	RPC
%define		pnam	XML
Summary:	Implementation of XML-RPC for Perl
Summary(pl):	Implementacja standardu XML-RPC dla Perla
Name:		perl-%{pdir}-%{pnam}
Version:	0.53
Release:	1
Vendor:		Randy J. Ray
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	aca56b9abe71f52acf7e046f407f0b42
URL:		http://www.blackperl.com/RPC::XML/
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-libwww
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
The RPC::XML package for Perl is an implementation of the XML-RPC
standard as defined at <http://www.xmlrpc.com/spec/>. It is written in
pure Perl without use or need of C (or XS) linkage. It does (at
present) require the XML::Parser and LWP CPAN modules for operation.

%description -l pl
Pakiet RPC::XML jest implementacj± standardu XML-RPC zdefiniowanego na
<http://www.xmlrpc.com/spec/>. Jest napisany wy³±cznie w Perlu, bez
³±czenia z C (ani XS). Aktualnie wymaga do dzia³ania modu³ów
XML::Parser i LWP z CPAN.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc ChangeLog README README.apache
%{perl_vendorlib}/RPC/XML.pm
%{perl_vendorlib}/RPC/XML
%dir %{perl_vendorlib}/auto/RPC
%dir %{perl_vendorlib}/auto/RPC/XML
%dir %{perl_vendorlib}/auto/RPC/XML/*
%{perl_vendorlib}/auto/RPC/XML/*/*.al
%{perl_vendorlib}/auto/RPC/XML/*/autosplit.ix
%{perl_vendorlib}/Apache/RPC
%{_mandir}/man3/*
%{_mandir}/man1/*
