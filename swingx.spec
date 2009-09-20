Name:		swingx
Version:	0.9.4
Release:	%mkrel 2
Summary:	SwingLabs Swing Component Extensions
Group:		Development/Java
License:	LGPLv2+
URL:		https://swingx.dev.java.net/
Source:		%{name}-%{version}-src.zip
Patch0:		swingx-properties.patch
BuildRequires:	java-devel java-rpmbuild ant ant-nodeps
BuildRequires:	jmock emma junit swingworker swing-layout batik jhlabs-filters
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
%description
Swingx contains extensions to the Swing GUI toolkit, including new and
enhanced components that provide functionality commonly required by
rich client applications. Highlights include:

  * Sorting, filtering, highlighting for tables, trees, and lists
  * Find/search
  * Auto-completion
  * Login/authentication framework
  * TreeTable component
  * Collapsible panel component
  * Date picker component
  * Tip-of-the-Day component

Many of these features will eventually be incorporated into the Swing
toolkit, although API compatibility will not be guaranteed. The SwingX
project focuses exclusively on the raw components themselves.

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p1

%{_bindir}/find . -name '*.class' -or -name '*.jar' -exec %{__rm} -f {} \;

%build
%ant jar

%install
%{__rm} -Rf %{buildroot}
%{__install} -d %{buildroot}%{_javadir}
%{__install} -m 0644 dist/%{name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%create_jar_links

%files
%doc README COPYING
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
