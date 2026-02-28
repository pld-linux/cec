Summary:	Coraid Ethernet Console client
Summary(pl.UTF-8):	Klient Coraid Ethernet Console (konsoli ethernetowej Coraid)
Name:		cec
Version:	14
Release:	2
License:	GPL v2
Group:		Networking
Source0:	http://downloads.sourceforge.net/aoetools/%{name}-%{version}.tgz
# Source0-md5:	d7a467eb70f2a1dcc27ec77085e00527
URL:		http://aoetools.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Coraid Ethernet Console (cec) is a lightweight protocol for
connecting two endpoints using raw ethernet frames. The communication
is not secure.

cec is also the name of the client used to connect to cec servers. It
will run on Linux, and BSD flavors supporting BPF.

%description -l pl.UTF-8
Coraid Ethernet Console (cec) to lekki protokół pozwalający na
połączenie dwóch końców przy użyciu surowych ramek ethernetowych.
Komunikacja nie jest bezpieczna.

cec to także nazwa klienta służącego do łączenia z serwerami cec.
Działa pod Linuksem i odmianami BSD z obsługą BPF.

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
%doc NEWS README cec.txt
%attr(755,root,root) %{_sbindir}/cec
%{_mandir}/man8/cec.8*
