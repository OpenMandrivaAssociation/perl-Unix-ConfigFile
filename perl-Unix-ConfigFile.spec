%define upstream_name    Unix-ConfigFile
%define upstream_version 0.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Unix::ConfigFile module for Perl
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Unix/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Easy access to data in many formats

%prep
%setup -q -n  %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="$RPM_OPT_FLAGS" PREFIX=%{_prefix}

%check
%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT  

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%dir %{perl_vendorlib}/Unix
%{perl_vendorlib}/Unix/*.pm
