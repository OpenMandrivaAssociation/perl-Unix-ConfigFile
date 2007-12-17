%define realname Unix-ConfigFile
%define name perl-%{realname}
%define version 0.06
%define release %mkrel 6

Name:		%{name}
Summary:	Unix::ConfigFile module for Perl
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source:		%{realname}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel

%description
Easy access to data in many formats

%prep
%setup -q -n  %{realname}-%{version}

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

