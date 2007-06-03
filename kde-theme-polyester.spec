%define         _name polyester

Summary:	KDE theme - %{_name}
Summary(pl.UTF-8):	Motyw do KDE - %{_name}
Name:		kde-theme-%{_name}
Version:	1.0.1
Release:	1
License:	GPL
Group:		Themes
Source0:	http://www.notmart.org/files/polyester-%{version}.tar.bz2
# Source0-md5:	ad446cbaa846f660670315bad7c07dc0
URL:		http://www.kde-look.org/content/show.php?content=27968
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.5.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_name} KDE theme.

%description -l pl.UTF-8
Motyw KDE %{_name}.

%package -n kde-style-%{_name}
Summary:	KDE style - %{_name}
Summary(pl.UTF-8):	Styl do KDE - %{_name}
Group:		Themes
Requires:	kdelibs

%description -n kde-style-%{_name}
Polyester is a style and kwin decoration both aimed to be a good
balance between eye candy and simplicity.

%description -n kde-style-%{_name} -l pl.UTF-8
Styl Polyester to zestaw dekoracji dla kontrolek i okien stworzony
tak, aby zachować równowagę pomiędzy prostotą i dobrym wyglądem.

%package -n kde-colorscheme-%{_name}
Summary:	Color scheme for KDE style - %{_name}
Summary(pl.UTF-8):	Schemat kolorów do stylu KDE - %{_name}
Group:		Themes
Requires:	kdebase-core

%description -n kde-colorscheme-%{_name}
Color scheme for KDE style - %{_name}.

%description -n kde-colorscheme-%{_name} -l pl.UTF-8
Schemat kolorów do stylu KDE - %{_name}.

%package -n kde-decoration-%{_name}
Summary:	Kwin decoration - %{_name}
Summary(pl.UTF-8):	Dekoracja kwin - %{_name}
Group:		Themes
Requires:	kdebase-desktop-libs

%description -n kde-decoration-%{_name}
Kwin decoration - %{_name}.

%description -n kde-decoration-%{_name} -l pl.UTF-8
Dekoracja kwin - %{_name}.

%prep
%setup -q -n %{_name}-%{version}

%build
cp -f /usr/share/automake/config.sub admin

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir="%{_kdedocdir}"

%clean
rm -rf $RPM_BUILD_ROOT

%files -n kde-style-%{_name}
%defattr(644,root,root,755)
%{_libdir}/kde3/kstyle_*.la
%attr(755,root,root) %{_libdir}/kde3/kstyle_*.so
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/*.so
#%{_libdir}/kde3/plugins/styles/*.la
%{_datadir}/apps/kstyle/themes/*.themerc

%files -n kde-decoration-%{_name}
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin3_polyester.la
%attr(755,root,root) %{_libdir}/kde3/kwin3_polyester.so
%{_libdir}/kde3/kwin_polyester_config.la
%attr(755,root,root) %{_libdir}/kde3/kwin_polyester_config.so
%{_datadir}/apps/kwin/polyester.desktop

%files -n kde-colorscheme-%{_name}
%defattr(644,root,root,755)
%{_datadir}/apps/kdisplay/color-schemes/Polyester*.kcsrc
