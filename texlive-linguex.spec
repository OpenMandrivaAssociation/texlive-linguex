Name:		texlive-linguex
Version:	30815
Release:	1
Summary:	Format linguists' examples
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/linguex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/linguex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/linguex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This bundle comprises two packages: - The linguex package
facilitates the formatting of linguist examples, automatically
taking care of example numbering, indentations, indexed
brackets, and the '*' in grammaticality judgments. - The ps-
trees package provides linguistic trees, building on the macros
of tree-dvips, but overcoming some of the older package's
shortcomings.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/linguex/linguex.sty
%{_texmfdistdir}/tex/latex/linguex/linguho.sty
%{_texmfdistdir}/tex/latex/linguex/ps-trees.sty
%doc %{_texmfdistdir}/doc/latex/linguex/README
%doc %{_texmfdistdir}/doc/latex/linguex/linguex-doc.pdf
%doc %{_texmfdistdir}/doc/latex/linguex/linguex-doc.tex
%doc %{_texmfdistdir}/doc/latex/linguex/ps-trees-doc.pdf
%doc %{_texmfdistdir}/doc/latex/linguex/ps-trees-doc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
