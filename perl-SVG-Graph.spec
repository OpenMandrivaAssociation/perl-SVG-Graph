%define module	SVG-Graph
%define name	perl-%{module}
%define version 0.02
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Visualize your data in Scalable Vector Graphics (SVG) format
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/SVG/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
Buildrequires:	perl(SVG)
Buildrequires:	perl(Statistics::Descriptive)
Buildrequires:	perl(Math::Spline)
Buildrequires:	perl(Tree::DAG_Node)
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
SVG::Graph is a suite of perl modules for plotting data. SVG::Graph currently
supports plots of one-, two- and three-dimensional data, as well as N-ary
rooted trees. 

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/SVG
%{_mandir}/*/*

