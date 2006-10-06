Summary:	Coraid Ethernet Console client
Summary(pl):	Klient Coraid Ethernet Console (konsoli ethernetowej Coraid)
Name:		cec
Version:	4
Release:	1
License:	BSD
Group:		Networking
Source0:	http://dl.sourceforge.net/aoetools/%{name}-%{version}.tgz
# Source0-md5:	0b556d9e0aac29b14a38feb72f4cfa78
URL:		http://aoetools.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Coraid Ethernet Console (cec) is a lightweight protocol for
connecting two endpoints using raw ethernet frames. The communication
is not secure.

cec is also the name of the client used to connect to cec servers. It
will run on Linux, and BSD flavors supporting BPF.

%description -l pl
Coraid Ethernet Console (cec) to lekki protokó³ pozwalaj±cy na
po³±czenie dwóch koñców przy u¿yciu surowych ramek ethernetowych.
Komunikacja nie jest bezpieczna.

cec to tak¿e nazwa klienta s³u¿±cego do ³±czenia z serwerami cec.
Dzia³a pod Linuksem i odmianami BSD z obs³ug± BPF.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install cec $RPM_BUILD_ROOT%{_sbindir}
install cec.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE NEWS README
%attr(755,root,root) %{_sbindir}/cec
%{_mandir}/man8/cec.8*
