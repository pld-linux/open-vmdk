Summary:	Open VMDK - assistant tool for creating Open Virtual Appliance (OVA)
Summary(pl.UTF-8):	Open VMDK - narzędzie pomagające przy tworzeniu Open Virtual Appliance (OVA)
Name:		open-vmdk
%define	gitref	875f4162c91c7fc7bc450dccaf7b896a927fa42b
%define	snap	20211104
Version:	0
Release:	0.%{snap}.1
License:	Apache v2.0
Group:		Applications/File
Source0:	https://github.com/vmware/open-vmdk/archive/%{gitref}/%{name}-%{snap}.tar.gz
# Source0-md5:	ab2448b64262ccb43a0ec545f18156d2
URL:		https://github.com/vmware/open-vmdk
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Open VMDK is an assistant tool for creating Open Virtual Appliance
(OVA). An OVA is a tar archive file with Open Virtualization Format
(OVF) files inside, which is composed of an OVF descriptor with
extension .ovf, a virtual machine disk image file with extension
.vmdk, and a manifest file with extension .mf.

%description -l pl.UTF-8
Open VMDK to narzędzie pomagające przy tworzeniu OVA (Open Virtual
Appliance). OVA to plik archiwum tar zawierające pliki OVF (Open
Virtualization Format), składające się z opisu OVF z rozszerzeniem
.ovf, pliku obrazu dysku maszyny wirtualnej z rozszerzeniem .vmdk
oraz pliku manifestu z rozszerzeniem .mf.

%prep
%setup -q -n %{name}-%{gitref}

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -W -Wall" \
	LDFLAGS="%{rpmldflags} -lz"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/mkova.sh
%attr(755,root,root) %{_bindir}/vmdk-convert
