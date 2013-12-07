# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/tableaux
# catalog-date 2008-11-10 21:50:32 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-tableaux
Version:	20081110
Release:	4
Summary:	Construct tables of signs and variations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tableaux
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tableaux.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tableaux.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package uses PStricks; the user may define the width of the
table, the number of lines and the height of each line.
Placement of labels within the boxes may be absolute, or as a
percentage of the width; various other controls are available.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tableaux/minimum.sty
%{_texmfdistdir}/tex/latex/tableaux/tableau.sty
%doc %{_texmfdistdir}/doc/latex/tableaux/exemples.pdf
%doc %{_texmfdistdir}/doc/latex/tableaux/exemples.tex
%doc %{_texmfdistdir}/doc/latex/tableaux/tableau.pdf
%doc %{_texmfdistdir}/doc/latex/tableaux/tableau.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20081110-2
+ Revision: 756428
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20081110-1
+ Revision: 719634
- texlive-tableaux
- texlive-tableaux
- texlive-tableaux

