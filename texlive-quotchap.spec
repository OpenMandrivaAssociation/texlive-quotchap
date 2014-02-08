# revision 21082
# category Package
# catalog-ctan /macros/latex/contrib/quotchap
# catalog-date 2011-01-16 00:30:55 +0100
# catalog-license gpl
# catalog-version 1.0
Name:		texlive-quotchap
Version:	1.0
Release:	3
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
quotations, a PostScript output device and the psnfss package
are needed, the color package and a greyscale output device are
recommended.

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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 755570
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719425
- texlive-quotchap
- texlive-quotchap
- texlive-quotchap
- texlive-quotchap

