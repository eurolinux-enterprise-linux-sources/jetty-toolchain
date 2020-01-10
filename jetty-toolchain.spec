Name:           jetty-toolchain
Version:        1.4
Release:        9%{?dist}
Summary:        Jetty Toolchain main POM file

License:        ASL 2.0 or EPL
URL:            http://www.eclipse.org/jetty/
Source0:        http://git.eclipse.org/c/jetty/org.eclipse.jetty.toolchain.git/snapshot/%{name}-%{version}.tar.bz2
# rpmlint config file (fedpkg lint will use this)
Source1:        .rpmlint
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  jetty-parent
BuildRequires:  maven-release-plugin

%description
Jetty Toolchain main POM file

%prep
%setup -q
cp -p jetty-distribution-remote-resources/src/main/resources/* .

%build
pushd %{name}
%mvn_build

%install
pushd %{name}
%mvn_install

%files -f %{name}/.mfiles
%doc LICENSE-APACHE-2.0.txt LICENSE-ECLIPSE-1.0.html notice.html


%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.4-9
- Mass rebuild 2013-12-27

* Tue Jul 30 2013 Michal Srb <msrb@redhat.com> - 1.4-8
- Build with XMvn
- Drop group tag
- Fix R/BR

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.4-6
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Sep 20 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-5
- Install license files

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov  3 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4-2
- Added build section (available for overriding)

* Wed Nov  2 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4-1
- Initial version

