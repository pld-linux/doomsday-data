# NOTE:
# - sure this package could be instead doom-data, but doomsday engine is the best!
# TODO
# - hexen2, doom2, Plutionia and Tnt could be available freely.
Summary:	Doom, Heretic and Hexen .wadfiles
Summary(pl.UTF-8):	Pliki .wad z Dooma, Heretica i Hexena
Name:		doomsday-data
Version:	0.1
Release:	0.2
License:	?
Group:		Applications/Games
Source0:	Doom.wad
# NoSource0-md5:	c4fe9fd920207691a9f493668e0a2083
NoSource:	0
Source1:	Plutonia.wad
# NoSource1-md5:	75c8cf89566741fa9d22447604053bd7
NoSource:	1
Source2:	Tnt.wad
# NoSource2-md5:	4e158d9953c79ccf97bd0663244cc6b6
NoSource:	2
Source3:	Heretic.wad
# NoSource3-md5:	ae779722390ec32fa37b0d361f7d82f8
NoSource:	3
Source4:	Hexen.wad
# NoSource4-md5:	abb033caf81e26f12a2103e1fa25453f
NoSource:	4
Requires:	doomsday
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gamedatadir	%{_datadir}/deng/Data

%description
This package contains wad files for jDoom:
- Doom - Doom I
- Plutonia
- Tnt
- Heretic - Heretic I
- Hexen - Hexen I

%description -l pl.UTF-8
Ten pakiet zawiera pliki wad dla jDooma:
- Doom - Doom I
- Plutonia
- Tnt
- Heretic - Heretic I
- Hexen - Hexen I

%prep
%setup -q -c -T
cp -p %{SOURCE0} .
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .
cp -p %{SOURCE3} .
cp -p %{SOURCE4} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_gamedatadir}/j{Doom,Heretic,Hexen}

cp -p Doom.wad Plutonia.wad Tnt.wad $RPM_BUILD_ROOT%{_gamedatadir}/jDoom
cp -p Heretic.wad $RPM_BUILD_ROOT%{_gamedatadir}/jHeretic
cp -p Hexen.wad $RPM_BUILD_ROOT%{_gamedatadir}/jHexen

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_gamedatadir}/j*/*.wad
