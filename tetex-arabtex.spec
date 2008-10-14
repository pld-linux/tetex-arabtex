%define _short_name 	arabtex
Summary:	Set of LaTeX macros for arabtex
Summary(pl.UTF-8):	Zestaw makr LaTeXa dla arabtexa
Name:		tetex-arabtex
Version:	1
Release:	7
License:	nonfree
Group:		Applications/Publishing/TeX
Source0:	ftp://ftp.informatik.uni-stuttgart.de/pub/%{_short_name}/%{_short_name}.tar.Z
# Source0-md5:	ba1a9a6796699d6bcda58e2225e28d9a
BuildRequires:	tetex-latex
PreReq:		tetex >= 1.0.7.beta_20001218-2
Requires(post,postun):	/usr/bin/mktexlsr
Requires(post,postun):	/usr/bin/tetex-updmap
Requires:	tetex
Requires:	tetex-latex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set of LaTeX macros for arabtex.

%description -l pl.UTF-8
Zestaw makr LaTeXa dla arabtexa.

%prep
%setup -q -n %{_short_name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/{tex/%{_short_name},source/%{_short_name}} \
	$RPM_BUILD_ROOT%{_datadir}/texmf/fonts/{tfm/%{_short_name},type1/%{_short_name}} \
	$RPM_BUILD_ROOT%{_datadir}/texmf/dvips/config

install texinput/* $RPM_BUILD_ROOT%{_datadir}/texmf/tex/%{_short_name}/
install mfinput/* $RPM_BUILD_ROOT%{_datadir}/texmf/source/%{_short_name}/
install tfm/* $RPM_BUILD_ROOT%{_datadir}/texmf/fonts/tfm/%{_short_name}/
install psfonts/*pfb $RPM_BUILD_ROOT%{_datadir}/texmf/fonts/type1/%{_short_name}/
install psfonts/arabtex.map $RPM_BUILD_ROOT%{_datadir}/texmf/dvips/config/

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
/usr/bin/mktexlsr
echo arabtex.map >>/etc/sysconfig/tetex-updmap/maps.lst
/usr/bin/tetex-updmap

%postun
umask 022
/usr/bin/mktexlsr
sed -e 's/arabtex.map//' /etc/sysconfig/tetex-updmap/maps.lst \
	> /etc/sysconfig/tetex-updmap/maps.lst.rpmtmp
mv -f /etc/sysconfig/tetex-updmap/maps.lst.rpmtmp /etc/sysconfig/tetex-updmap/maps.lst
/usr/bin/tetex-updmap

%files
%defattr(644,root,root,755)
%doc {announce,changes,readme}.txt doc/txt/{readme.305,arabtex.doc,arabtex.faq}
%doc examples arabtex.htm arabtex.gif
%{_datadir}/texmf/tex/%{_short_name}
%{_datadir}/texmf/source/%{_short_name}
%{_datadir}/texmf/fonts/tfm/%{_short_name}
%{_datadir}/texmf/fonts/type1/%{_short_name}
%{_datadir}/texmf/dvips/config/%{_short_name}.map
