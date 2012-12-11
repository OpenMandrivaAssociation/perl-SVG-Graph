%define upstream_name	 SVG-Graph
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Visualize your data in Scalable Vector Graphics (SVG) format
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/SVG/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(SVG)
BuildRequires:	perl(Statistics::Descriptive)
BuildRequires:	perl(Math::Spline)
BuildRequires:	perl(Tree::DAG_Node)
BuildArch:	noarch

%description
SVG::Graph is a suite of perl modules for plotting data. SVG::Graph currently
supports plots of one-, two- and three-dimensional data, as well as N-ary
rooted trees. 

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
make test

%files 
%doc README Changes
%{perl_vendorlib}/SVG
%{_mandir}/*/*


%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.0
+ Revision: 404425
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.02-2mdv2009.0
+ Revision: 268718
- rebuild early 2009.0 package (before pixel changes)

* Thu Jun 12 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-1mdv2009.0
+ Revision: 218355
- update to new version 0.02

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jul 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-7mdv2008.0
+ Revision: 47037
- rebuild


* Fri Jun 09 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-6mdv2007.0
- spec cleanup
- %%mkrel

* Tue Jun 07 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-5mdk 
- better url
- spec cleanup
- make test in %%check

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.01-4mdk 
- fix summary
- fix directory ownership

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.01-3mdk
- fix buildrequires in a backward compatible way

* Fri Jul 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.01-2mdk 
- rpmbuildupdate aware

* Tue Jan 06 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.01-1mdk
- first mdk release

