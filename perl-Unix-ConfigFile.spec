%define upstream_name    Unix-ConfigFile
%define upstream_version 0.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Unix::ConfigFile module for Perl
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Unix/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Easy access to data in many formats

%prep
%setup -q -n  %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}" PREFIX=%{_prefix}

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/Unix


%changelog
* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.60.0-1mdv2010.0
+ Revision: 408096
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.06-8mdv2009.0
+ Revision: 242117
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- simplify buildrequires
- buildrequires obsoletes buildprereq

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 0.06-6mdv2008.0
+ Revision: 23626
- rebuild


* Tue Sep 27 2005 Olivier Thauvin <nanardon@mandriva.org> 0.06-5mdk
- rebuild

* Mon Aug 30 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.06-4mdk
- Rebuild, cleanup of spec

* Tue Jul 22 2003 François Pons <fpons@mandrakesoft.com> 0.06-3mdk
- applied patch from Michael Scherer.

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.06-2mdk
- rebuild for new auto{prov,req}

* Thu Jul 25 2002 Philippe Libat <philippe@mandrakesoft.com> 0.06-1mdk
- initial specfile

