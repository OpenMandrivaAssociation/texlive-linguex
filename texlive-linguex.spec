%global tl_name linguex
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.3
Release:	%{tl_revision}.1
Summary:	Format linguists examples
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/linguex
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/linguex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/linguex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This bundle comprises two packages: The linguex package facilitates the
formatting of linguist examples, automatically taking care of example
numbering, indentations, indexed brackets, and the '*' in grammaticality
judgments. The ps-trees package provides linguistic trees, building on
the macros of tree-dvips, but overcoming some of the older package's
shortcomings.

