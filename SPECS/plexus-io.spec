%bcond_with bootstrap

Name:           plexus-io
Version:        3.2.0
Release:        9%{?dist}
Summary:        Plexus IO Components
License:        ASL 2.0
URL:            https://github.com/codehaus-plexus/plexus-io
BuildArch:      noarch

Source0:        https://github.com/codehaus-plexus/plexus-io/archive/plexus-io-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  maven-local-openjdk8
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
%endif

%description
Plexus IO is a set of plexus components, which are designed for use
in I/O operations.

%package        javadoc
Summary:        Javadoc for %{name}

%description    javadoc
API documentation for %{name}.

%prep
%setup -q -n plexus-io-plexus-io-%{version}
cp %{SOURCE1} .

%pom_remove_plugin :animal-sniffer-maven-plugin

# Test fails in mock
sed -i /class/i@org.junit.Ignore src/test/java/org/codehaus/plexus/components/io/attributes/SymlinkUtilsTest.java

%build
%mvn_file  : plexus/io
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license NOTICE.txt LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%license NOTICE.txt LICENSE-2.0.txt

%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 3.2.0-9
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Wed Jun 09 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2.0-8
- Rebuild to workaround DistroBaker issue

* Tue Jun 08 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2.0-7
- Bootstrap Maven for CentOS Stream 9

* Mon May 17 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2.0-6
- Bootstrap build
- Non-bootstrap build

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 3.2.0-3
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2.0-2
- Mass rebuild for javapackages-tools 201902

* Wed Oct 23 2019 Marian Koncek <mkoncek@redhat.com> - 3.2.0-1
- Update to upstream version 3.2.0

* Wed Oct 16 2019 Fabio Valentini <decathorpe@gmail.com> - 3.2.0-1
- Update to version 3.2.0.

* Mon Jul 29 2019 Fabio Valentini <decathorpe@gmail.com> - 3.1.1-1
- Update to version 3.1.1.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1.1-2
- Mass rebuild for javapackages-tools 201901

* Mon May 13 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1.1-1
- Update to upstream version 3.1.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 11 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.0-1
- Update to upstream version 3.0.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Apr 20 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.7.1-1
- Update to upstream version 2.7.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun  9 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.6-1
- Update to upstream version 2.6

* Wed Apr  1 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5-2
- Update upstream URL

* Tue Mar 24 2015 Michael Simacek <msimacek@redhat.com> - 2.5-1
- Update to upstream version 2.5

* Mon Nov  3 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.3-1
- Update to upstream version 2.3.3

* Fri Oct 24 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.2-1
- Update to upstream version 2.3.2

* Fri Oct 24 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3-1
- Update to upstream version 2.3

* Fri Oct 24 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-1
- Update to upstream version 2.2

* Fri Oct 24 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1.4-1
- Update to upstream version 2.1.4

* Fri Oct  3 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1.3-1
- Update to upstream version 2.1.3

* Wed Oct  1 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1.2-1
- Update to upstream version 2.1.2
- Remove patch for PLXCOMP-244 (accepted upstream)

* Mon Sep 29 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1.1-2
- Don't try to set attributes of symbolic links

* Mon Sep 29 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1.1-1
- Update to upstream version 2.1.1
- Remove patch for PLXCOMP-241: accepted upstream

* Tue Sep 23 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.0.12-1
- Update to upstream version 2.0.12

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.0.10-2
- Use Requires: java-headless rebuild (#1067528)

* Tue Jan 21 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.0.10-1
- Update to upstream version 2.0.10

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.0.5-7
- Add ASL 2.0 license text to rpms

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.0.5-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jan 17 2013 Michal Srb <msrb@redhat.com> - 2.0.5-4
- Build with xmvn

* Thu Nov 22 2012 Jaromir Capik <jcapik@redhat.com> - 2.0.5-3
- Migration to plexus-containers-container-default

* Tue Nov 13 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.0.5-2
- Use ordinary URL for Source0
- Make sure we use 1.5 source/target
- Add enforcer plugin to BR

* Wed Oct 10 2012 Alexander Kurtakov <akurtako@redhat.com> 2.0.5-1
- Update to upstream 2.0.5 release.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 18 2012 Alexander Kurtakov <akurtako@redhat.com> 2.0.4-1
- Update to latest upstream.

* Thu Feb 02 2012 Tomas Radej <tradej@redhat.com> - 2.0.2-1
- Updated to upstream version

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep 8 2011 Alexander Kurtakov <akurtako@redhat.com> 2.0.1-1
- Update to 2.0.1 upstream release.

* Wed Jul 27 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0.1-2
- Use add_maven_depmap macro

* Wed Jul 27 2011 Jaromir Capik <jcapik@redhat.com> - 1.0.1-2
- Removal of plexus-maven-plugin dependency (not needed)
- Minor spec file changes according to the latest guidelines

* Tue May 17 2011 Alexander Kurtakov <akurtako@redhat.com> 1.0.1-1
- Update to upstream 1.0.1.
- Adapt to current guidelines.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.3.a5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 23 2009 Alexander Kurtakov <akurtako@redhat.com> 1.0-0.2.a5
- Fix review comments.

* Wed Dec 23 2009 Alexander Kurtakov <akurtako@redhat.com> 1.0-0.1.a5.1
- Initial package
