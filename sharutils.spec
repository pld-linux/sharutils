Summary:	GNU shar utils - shar, unshar, uuencode, uudecode
Summary(de):	GNU-shar-Dienstprogramme - shar, unshar, uuencode, uudecode
Summary(fr):	Utilitaires shar de GNU - shar, unshar, uuencode, uudecode
Summary(pl):	Narz�dzia z GNU shar - shar, unshar, uuencode, uudecode
Summary(tr):	Ar�ivleme ve kabuk ara�lar�
Name:		sharutils
Version:	4.2
Release:	14
Copyright:	GPL
Group:		Utilities
Group(pl):	Narz�dzia
Source:		ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Patch0:		sharutils.patch
Patch1:		sharutils-pl.patch
Patch2:		sharutils-info.patch
Patch3:		sharutils-autoconf_fix.patch
Patch4:		sharutils-y2k.patch
Patch5:		sharutils-spaces.patch
Patch6:		sharutils-sh.patch
Patch7:		sharutils-tmpfix.patch
Prereq:		/sbin/install-info
Buildroot:	/tmp/%{name}-%{version}-root

%description
The shar utilities can be used to encode and package a number of
files, binary and/or text, in a special plain text format.  This
format can safely be sent through email or other means where
sending binary files is difficult.

%description -l de
Sie k�nnen die shar-Dienstprogramme zum Verschl�sseln und Packen einer
Reihe von Dateien (bin�r oder Text) in ein einfaches Textformat verwenden
Dieses Format kann sicher per E-Mail oder andere Verfahren
gesendet werden, bei denen das Senden von Bin�rdateien schwierig ist.

%description -l fr
Les utilitaires shar servent � encoder et empaqueter un certain
nombre de fichiers, binaires et/ou texte, sous un format texte
sp�cial. Ce format peut �tre envoy� sans probl�me par courrier ou
par d'autres moyens o� l'envoi de fichiers binaires est difficile.

%description -l pl
Narz�dzia shar s�u�� do przekszta�cenia i dystrybuowania wielu plik�w
binarnych i/lub tekstowych w jednym, tekstowym archiwum. Archiwum mo�na
nast�pnie wysy�a� e-poczt� albo innymi metodami, kt�re zabraniaj�
transmisji plik�w binarnych, lub jest ona wysoce utrudniona.

%description -l tr
shar ara�lar�, derlemi� ya da metin bi�imindeki dosyalar� d�z metin
bi�iminde kodlamak i�in kullan�labilir. Bu bi�imdeki dosya, posta ile
ya da derlenmi� dosyalar�n g�nderilmesinin sorun ��kard��� di�er programlar
�zerinden g�venli bir �ekilde g�nderilebilir.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build

LDFLAGS="-s"; export LDFLAGS
%configure \
	--mandir=%{_mandir} \
	--infodir=%{_infodir} \
	--enable-nsl \
	--without-gnu-gettext

make all localedir=%{_datadir}/locale

%install
rm -rf $RPM_BUILD_ROOT

make install install-man \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	infodir=$RPM_BUILD_ROOT%{_infodir}

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/{sharutils*,remsync*} \
	$RPM_BUILD_ROOT%{_mandir}/man?/* ChangeLog NEWS

%find_lang %{name}

%post
/sbin/install-info %{_infodir}/sharutils.info.gz /etc/info-dir

%preun
if [ $1 = 0 ]; then
	/sbin/install-info --delete %{_infodir}/sharutils.info.gz /etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {ChangeLog,NEWS}.gz

%attr(755,root,root) %{_bindir}/*

%{_infodir}/*.info.gz
%{_mandir}/man[15]/*

%changelog
* Thu May 20 1999 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [2.4-14]
- FHS 2.0,
- added support for pl,
- added some macros,
- build prepare for Ra.

* Tue Sep  1 1998 Marcin Korzonek <mkorz@shadow.eu.org>
- build against glibc-2.1,
- translations modified for pl,
- changed files permission.
- start at RH spec file.
