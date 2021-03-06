%define debug_package %{nil}

Name:           js_of_ocaml
Version:        1.3.2
Release:        1
Summary:        Compile OCaml programs to javascript
License:        LGPL and others
Group:          Development/Other
URL:            http://ocsigen.org/download/js_of_ocaml-1.3.2.tar.gz
Source0:        http://ocsigen.org/download/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml ocaml-findlib ocaml-findlib-devel deriving-ocsigen-devel ocaml-lwt-devel ocaml-camlp4-devel ocaml-ocamldoc
Requires:       ocaml ocaml-findlib ocaml-findlib-devel deriving-ocsigen-devel ocaml-lwt-devel ocaml-camlp4-devel

%description
Compile OCaml programs to Javascript.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
#Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/ocaml
mkdir -p %{buildroot}/%{_libdir}/ocaml/stublibs
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export OCAMLFIND_LDCONF=ignore
mkdir -p %{buildroot}/%{_bindir}
make install BINDIR=%{buildroot}/%{_bindir}/

%clean
rm -rf %{buildroot}

%files
# This space intentionally left blank

%files devel
%defattr(-,root,root)
%doc LICENSE README CHANGES
%{_libdir}/ocaml/js_of_ocaml/*
%{_libdir}/ocaml/stublibs/dlljs_of_ocaml.so
%{_libdir}/ocaml/stublibs/dlljs_of_ocaml.so.owner
%{_bindir}/js_of_ocaml

%changelog
* Sun Jun  2 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

