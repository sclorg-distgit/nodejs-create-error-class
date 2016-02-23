%{?scl:%scl_package nodejs-%{module_name}}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global module_name create-error-class
%global commit0 bec0186ac350c5b89b1707d395c23a5a080b4f45
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           %{?scl_prefix}nodejs-%{module_name}
Version:        2.0.1
Release:        6%{?dist}
Summary:        Create Error classes

License:        MIT
URL:            https://github.com/floatdrop/create-error-class
Source0:        https://github.com/floatdrop/%{module_name}/archive/%{commit0}.tar.gz#/%{module_name}-%{shortcommit0}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  %{?scl_prefix}runtime

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm(inherits)
BuildRequires:  %{?scl_prefix}npm(capture-stack-trace)
BuildRequires:  %{?scl_prefix}npm(mocha)
%endif

%description
%{summary}.

%prep
%setup -q -n %{module_name}-%{commit0}
rm -rf node_modules

%nodejs_fixdep inherits

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -p package.json index.js %{buildroot}%{nodejs_sitelib}/%{module_name}
%nodejs_symlink_deps

%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
mocha
%endif

%files
%{!?_licensedir:%global license %doc}
%doc readme.md
%license license
%{nodejs_sitelib}/%{module_name}

%changelog
* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.1-6
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.1-5
- Rebuilt with updated metapackage

* Tue Jan 12 2016 Tomas Hrcka <thrcka@redhat.com> - 2.0.1-4
- Use macro to find provides and requires

* Tue Jan 12 2016 Tomas Hrcka <thrcka@redhat.com> - 2.0.1-3
- Enable scl macros, fix license macro for el6

* Thu Aug 06 2015 Parag Nemade <pnemade AT redhat DOT com> - 2.0.1-2
- Add missing BuildRequires
- fix summary macro
- correct check section

* Thu Jul 30 2015 Parag Nemade <pnemade AT redhat DOT com> - 2.0.1-1
- Initial packaging