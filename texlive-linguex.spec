# revision 19440
# category Package
# catalog-ctan /macros/latex/contrib/linguex
# catalog-date 2010-06-01 09:12:12 +0200
# catalog-license lppl
# catalog-version 4.3
Name:		texlive-linguex
Version:	4.3
Release:	1
Summary:	Format linguists' examples
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/linguex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/linguex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/linguex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This bundle comprises two packages: - The linguex package
facilitates the formatting of linguist examples, automatically
taking care of example numbering, indentations, indexed
brackets, and the '*' in grammaticality judgments. - The ps-
trees package provides linguistic trees, building on the macros
of tree-dvips, but overcoming some of the older package's
shortcomings.

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
%{_texmfdistdir}/tex/latex/linguex/linguex.sty
%{_texmfdistdir}/tex/latex/linguex/linguho.sty
%{_texmfdistdir}/tex/latex/linguex/ps-trees.sty
%doc %{_texmfdistdir}/doc/latex/linguex/README
%doc %{_texmfdistdir}/doc/latex/linguex/README.TEXLIVE
%doc %{_texmfdistdir}/doc/latex/linguex/linguex-doc.pdf
%doc %{_texmfdistdir}/doc/latex/linguex/linguex-doc.tex
%doc %{_texmfdistdir}/doc/latex/linguex/ps-trees-doc.pdf
%doc %{_texmfdistdir}/doc/latex/linguex/ps-trees-doc.tex
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
