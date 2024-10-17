Name:		texlive-tableaux
Version:	42413
Release:	2
Summary:	Construct tables of signs and variations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tableaux
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tableaux.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tableaux.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
