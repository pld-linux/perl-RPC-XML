%include	/usr/lib/rpm/macros.perl

%define	pdir	RPC
%define	pnam	XML

Summary:	Implementation of XML-RPC for Perl
Summary(pl):	Implementacja standardu XML-RPC dla Perla
Name:		perl-%{pdir}-%{pnam}
Version:	0.37
Release:	1
Vendor:	Randy J. Ray
Url:	http://www.blackperl.com/RPC::XML
License:	Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-56
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-libwww
BuildRequires:	perl-XML-Parser
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
The RPC::XML package for Perl is an implementation of the XML-RPC standard
as defined at <http://www.xmlrpc.com/spec>. It is written in pure Perl without
use or need of C (or XS) linkage. It does (at present) require the XML::Parser
and LWP CPAN modules for operation.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README README.apache

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc *.gz
%{perl_sitelib}/RPC/XML.pm
%{perl_sitelib}/RPC/XML
%{perl_sitelib}/auto/RPC/XML
%{perl_sitelib}/Apache/RPC
%{_mandir}/man3/*
%{_mandir}/man1/*
