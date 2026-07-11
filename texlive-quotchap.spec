%global tl_name quotchap
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Decorative chapter headings
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/quotchap
License:	gpl2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/quotchap.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/quotchap.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/quotchap.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A package for creating decorative chapter headings with quotations. Uses
graphical and coloured output and by default needs the "Adobe standard
font set" (as supported by psnfss).

