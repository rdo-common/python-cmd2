%if 0%{?fedora}
%global with_python3 1
%endif

%global modname cmd2

Name:             python-cmd2
Version:          0.6.8
Release:          16%{?dist}
Summary:          Extra features for standard library's cmd module

Group:            Development/Libraries
License:          MIT
URL:              http://pypi.python.org/pypi/cmd2
Source0:          http://pypi.python.org/packages/source/c/%{modname}/%{modname}-%{version}.tar.gz

# https://bitbucket.org/catherinedevlin/cmd2/issues/18
Patch0:           python-cmd2-python35-compat.patch

BuildArch:        noarch


BuildRequires:    python2-devel
BuildRequires:    dos2unix

%if 0%{?with_python3}
BuildRequires:    python3-devel
BuildRequires:    python2-tools
BuildRequires:    dos2unix
%endif

%global _description\
Enhancements for standard library's cmd module.\
\
Drop-in replacement adds several features for command-prompt tools:\
\
 * Searchable command history (commands: "hi", "li", "run")\
 * Load commands from file, save to file, edit commands in file\
 * Multi-line commands\
 * Case-insensitive commands\
 * Special-character shortcut commands (beyond cmd's "@" and "!")\
 * Settable environment parameters\
 * Parsing commands with flags\
 * > (filename), >> (filename) redirect output to file\
 * < (filename) gets input from file\
 * bare >, >>, < redirect to/from paste buffer\
 * accepts abbreviated commands when unambiguous\
 * `py` enters interactive Python console\
 * test apps against sample session transcript (see example/example.py)\
\
Usable without modification anywhere cmd is used; simply import cmd2.Cmd\
in place of cmd.Cmd.\
\
See docs at http://packages.python.org/cmd2/

%description %_description

%package -n python2-cmd2
Summary: %summary
Requires:         python2-pyparsing >= 2.0.1
Requires:         /usr/bin/which
%{?python_provide:%python_provide python2-cmd2}

%description -n python2-cmd2 %_description

%if 0%{?with_python3}
%package -n python3-cmd2
Summary:        Extra features for standard library's cmd module
Group:          Development/Libraries

Requires:       python3-pyparsing

%description -n python3-cmd2
Enhancements for standard library's cmd module.

Drop-in replacement adds several features for command-prompt tools:

 * Searchable command history (commands: "hi", "li", "run")
 * Load commands from file, save to file, edit commands in file
 * Multi-line commands
 * Case-insensitive commands
 * Special-character shortcut commands (beyond cmd's "@" and "!")
 * Settable environment parameters 
 * Parsing commands with flags
 * > (filename), >> (filename) redirect output to file
 * < (filename) gets input from file
 * bare >, >>, < redirect to/from paste buffer
 * accepts abbreviated commands when unambiguous
 * `py` enters interactive Python console
 * test apps against sample session transcript (see example/example.py)

Usable without modification anywhere cmd is used; simply import cmd2.Cmd
in place of cmd.Cmd.

See docs at http://packages.python.org/cmd2/
%endif

%prep
%setup -q -n %{modname}-%{version}
%patch0 -p1

chmod -x README.txt
dos2unix README.txt

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif

%build
%{__python} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif

%install
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root=%{buildroot}
popd
%endif

%{__python} setup.py install -O1 --skip-build --root=%{buildroot}

%files -n python2-cmd2
%doc README.txt
%{python_sitelib}/cmd2.py*
%{python_sitelib}/%{modname}-%{version}*

%if 0%{?with_python3}
%files -n python3-%{modname}
%doc README.txt
%{python3_sitelib}/cmd2.py*
%{python3_sitelib}/__pycache__/cmd2*
%{python3_sitelib}/%{modname}-%{version}*
%endif

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.8-15
- Rebuilt for Python 3.7

* Sun Feb 11 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.6.8-14
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.6.8-12
- Python 2 binary package renamed to python2-cmd2
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.6.8-9
- Rebuild for Python 3.6

* Mon Oct 31 2016 Mike Burns <mburns@redhat.com> - 0.6.8-8
- add Requires: which (bz#1390360)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.8-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 19 2016 Ralph Bean <rbean@redhat.com> - 0.6.8-6
- Apply patch for compat on python-3.5.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.8-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 29 2015 Ralph Bean <rbean@redhat.com> - 0.6.8-2
- Fix python3 subpackage by removing double-run of 2to3 (it's not idempotent!).

* Wed Apr 29 2015 Ralph Bean <rbean@redhat.com> - 0.6.8-1
- new version

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.6.7-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed Dec 11 2013 Ralph Bean <rbean@redhat.com> - 0.6.7-3
- Versioned requirement on pyparsing.  (#1040339)

* Thu Nov 14 2013 Ralph Bean <rbean@redhat.com> - 0.6.7-2
- Bump release.

* Thu Nov 14 2013 Ralph Bean <rbean@redhat.com> - 0.6.7-1
- Latest upstream.
- Drop patch which has been upstreamed.
- Modernized python3 macro def.

* Tue Jul 30 2013 Pádraig Brady <pbrady@redhat.com> - 0.6.4-7
- Suppress warnings about missing editors when $EDITOR not set

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug 03 2012 David Malcolm <dmalcolm@redhat.com> - 0.6.4-4
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 05 2012 Ralph Bean <rbean@redhat.com> - 0.6.4-2
- Corrected spelling error in description.

* Thu Jun 28 2012 Ralph Bean <rbean@redhat.com> - 0.6.4-1
- initial package for Fedora
