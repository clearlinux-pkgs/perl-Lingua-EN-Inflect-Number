#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Lingua-EN-Inflect-Number
Version  : 1.12
Release  : 12
URL      : https://cpan.metacpan.org/authors/id/N/NE/NEILB/Lingua-EN-Inflect-Number-1.12.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NE/NEILB/Lingua-EN-Inflect-Number-1.12.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libl/liblingua-en-inflect-number-perl/liblingua-en-inflect-number-perl_1.12-1.debian.tar.xz
Summary  : 'Force number of words to singular or plural'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Lingua-EN-Inflect-Number-license = %{version}-%{release}
Requires: perl-Lingua-EN-Inflect-Number-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Lingua::EN::Inflect)

%description
This archive contains the distribution Lingua-EN-Inflect-Number,
version 1.12:
Force number of words to singular or plural

%package dev
Summary: dev components for the perl-Lingua-EN-Inflect-Number package.
Group: Development
Provides: perl-Lingua-EN-Inflect-Number-devel = %{version}-%{release}
Requires: perl-Lingua-EN-Inflect-Number = %{version}-%{release}

%description dev
dev components for the perl-Lingua-EN-Inflect-Number package.


%package license
Summary: license components for the perl-Lingua-EN-Inflect-Number package.
Group: Default

%description license
license components for the perl-Lingua-EN-Inflect-Number package.


%package perl
Summary: perl components for the perl-Lingua-EN-Inflect-Number package.
Group: Default
Requires: perl-Lingua-EN-Inflect-Number = %{version}-%{release}

%description perl
perl components for the perl-Lingua-EN-Inflect-Number package.


%prep
%setup -q -n Lingua-EN-Inflect-Number-1.12
cd %{_builddir}
tar xf %{_sourcedir}/liblingua-en-inflect-number-perl_1.12-1.debian.tar.xz
cd %{_builddir}/Lingua-EN-Inflect-Number-1.12
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Lingua-EN-Inflect-Number-1.12/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Lingua-EN-Inflect-Number
cp %{_builddir}/Lingua-EN-Inflect-Number-1.12/LICENSE %{buildroot}/usr/share/package-licenses/perl-Lingua-EN-Inflect-Number/f64962ea2646981898a121d94ec42de3a591f049
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Lingua-EN-Inflect-Number/48aa45c200805df9bfc9e90f8d938b2cb721afdd
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Lingua::EN::Inflect::Number.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Lingua-EN-Inflect-Number/48aa45c200805df9bfc9e90f8d938b2cb721afdd
/usr/share/package-licenses/perl-Lingua-EN-Inflect-Number/f64962ea2646981898a121d94ec42de3a591f049

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.2/Lingua/EN/Inflect/Number.pm
