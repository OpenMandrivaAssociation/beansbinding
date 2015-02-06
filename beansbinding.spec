%define section		free

Name:		beansbinding
Version:	1.2.1
Release:	8
Epoch:		0
Summary:        Beans Binding API
License:        LGPL
Url:            https://beansbinding.dev.java.net/
Group:		Development/Java
#
Source0:        https://beansbinding.dev.java.net/files/documents/6779/73673/beansbinding-1.2.1-src.zip
BuildRequires:	java-rpmbuild >= 1.6
BuildRequires:	java-devel >= 1.6
BuildRequires:	java >= 1.6
BuildRequires:  ant
BuildRequires:  ant-nodeps
BuildRequires:  ant-junit
Requires:	java >= 1.6
BuildArch:      noarch

%description
In essence, Beans Binding (JSR 295) is about keeping two properties
(typically of two objects) in sync. An additional emphasis is placed on the 
ability to bind to Swing components, and easy integration with IDEs such as 
NetBeans. This project provides the reference implementation.

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Java
Requires(post):   /bin/rm,/bin/ln
Requires(postun): /bin/rm

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c -n %{name}-%{version}
# remove all binary libs
find . -name "*.jar" -exec %{__rm} -f {} \;

%build
[ -z "$JAVA_HOME" ] && export JAVA_HOME=%{_jvmdir}/java 
ant dist

%install
# jar
%{__install} -d -m 755 %{buildroot}%{_javadir}
%{__install} -m 644 dist/%{name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%{__ln_s} %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
# javadoc
%{__install} -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr dist/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
(cd %{buildroot}%{_javadocdir} && ln -sf %{name}-%{version} %{name})

%post javadoc
%{__rm} -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ $1 -eq 0 ]; then
  %{__rm} -f %{_javadocdir}/%{name}
fi

%files
%defattr(-,root,root)
%{_javadir}/*


%files javadoc
%defattr(-,root,root)
%dir %{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}-%{version}/*
%ghost %{_javadocdir}/%{name}


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0:1.2.1-6mdv2011.0
+ Revision: 616745
- the mass rebuild of 2010.0 packages

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 0:1.2.1-5mdv2010.0
+ Revision: 424026
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0:1.2.1-4mdv2009.0
+ Revision: 243208
- rebuild

* Sun Dec 16 2007 Anssi Hannula <anssi@mandriva.org> 0:1.2.1-2mdv2008.1
+ Revision: 120835
- buildrequire java-rpmbuild, i.e. build with icedtea on x86(_64)

* Thu Dec 13 2007 Jaroslav Tulach <jtulach@mandriva.org> 0:1.2.1-1mdv2008.1
+ Revision: 119152
- First package of beansbinding library
- create beansbinding

