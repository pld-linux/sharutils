Summary:	GNU shar utils - shar, unshar, uuencode, uudecode
Summary(de):	GNU-shar-Dienstprogramme - shar, unshar, uuencode, uudecode
Summary(fr):	Utilitaires shar de GNU - shar, unshar, uuencode, uudecode
Summary(pl):	Narzêdzia z GNU shar - shar, unshar, uuencode, uudecode
Summary(tr):	Arþivleme ve kabuk araçlarý
Name:		sharutils
Version:	4.2
Release:	14
Copyright:	GPL
Group:		Utilities
Group(pl):	Narzêdzia
Source:		ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Patch0:		%{name}.patch
Patch1:		%{name}-pl.patch
Prereq:		/sbin/install-info
Buildroot:	/tmp/%{name}-%{version}-root

%description
The shar utilities can be used to encode and package a number of
files, binary and/or text, in a special plain text format.  This
format can safely be sent through email or other means where
sending binary files is difficult.

%description -l de
Sie können die shar-Dienstprogramme zum Verschlüsseln und Packen einer
Reihe von Dateien (binär oder Text) in ein einfaches Textformat verwenden
Dieses Format kann sicher per E-Mail oder andere Verfahren
gesendet werden, bei denen das Senden von Binärdateien schwierig ist.

%description -l fr
Les utilitaires shar servent à encoder et empaqueter un certain
nombre de fichiers, binaires et/ou texte, sous un format texte
spécial. Ce format peut être envoyé sans problème par courrier ou
par d'autres moyens où l'envoi de fichiers binaires est difficile.

%description -l pl
Narzêdzia shar s³u¿± do przekszta³cenia i dystrybuowania wielu plików
binarnych i/lub tekstowych w jednym, tekstowym archiwum. Archiwum mo¿na
nastêpnie wysy³aæ e-poczt± albo innymi metodami, które zabraniaj±
transmisji plików binarnych, lub jest ona wysoce utrudniona.

%description -l tr
shar araçlarý, derlemiþ ya da metin biçimindeki dosyalarý düz metin
biçiminde kodlamak için kullanýlabilir. Bu biçimdeki dosya, posta ile
ya da derlenmiþ dosyalarýn gönderilmesinin sorun çýkardýðý diðer programlar
üzerinden güvenli bir þekilde gönderilebilir.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoheader && autoconf 
CFLAGS=$RPM_OPT_FLAGS LDFLAGS=-s \
    ./configure \
	--prefix=%{_prefix} \
	--infodir=%{_infodir} \
	--enable-nsl \
	--with-gnu-gettext %{_target_platform}

make clean; make all;

%install
rm -rf $RPM_BUILD_ROOT

make install-man \
    mandir=$RPM_BUILD_ROOT%{_mandir}

make install \
    prefix=$RPM_BUILD_ROOT%{_prefix} \
    infodir=$RPM_BUILD_ROOT%{_infodir}

gzip -9nf $RPM_BUILD_ROOT%{_infodir}/{sharutils*,remsync*}
gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[15]/* ChangeLog NEWS

%post
/sbin/install-info %{_infodir}/sharutils.info.gz /etc/info-dir

%preun
if [ $1 = 0 ]; then
    /sbin/install-info --delete %{_infodir}/sharutils.info.gz /etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,NEWS}.gz

%attr(755,root,root) %{_bindir}/*

%{_infodir}/*.info.gz
%{_mandir}/man[15]/*

%lang(de) /usr/share/locale/de/LC_MESSAGES/sharutils.mo
%lang(fr) /usr/share/locale/fr/LC_MESSAGES/sharutils.mo
%lang(ja) /usr/share/locale/ja_JP.EUC/LC_MESSAGES/sharutils.mo
%lang(nl) /usr/share/locale/nl/LC_MESSAGES/sharutils.mo
%lang(pl) /usr/share/locale/pl/LC_MESSAGES/sharutils.mo
%lang(pt) /usr/share/locale/pt/LC_MESSAGES/sharutils.mo
%lang(sv) /usr/share/locale/sv/LC_MESSAGES/sharutils.mo

%changelog
* Thu May 20 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
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
