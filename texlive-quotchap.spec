# revision 21082
# category Package
# catalog-ctan /macros/latex/contrib/quotchap
# catalog-date 2011-01-16 00:30:55 +0100
# catalog-license gpl
# catalog-version 1.0
Name:		texlive-quotchap
Version:	1.0
Release:	1
Summary:	Decorative chapter headings
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/quotchap
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/quotchap.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/quotchap.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/quotchap.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A package for creating decorative chapter headings with
quotations, a PostScript output device and the psnfss package
are needed, the color package and a greyscale output device are
recommended.

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
%{_texmfdistdir}/tex/latex/quotchap/quotchap.sty
%doc %{_texmfdistdir}/doc/latex/quotchap/README
%doc %{_texmfdistdir}/doc/latex/quotchap/document.pdf
%doc %{_texmfdistdir}/doc/latex/quotchap/document.tex
%doc %{_texmfdistdir}/doc/latex/quotchap/quotchap.pdf
#- source
%doc %{_texmfdistdir}/source/latex/quotchap/quotchap.dtx
%doc %{_texmfdistdir}/source/latex/quotchap/quotchap.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
