%global tl_name tableaux
%global tl_revision 42413

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Construct tables of signs and variations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tableaux
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tableaux.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tableaux.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package uses PSTricks; the user may define the width of the table,
the number of lines and the height of each line. Placement of labels
within the boxes may be absolute, or as a percentage of the width;
various other controls are available.

