Summary:	GNU shar utils - shar, unshar, uuencode, uudecode
Summary(de.UTF-8):	GNU-shar-Dienstprogramme - shar, unshar, uuencode, uudecode
Summary(es.UTF-8):	Utilitarios shar de la GNU - shar, unshar, uuencode, uudecode
Summary(fr.UTF-8):	Utilitaires shar de GNU - shar, unshar, uuencode, uudecode
Summary(pl.UTF-8):	Narzędzia z GNU shar - shar, unshar, uuencode, uudecode
Summary(pt_BR.UTF-8):	Utilitários shar da GNU - shar, unshar, uuencode, uudecode
Summary(ru.UTF-8):	Утилиты GNU shar для создания и распаковки shell-архивов
Summary(tr.UTF-8):	Arşivleme ve kabuk araçları
Summary(uk.UTF-8):	Утиліти GNU shar для створення та розпаковки shell-архівів
Name:		sharutils
Version:	4.7
Release:	1
License:	GPL v3+
Group:		Applications
Source0:	ftp://ftp.gnu.org/gnu/sharutils/REL-%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	729c070d814d9c688489d88dd7fd3efb
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	336f405f69324d129a6ccd3b66f8eb6c
Patch0:		%{name}-info.patch
Patch1:		%{name}-sh.patch
Patch2:		%{name}-gettext17.patch
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel >= 0.14.5
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

%description -l de.UTF-8
Sie können die shar-Dienstprogramme zum Verschlüsseln und Packen einer
Reihe von Dateien (binär oder Text) in ein einfaches Textformat
verwenden Dieses Format kann sicher per E-Mail oder andere Verfahren
gesendet werden, bei denen das Senden von Binärdateien schwierig ist.

%description -l es.UTF-8
Los utilitarios shar pueden ser usados para codificar y empaquetar
varios archivos, binarios y/o texto, en un formato especial de texto
plano. Este formato puede ser seguramente mandado a través de mail o
otros medios donde mandar archivos binarios sea difícil.

%description -l fr.UTF-8
Les utilitaires shar servent à encoder et empaqueter un certain nombre
de fichiers, binaires et/ou texte, sous un format texte spécial. Ce
format peut être envoyé sans problème par courrier ou par d'autres
moyens où l'envoi de fichiers binaires est difficile.

%description -l pl.UTF-8
Narzędzia shar służą do przekształcania i dystrybucji wielu plików
binarnych i/lub tekstowych w jednym, tekstowym archiwum. Archiwum
można następnie wysyłać pocztą elektroniczną albo innymi metodami,
które uniemożliwiają lub znacznie utrudniają transmisję plików
binarnych.

%description -l pt_BR.UTF-8
Os utilitários shar podem ser usados para codificar e empacotar vários
arquivos, binários e/ou texto, em um formato especial de texto plano.
Este formato pode ser seguramente mandado através de mail ou outros
meios onde mandar arquivos binários é difícil.

%description -l ru.UTF-8
Утилиты shar могут быть использованы для кодирования и упаковки
нескольких файлов, бинарных и/или текстовых, в специальный файл чисто
текстового формата. Этот файл может быть послан e-mail'ом или другим
способом, где посылка бинарных файлов затруднена.

%description -l tr.UTF-8
shar araçları, derlemiş ya da metin biçimindeki dosyaları düz metin
biçiminde kodlamak için kullanılabilir. Bu biçimdeki dosya, posta ile
ya da derlenmiş dosyaların gönderilmesinin sorun çıkardığı diğer
programlar üzerinden güvenli bir şekilde gönderilebilir.

%description -l uk.UTF-8
Утиліти shar можуть бути використані для кодування та упаковки кількох
файлів, двійкових та/або текстових, в спеціальний файл чисто
текстового формату. Цей файл можна надсилати електронною поштою чи
іншим способом, при якому посилка двійкових файлів не підтримується.

%prep
%setup -q -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
