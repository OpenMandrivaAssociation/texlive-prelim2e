%global tl_name prelim2e
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.00
Release:	%{tl_revision}.1
Summary:	Allows the marking of preliminary versions of a document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/prelim2e
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/prelim2e.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/prelim2e.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/prelim2e.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Puts text below the normal page content (the default text marks the
document as draft and puts a timestamp on it). Can be used together with
e.g. the vrsion, rcs and rcsinfo packages. Uses the everyshi package and
can use the scrtime package from the koma-script bundle.

