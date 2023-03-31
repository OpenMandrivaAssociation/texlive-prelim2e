Name:		texlive-prelim2e
Version:	57000
Release:	2
Summary:	Allows the marking of preliminary versions of a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/prelim2e
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/prelim2e.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/prelim2e.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/prelim2e.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Puts text below the normal page content (the default text marks
the document as draft and puts a timestamp on it). Can be used
together with e.g. the vrsion, rcs and rcsinfo packages. Uses
the everyshi package and can use the scrtime package from the
koma-script bundle.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/prelim2e
%{_texmfdistdir}/tex/latex/prelim2e
%doc %{_texmfdistdir}/doc/latex/prelim2e

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
