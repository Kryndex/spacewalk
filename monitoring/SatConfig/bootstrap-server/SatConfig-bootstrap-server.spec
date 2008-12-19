Name:         SatConfig-bootstrap-server
Version:      1.13.1
Release:      1%{?dist}
Source0:      https://fedorahosted.org/releases/s/p/spacewalk/%{name}-%{version}.tar.gz
Summary:      Provides scout info for boostrap
URL:          https://fedorahosted.org/spacewalk
BuildArch:    noarch
Requires:     perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Group:        Development/Libraries
License:      GPLv2
Buildroot:    %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
NOCpulse provides application, network, systems and transaction monitoring,
coupled with a comprehensive reporting system including availability,
historical and trending reports in an easy-to-use browser interface.

This package dole out ID's and descriptions to bootstrapping scouts.

%prep
%setup -q

%build
#Nothing to build

%install
rm -rf $RPM_BUILD_ROOT

# CGI bin
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/np.d/apachereg
mkdir -p $RPM_BUILD_ROOT%{perl_vendorlib}/NOCpulse/SatConfig
install -m 644 Bootstrap.pm $RPM_BUILD_ROOT%{perl_vendorlib}/NOCpulse/SatConfig
install -m 644 TranslateKey.pm $RPM_BUILD_ROOT%{perl_vendorlib}/NOCpulse/SatConfig
install -m 644 Apache.SatConfig-bootstrap-server $RPM_BUILD_ROOT%{_sysconfdir}/rc.d/np.d/apachereg

%{_fixperms} $RPM_BUILD_ROOT/*

%files
%defattr(-,root,root,-)
%{perl_vendorlib}/NOCpulse/*
%config(noreplace) %{_sysconfdir}/rc.d/np.d/apachereg/Apache.SatConfig-bootstrap-server

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Sep 23 2008 Miroslav Suchý <msuchy@redhat.com> 1.13.1-1
- spec cleanup for Fedora

* Tue Jun 10 2008 Milan Zazrivec <mzazrivec@redhat.com> 1.13.0-10
- cvs.dist import
