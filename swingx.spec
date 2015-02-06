Name:           swingx
Version:        0.9.5
Release:        5
Summary:        A collection of Swing components
License:        LGPLv2
Group:          Development/Java
Url:            https://swingx.dev.java.net/
Source0:        https://swingx.dev.java.net/files/documents/2981/121928/%{name}-%{version}-src.zip
# Remove external dependency that's now included in JDK 1.6
# See http://forums.java.net/jive/thread.jspa?messageID=318384
Patch0:         swingx-0.9.4-LoginService.patch
# Remove build dependencies on included binary jars and add system jars
# Remove main class from manifest
Patch1:         swingx-0.9.4-project-properties.patch
# Don't do the "demo taglet" stuff
Patch2:         swingx-0.9.5-swinglabs-build-impl.patch

BuildArch:      noarch

BuildRequires:      ant
BuildRequires:      ant-nodeps
BuildRequires:      java-devel >= 0:1.6.0
BuildRequires:      jpackage-utils >= 0:1.5
BuildRequires:      batik

Requires:           java >= 0:1.6.0

Requires(post):     jpackage-utils
Requires(postun):   jpackage-utils

%description
SwingX contains a collection of powerful, useful, and just plain fun Swing
components. Each of the Swing components have been extended, providing
data-aware functionality out of the box. New useful components have been
created like the JXDatePicker, JXTaskPane, and JXImagePanel.


%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p1
%patch1 -p1
%patch2 -p1
rm -rf lib/


%build
ant jar javadoc


%install
# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p dist/%{name}.jar  $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadocs
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/
cp -r dist/javadoc $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_to_maven_depmap org.jdesktop.swingx %{name} %{version} JPP %{name}


%post
%update_maven_depmap


%postun
%update_maven_depmap


%files
%defattr(-,root,root,-)
%doc COPYING README
%{_javadir}/*.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}


%files javadoc
%defattr(-,root,root,-)
%doc COPYING
%{_javadocdir}/%{name}




%changelog
* Sun Nov 27 2011 Guilherme Moro <guilherme@mandriva.com> 0.9.5-4
+ Revision: 734245
- rebuild
- imported package swingx

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Jan 23 2009 Jérôme Soyer <saispo@mandriva.org> 0.9.4-1mdv2009.1
+ Revision: 332895
- New upstream release

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 0.9.1-4mdv2009.0
+ Revision: 261306
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0.9.1-3mdv2009.0
+ Revision: 253861
- rebuild

  + Nicolas Vigier <nvigier@mandriva.com>
    - use create_jar_links macro

* Wed Mar 05 2008 Nicolas Vigier <nvigier@mandriva.com> 0.9.1-1mdv2008.1
+ Revision: 179987
- import swingx


