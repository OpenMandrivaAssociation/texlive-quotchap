Name:		texlive-quotchap
Version:	56926
Release:	2
Summary:	Decorative chapter headings
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/quotchap
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/quotchap.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/quotchap.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/quotchap.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
