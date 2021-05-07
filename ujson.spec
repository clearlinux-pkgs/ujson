#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ujson
Version  : 3.2.0
Release  : 15
URL      : https://files.pythonhosted.org/packages/53/2a/dc633a35e21e2d712f142cbb5c796e8364147d49aa3174cadfd08f6e9895/ujson-3.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/53/2a/dc633a35e21e2d712f142cbb5c796e8364147d49aa3174cadfd08f6e9895/ujson-3.2.0.tar.gz
Summary  : Ultra fast JSON encoder and decoder for Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: ujson-license = %{version}-%{release}
Requires: ujson-python = %{version}-%{release}
Requires: ujson-python3 = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-scons
BuildRequires : setuptools_scm

%description
=========

%package license
Summary: license components for the ujson package.
Group: Default

%description license
license components for the ujson package.


%package python
Summary: python components for the ujson package.
Group: Default
Requires: ujson-python3 = %{version}-%{release}

%description python
python components for the ujson package.


%package python3
Summary: python3 components for the ujson package.
Group: Default
Requires: python3-core
Provides: pypi(ujson)

%description python3
python3 components for the ujson package.


%prep
%setup -q -n ujson-3.2.0
cd %{_builddir}/ujson-3.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1599843676
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ujson
cp %{_builddir}/ujson-3.2.0/deps/double-conversion/COPYING %{buildroot}/usr/share/package-licenses/ujson/8d434c9c1704b544a8b0652efbc323380b67f9bc
cp %{_builddir}/ujson-3.2.0/deps/double-conversion/LICENSE %{buildroot}/usr/share/package-licenses/ujson/8d434c9c1704b544a8b0652efbc323380b67f9bc
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ujson/8d434c9c1704b544a8b0652efbc323380b67f9bc

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
