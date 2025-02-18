%define upstream_name    Dist-Zilla-Plugin-PurePerlTests
%define upstream_version 0.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Run all your tests twice, once with XS code and once with pure Perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Most)
BuildArch:	noarch

%description
This plugin is for modules which ship with a dual XS/pure Perl
implementation.

The plugin makes a copy of all your tests when doing release testing (via
'dzil test' or 'dzil release'). The copy will set an environment value that
you specify in a 'BEGIN' block. You can use this to force your code to not
load the XS implementation.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*


