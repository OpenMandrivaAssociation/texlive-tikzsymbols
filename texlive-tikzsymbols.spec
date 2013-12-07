# revision 31297
# category Package
# catalog-ctan /graphics/pgf/contrib/tikzsymbols
# catalog-date 2013-07-28 14:35:06 +0200
# catalog-license lppl1.3
# catalog-version 3.0
Name:		texlive-tikzsymbols
Version:	3.0
Release:	3
Summary:	Some symbols created using TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/tikzsymbols
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzsymbols.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzsymbols.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzsymbols.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides various emoticons, cooking symbols and
trees.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tikzsymbols/tikzsymbols.sty
%doc %{_texmfdistdir}/doc/latex/tikzsymbols/README
%doc %{_texmfdistdir}/doc/latex/tikzsymbols/tikzsymbols.pdf
#- source
%doc %{_texmfdistdir}/source/latex/tikzsymbols/tikzsymbols.dtx
%doc %{_texmfdistdir}/source/latex/tikzsymbols/tikzsymbols.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
