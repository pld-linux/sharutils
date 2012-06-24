Summary:	GNU shar utils - shar, unshar, uuencode, uudecode
Summary(de):	GNU-shar-Dienstprogramme - shar, unshar, uuencode, uudecode
Summary(es):	Utilitarios shar de la GNU - shar, unshar, uuencode, uudecode
Summary(fr):	Utilitaires shar de GNU - shar, unshar, uuencode, uudecode
Summary(pl):	Narz�dzia z GNU shar - shar, unshar, uuencode, uudecode
Summary(pt_BR):	Utilit�rios shar da GNU - shar, unshar, uuencode, uudecode
Summary(ru):	������� GNU shar ��� �������� � ���������� shell-�������
Summary(tr):	Ar�ivleme ve kabuk ara�lar�
Summary(uk):	���̦�� GNU shar ��� ��������� �� ���������� shell-��Ȧצ�
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
Sie k�nnen die shar-Dienstprogramme zum Verschl�sseln und Packen einer
Reihe von Dateien (bin�r oder Text) in ein einfaches Textformat
verwenden Dieses Format kann sicher per E-Mail oder andere Verfahren
gesendet werden, bei denen das Senden von Bin�rdateien schwierig ist.

%description -l es
Los utilitarios shar pueden ser usados para codificar y empaquetar
varios archivos, binarios y/o texto, en un formato especial de texto
plano. Este formato puede ser seguramente mandado a trav�s de mail o
otros medios donde mandar archivos binarios sea dif�cil.

%description -l fr
Les utilitaires shar servent � encoder et empaqueter un certain nombre
de fichiers, binaires et/ou texte, sous un format texte sp�cial. Ce
format peut �tre envoy� sans probl�me par courrier ou par d'autres
moyens o� l'envoi de fichiers binaires est difficile.

%description -l pl
Narz�dzia shar s�u�� do przekszta�cania i dystrybucji wielu plik�w
binarnych i/lub tekstowych w jednym, tekstowym archiwum. Archiwum
mo�na nast�pnie wysy�a� poczt� elektroniczn� albo innymi metodami,
kt�re uniemo�liwiaj� lub znacznie utrudniaj� transmisj� plik�w
binarnych.

%description -l pt_BR
Os utilit�rios shar podem ser usados para codificar e empacotar v�rios
arquivos, bin�rios e/ou texto, em um formato especial de texto plano.
Este formato pode ser seguramente mandado atrav�s de mail ou outros
meios onde mandar arquivos bin�rios � dif�cil.

%description -l ru
������� shar ����� ���� ������������ ��� ����������� � ��������
���������� ������, �������� �/��� ���������, � ����������� ���� �����
���������� �������. ���� ���� ����� ���� ������ e-mail'�� ��� ������
��������, ��� ������� �������� ������ ����������.

%description -l tr
shar ara�lar�, derlemi� ya da metin bi�imindeki dosyalar� d�z metin
bi�iminde kodlamak i�in kullan�labilir. Bu bi�imdeki dosya, posta ile
ya da derlenmi� dosyalar�n g�nderilmesinin sorun ��kard��� di�er
programlar �zerinden g�venli bir �ekilde g�nderilebilir.

%description -l uk
���̦�� shar ������ ���� ���������Φ ��� ��������� �� �������� ˦�����
���̦�, �צ������ ��/��� ���������, � ���æ������ ���� �����
���������� �������. ��� ���� ����� ��������� ����������� ������ ��
����� ��������, ��� ����� ������� �צ������ ���̦� �� Ц�����դ����.

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
