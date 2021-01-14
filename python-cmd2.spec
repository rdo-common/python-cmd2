%{?python_enable_dependency_generator}
%global pypi_name cmd2

Name:             python-%{pypi_name}
Version:          1.4.0
Release:          1.1%{?dist}
Summary:          Extra features for standard library's cmd module

License:          MIT
URL:              https://pypi.python.org/pypi/cmd2
Source0:          %{pypi_source}
BuildArch:        noarch

BuildRequires:    git
Patch0001:        0001-Remove-dep-on-setuptools_scm-3.0.patch

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

%package -n python3-cmd2
Summary:          %{summary}
BuildRequires:    python3-devel
BuildRequires:    python3-setuptools
BuildRequires:    python3-setuptools_scm
BuildRequires:    dos2unix

Requires:         python3-pyparsing
Requires:         python3-pyperclip
Requires:         python3-six
Requires:         python3-wcwidth
Requires:         /usr/bin/which
%{?python_provide:%python_provide python3-cmd2}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version} -S git

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc CHANGELOG.md CONTRIBUTING.md README.md CODE_OF_CONDUCT.md docs
%{python3_sitelib}/cmd2
%{python3_sitelib}/%{pypi_name}-%{version}*

%changelog
* Fri Dec 11 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.4.0-1
- Update to latest upstream release 1.4.0

* Thu Nov 19 2020 Joel Capitao <jcapitao@redhat.com> - 1.3.11-1
- Update to 1.3.11.

* Sun Sep 27 2020 Kevin Fenzi <kevin@scrye.com> - 1.3.10-1
- Update to 1.3.10. Fixes bug #1878431

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.16-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.16-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 24 2019 Kevin Fenzi <kevin@scrye.com> - 0.9.16-1
- Update to 0.9.16. Fixes bug #1732777

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.8-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 25 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.8-7
- Subpackage python2-cmd2 has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Haïkel Guémar <hguemar@fedoraproject.org> - 0.8.8-5
- More dependencies

* Wed Jul 25 2018 Haïkel Guémar <hguemar@fedoraproject.org> - 0.8.8-4
- Add missing wcwidth dependency

* Wed Jul 25 2018 Haïkel Guémar <hguemar@fedoraproject.org> - 0.8.8-3
- Modernize spec file
- Add missing pyperclip dependency (blocks RHBZ#1605632)

* Tue Jul 24 2018 Alfredo Moralejo <amoralej@redhat.com> - 0.8.8-2
- Added setuptools as BuildRequires.

* Mon Jul 23 2018 Kevin Fenzi <kevin@scrye.com> - 0.8.8-1
- Fix FTBFS bug #1605635
- Update to 0.8.8 - Fixes bug #1568598

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
