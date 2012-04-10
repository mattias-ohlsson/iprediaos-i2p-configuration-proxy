Name:		iprediaos-i2p-configuration-proxy
Version:	0.1
Release:	1%{?dist}
Summary:	Proxy configuration for IprediaOS

Group:		System Environment/Base
License:	GPL
URL:		http://www.ipredia.org
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch

Requires:	i2p
Requires(post):	GConf2

%description
Configuration for i2p proxy.


%prep
%setup -q


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%post
# Set proxy
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.mandatory --type=string --set /system/proxy/mode "manual"
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.mandatory --type=bool --set /system/http_proxy/use_http_proxy "TRUE"
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.mandatory --type=string --set /system/http_proxy/host "localhost"
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.mandatory --type=int --set /system/http_proxy/port "4444"
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.mandatory --type=string --set /system/proxy/secure_host "localhost"
gconftool-2 --direct --config-source xml:readwrite:/etc/gconf/gconf.xml.mandatory --type=int --set /system/proxy/secure_port "4445"

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
%{_sysconfdir}/profile.d/*


%changelog
* Tue Apr 10 2012 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 0.1-1
- Initial package
