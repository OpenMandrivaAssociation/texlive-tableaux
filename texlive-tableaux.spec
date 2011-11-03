# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/tableaux
# catalog-date 2008-11-10 21:50:32 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-tableaux
Version:	20081110
Release:	1
Summary:	Construct tables of signs and variations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tableaux
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tableaux.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tableaux.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package uses PStricks; the user may define the width of the
table, the number of lines and the height of each line.
Placement of labels within the boxes may be absolute, or as a
percentage of the width; various other controls are available.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tableaux/minimum.sty
%{_texmfdistdir}/tex/latex/tableaux/tableau.sty
%doc %{_texmfdistdir}/doc/latex/tableaux/exemples.pdf
%doc %{_texmfdistdir}/doc/latex/tableaux/exemples.tex
%doc %{_texmfdistdir}/doc/latex/tableaux/tableau.pdf
%doc %{_texmfdistdir}/doc/latex/tableaux/tableau.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
