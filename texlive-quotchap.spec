# revision 28046
# category Package
# catalog-ctan /macros/latex/contrib/quotchap
# catalog-date 2012-10-20 22:28:24 +0200
# catalog-license gpl
# catalog-version 1.1
Name:		texlive-quotchap
Version:	1.1
Release:	2
Summary:	Decorative chapter headings
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/quotchap
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/quotchap.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/quotchap.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/quotchap.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package for creating decorative chapter headings with
quotations. Uses graphical and coloured output and by default
needs the "Adobe standard font set" (as supported by psnfss).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/quotchap/quotchap.sty
%doc %{_texmfdistdir}/doc/latex/quotchap/README
%doc %{_texmfdistdir}/doc/latex/quotchap/document.pdf
%doc %{_texmfdistdir}/doc/latex/quotchap/document.tex
%doc %{_texmfdistdir}/doc/latex/quotchap/quotchap.pdf
#- source
%doc %{_texmfdistdir}/source/latex/quotchap/quotchap.dtx
%doc %{_texmfdistdir}/source/latex/quotchap/quotchap.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
