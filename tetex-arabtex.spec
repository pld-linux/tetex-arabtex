%define _short_name 	arabtex
Summary:	Set of LaTeX macros for arabtex
Name:		tetex-arabtex
Version:	1
Release:	6
License:	nonfree
Group:		Applications/Publishing/TeX
Group(de):	Applikationen/Publizieren/TeX
Group(pl):	Aplikacje/Publikowanie/TeX
Source0:	ftp://ftp.informatik.uni-stuttgart.de/pub/%{_short_name}/%{_short_name}.tar.Z
Requires:	tetex
Requires:	tetex-latex
BuildRequires:	tetex-latex
Prereq:		tetex >= 1.0.7.beta_20001218-2 
Prereq:		/usr/bin/mktexlsr
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set of LaTeX macros for arabtex.

%prep
%setup -q -n %{_short_name}

%build

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

gzip -9nf {announce,changes,readme}.txt doc/{readme.305,arabtex.doc,arabtex.faq} 

%post 
%{_bindir}/mktexlsr
echo arabtex.map >>/etc/sysconfig/tetex-updmap/maps.lst
/usr/bin/tetex-updmap

%postun
%{_bindir}/mktexlsr
sed -e 's/arabtex.map//' < /etc/sysconfig/tetex-updmap/maps.lst> %{tmpdir}/updmap 
cp %{tmpdir}/updmap /etc/sysconfig/tetex-updmap/maps.lst
/usr/bin/tetex-updmap

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc *.gz doc/*.gz examples report arabtex.htm arabtex.gif 
%{_datadir}/texmf/tex/%{_short_name}
%{_datadir}/texmf/source/%{_short_name}
%{_datadir}/texmf/fonts/tfm/%{_short_name}
%{_datadir}/texmf/fonts/type1/%{_short_name}/
%{_datadir}/texmf/dvips/config/*
