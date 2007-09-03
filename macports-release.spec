Summary:	MacPorts release files
Name:		macports-release
Version:	1.5
Release:	0
License:	BSD
Group:		sysutils
URL:		http://macports.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildArch:	noarch
Prefix:		/opt/local

%description
MacPorts release files such as repo configs

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
#config(noreplace) %{prefix}/etc/yum/repos.d/*.repo
#config(noreplace) %{prefix}/etc/apt/sources.list.d/*.list
