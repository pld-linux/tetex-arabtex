%define _short_name 	arabtex
Summary:	Set of LaTeX macros for arabtex
Version:	1
Name:		tetex-arabtex
Release:	4
Copyright:	nonfree
Group:		Applications/Publishing/TeX
Group(de):	Applikationen/Publizieren/TeX
Group(pl):	Aplikacje/Publikowanie/TeX
Source0:	ftp://ftp.informatik.uni-stuttgart.de/pub/%{_short_name}/%{_short_name}.tar.Z
Requires:	tetex
Requires:	tetex-latex
BuildRequires:	tetex-latex
Prereq:		tetex
Prereq:		/usr/bin/mktexlsr
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Set of LaTeX macros for arabtex

%prep
%setup -q -n %{_short_name}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/%{_short_name} 
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/source/%{_short_name} 
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/fonts/tfm/%{_short_name} 
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/fonts/type1/%{_short_name} 
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/dvips/config
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/doc/%{_short_name}/{examples,report,doc}


install texinput/* $RPM_BUILD_ROOT%{_datadir}/texmf/tex/%{_short_name}/
install mfinput/* $RPM_BUILD_ROOT%{_datadir}/texmf/source/%{_short_name}/ 
install tfm/* $RPM_BUILD_ROOT%{_datadir}/texmf/fonts/tfm/%{_short_name}/ 
install psfonts/*pfb $RPM_BUILD_ROOT%{_datadir}/texmf/fonts/type1/%{_short_name}/ 
install psfonts/arabtex.map $RPM_BUILD_ROOT%{_datadir}/texmf/dvips/config/
install examples/* $RPM_BUILD_ROOT%{_datadir}/texmf/doc/%{_short_name}/examples 
install report/* $RPM_BUILD_ROOT%{_datadir}/texmf/doc/%{_short_name}/report
install doc/* $RPM_BUILD_ROOT%{_datadir}/texmf/doc/%{_short_name}/doc
install announce.txt arabtex.htm arabtex.gif changes.txt install.txt readme.txt \
             $RPM_BUILD_ROOT%{_datadir}/texmf/doc/%{_short_name}/doc

gzip -9nf $RPM_BUILD_ROOT%{_datadir}/texmf/doc/%{_short_name}/doc/{announce.txt,\
arabtex.htm,changes.txt,install.txt,readme.txt} 



%post 
%{_bindir}/mktexlsr
sed -e 's/extra_modules=\".*/\0 arabtex.map/' <%{_datadir}/texmf/dvips/config/updmap > %{tmpdir}/updmap 
cp %{tmpdir}/updmap %{_datadir}/texmf/dvips/config/
cd %{_datadir}/texmf/dvips/config/
chmod 700 updmap
./updmap

%postun
%{_bindir}/mktexlsr
sed -e 's/arabtex.map//' <%{_datadir}/texmf/dvips/config/updmap > %{tmpdir}/updmap 
cp %{tmpdir}/updmap %{_datadir}/texmf/dvips/config/
cd %{_datadir}/texmf/dvips/config/
chmod 700 updmap
./updmap

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%{_datadir}/texmf/tex/%{_short_name}/
%{_datadir}/texmf/source/%{_short_name}/
%{_datadir}/texmf/fonts/tfm/%{_short_name}/
%{_datadir}/texmf/fonts/type1/%{_short_name}/ 
%{_datadir}/texmf/dvips/config/
%doc %{_datadir}/texmf/doc/%{_short_name}/
