Summary:	GNU shar utils - shar, unshar, uuencode, uudecode
Summary(de):	GNU-shar-Dienstprogramme - shar, unshar, uuencode, uudecode
Summary(es):	Utilitarios shar de la GNU - shar, unshar, uuencode, uudecode
Summary(fr):	Utilitaires shar de GNU - shar, unshar, uuencode, uudecode
Summary(pl):	Narzêdzia z GNU shar - shar, unshar, uuencode, uudecode
Summary(pt_BR):	Utilitários shar da GNU - shar, unshar, uuencode, uudecode
Summary(ru):	õÔÉÌÉÔÙ GNU shar ÄÌÑ ÓÏÚÄÁÎÉÑ É ÒÁÓÐÁËÏ×ËÉ shell-ÁÒÈÉ×Ï×
Summary(tr):	Arþivleme ve kabuk araçlarý
Summary(uk):	õÔÉÌ¦ÔÉ GNU shar ÄÌÑ ÓÔ×ÏÒÅÎÎÑ ÔÁ ÒÏÚÐÁËÏ×ËÉ shell-ÁÒÈ¦×¦×
Name:		sharutils
Version:	4.2.1
Release:	14
License:	GPL
Group:		Applications
Source0:	ftp://ftp.gnu.org/pub/gnu/sharutils/%{name}-%{version}.tar.gz
# Source0-md5: b8ba1d409f07edcb335ff72a27bd9828
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5: 336f405f69324d129a6ccd3b66f8eb6c
Patch0:		%{name}.patch
Patch1:		%{name}-pl.patch
Patch2:		%{name}-info.patch
Patch3:		%{name}-autoconf_fix.patch
Patch4:		%{name}-spaces.patch
Patch5:		%{name}-sh.patch
Patch6:		%{name}-tmpfix.patch
Patch7:		%{name}-autoconf.patch
Patch8:		%{name}-po.patch
Patch9:		%{name}-uudecode.patch
Patch10:	%{name}-bo_fix.patch
#BuildRequires:	autoconf
#BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The sharutils package contains the GNU shar utilities, a set of tools
for encoding and decoding packages of files (in binary or text format)
in a special plain text format called shell archives (shar). This
format can be sent through email (which can be problematic for regular
binary files). The shar utility supports a wide range of capabilities
(compressing, uuencoding, splitting long files for multi-part
mailings, providing checksums), which make it very flexible at
creating shar files. After the files have been sent, the unshar tool
scans mail messages looking for shar files. Unshar automatically
strips off mail headers and introductory text and then unpacks the
shar files.

%description -l de
Sie können die shar-Dienstprogramme zum Verschlüsseln und Packen einer
Reihe von Dateien (binär oder Text) in ein einfaches Textformat
verwenden Dieses Format kann sicher per E-Mail oder andere Verfahren
gesendet werden, bei denen das Senden von Binärdateien schwierig ist.

%description -l es
Los utilitarios shar pueden ser usados para codificar y empaquetar
varios archivos, binarios y/o texto, en un formato especial de texto
plano. Este formato puede ser seguramente mandado a través de mail o
otros medios donde mandar archivos binarios sea difícil.

%description -l fr
Les utilitaires shar servent à encoder et empaqueter un certain nombre
de fichiers, binaires et/ou texte, sous un format texte spécial. Ce
format peut être envoyé sans problème par courrier ou par d'autres
moyens où l'envoi de fichiers binaires est difficile.

%description -l pl
Narzêdzia shar s³u¿± do przekszta³cania i dystrybucji wielu plików
binarnych i/lub tekstowych w jednym, tekstowym archiwum. Archiwum
mo¿na nastêpnie wysy³aæ poczt± elektroniczn± albo innymi metodami,
które uniemo¿liwiaj± lub znacznie utrudniaj± transmisjê plików
binarnych.

%description -l pt_BR
Os utilitários shar podem ser usados para codificar e empacotar vários
arquivos, binários e/ou texto, em um formato especial de texto plano.
Este formato pode ser seguramente mandado através de mail ou outros
meios onde mandar arquivos binários é difícil.

%description -l ru
õÔÉÌÉÔÙ shar ÍÏÇÕÔ ÂÙÔØ ÉÓÐÏÌØÚÏ×ÁÎÙ ÄÌÑ ËÏÄÉÒÏ×ÁÎÉÑ É ÕÐÁËÏ×ËÉ
ÎÅÓËÏÌØËÉÈ ÆÁÊÌÏ×, ÂÉÎÁÒÎÙÈ É/ÉÌÉ ÔÅËÓÔÏ×ÙÈ, × ÓÐÅÃÉÁÌØÎÙÊ ÆÁÊÌ ÞÉÓÔÏ
ÔÅËÓÔÏ×ÏÇÏ ÆÏÒÍÁÔÁ. üÔÏÔ ÆÁÊÌ ÍÏÖÅÔ ÂÙÔØ ÐÏÓÌÁÎ e-mail'ÏÍ ÉÌÉ ÄÒÕÇÉÍ
ÓÐÏÓÏÂÏÍ, ÇÄÅ ÐÏÓÙÌËÁ ÂÉÎÁÒÎÙÈ ÆÁÊÌÏ× ÚÁÔÒÕÄÎÅÎÁ.

%description -l tr
shar araçlarý, derlemiþ ya da metin biçimindeki dosyalarý düz metin
biçiminde kodlamak için kullanýlabilir. Bu biçimdeki dosya, posta ile
ya da derlenmiþ dosyalarýn gönderilmesinin sorun çýkardýðý diðer
programlar üzerinden güvenli bir þekilde gönderilebilir.

%description -l uk
õÔÉÌ¦ÔÉ shar ÍÏÖÕÔØ ÂÕÔÉ ×ÉËÏÒÉÓÔÁÎ¦ ÄÌÑ ËÏÄÕ×ÁÎÎÑ ÔÁ ÕÐÁËÏ×ËÉ Ë¦ÌØËÏÈ
ÆÁÊÌ¦×, Ä×¦ÊËÏ×ÉÈ ÔÁ/ÁÂÏ ÔÅËÓÔÏ×ÉÈ, × ÓÐÅÃ¦ÁÌØÎÉÊ ÆÁÊÌ ÞÉÓÔÏ
ÔÅËÓÔÏ×ÏÇÏ ÆÏÒÍÁÔÕ. ãÅÊ ÆÁÊÌ ÍÏÖÎÁ ÎÁÄÓÉÌÁÔÉ ÅÌÅËÔÒÏÎÎÏÀ ÐÏÛÔÏÀ ÞÉ
¦ÎÛÉÍ ÓÐÏÓÏÂÏÍ, ÐÒÉ ÑËÏÍÕ ÐÏÓÉÌËÁ Ä×¦ÊËÏ×ÉÈ ÆÁÊÌ¦× ÎÅ Ð¦ÄÔÒÉÍÕ¤ÔØÓÑ.

%prep
%setup -q -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

mv po/ja_JP.EUC.po po/ja.po
mv po/ja_JP.EUC.gmo po/ja.gmo

chmod -R u+w *

%build
#gettextize --copy --force
#aclocal
#autoconf
%configure2_13

%{__make} all localedir=%{_datadir}/locale

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install-man \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	infodir=$RPM_BUILD_ROOT%{_infodir} \
	localedir=$RPM_BUILD_ROOT%{_datadir}/locale

install -d $RPM_BUILD_ROOT%{_mandir}/{pl/man5,ja/man{1,5}}
install man/ja/man1/* $RPM_BUILD_ROOT%{_mandir}/ja/man1
install man/ja/man5/* $RPM_BUILD_ROOT%{_mandir}/ja/man5
install man/pl/man5/* $RPM_BUILD_ROOT%{_mandir}/pl/man5

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS README TODO AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_infodir}/*info*
%{_mandir}/man[15]/*
%lang(ja) %{_mandir}/ja/man?/*
%lang(pl) %{_mandir}/pl/man?/*
