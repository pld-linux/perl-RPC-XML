%include	/usr/lib/rpm/macros.perl
%define		pdir	RPC
%define		pnam	XML
Summary:	Implementation of XML-RPC for Perl
Summary(pl):	Implementacja standardu XML-RPC dla Perla
Name:		perl-%{pdir}-%{pnam}
Version:	0.51
Release:	1
Vendor:		Randy J. Ray
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
URL:		http://www.blackperl.com/RPC::XML/
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-libwww
BuildRequires:	rpm-perlprov >= 4.0.2-56
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
perl Makefile.PL
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
%{perl_sitelib}/RPC/XML.pm
%{perl_sitelib}/RPC/XML
%dir %{perl_sitelib}/auto/RPC
%dir %{perl_sitelib}/auto/RPC/XML
%dir %{perl_sitelib}/auto/RPC/XML/*
%{perl_sitelib}/auto/RPC/XML/*/*.al
%{perl_sitelib}/auto/RPC/XML/*/autosplit.ix
%{perl_sitelib}/Apache/RPC
%{_mandir}/man3/*
%{_mandir}/man1/*
