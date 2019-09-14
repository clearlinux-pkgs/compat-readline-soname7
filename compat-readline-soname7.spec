#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB5869F064EA74AB (chet@cwru.edu)
#
Name     : compat-readline-soname7
Version  : 7.0
Release  : 4
URL      : http://mirrors.kernel.org/gnu/readline/readline-7.0.tar.gz
Source0  : http://mirrors.kernel.org/gnu/readline/readline-7.0.tar.gz
Source1 : http://mirrors.kernel.org/gnu/readline/readline-7.0.tar.gz.sig
Summary  : Gnu Readline library for command line editing
Group    : Development/Tools
License  : GPL-3.0
Requires: compat-readline-soname7-lib = %{version}-%{release}
Requires: compat-readline-soname7-license = %{version}-%{release}
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : ncurses-dev
BuildRequires : ncurses-dev32
# Suppress generation of debuginfo
%global debug_package %{nil}
Patch1: 0001-Defaultinput-meta-output-meta-to-on.patch
Patch2: cve-2014-2524.nopatch
Patch3: 0001-Support-stateless-inputrc-configuration.patch
Patch4: build.patch
Patch5: readline-6.2-shlib.patch
Patch6: tinfow.patch

%description
Introduction
============
This is the Gnu Readline library, version 7.0.
The Readline library provides a set of functions for use by applications
that allow users to edit command lines as they are typed in.  Both
Emacs and vi editing modes are available.  The Readline library includes
additional functions to maintain a list of previously-entered command
lines, to recall and perhaps reedit those lines, and perform csh-like
history expansion on previous commands.

%package lib
Summary: lib components for the compat-readline-soname7 package.
Group: Libraries
Requires: compat-readline-soname7-license = %{version}-%{release}

%description lib
lib components for the compat-readline-soname7 package.


%package lib32
Summary: lib32 components for the compat-readline-soname7 package.
Group: Default
Requires: compat-readline-soname7-license = %{version}-%{release}

%description lib32
lib32 components for the compat-readline-soname7 package.


%package license
Summary: license components for the compat-readline-soname7 package.
Group: Default

%description license
license components for the compat-readline-soname7 package.


%prep
%setup -q -n readline-7.0
%patch1 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
pushd ..
cp -a readline-7.0 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1567834728
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static --with-curses --enable-multibyte
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static --with-curses --enable-multibyte   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check
cd ../build32;
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1567834728
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/compat-readline-soname7
cp COPYING %{buildroot}/usr/share/package-licenses/compat-readline-soname7/COPYING
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install
## Remove excluded files
rm -f %{buildroot}/usr/include/readline/chardefs.h
rm -f %{buildroot}/usr/include/readline/history.h
rm -f %{buildroot}/usr/include/readline/keymaps.h
rm -f %{buildroot}/usr/include/readline/readline.h
rm -f %{buildroot}/usr/include/readline/rlconf.h
rm -f %{buildroot}/usr/include/readline/rlstdc.h
rm -f %{buildroot}/usr/include/readline/rltypedefs.h
rm -f %{buildroot}/usr/include/readline/tilde.h
rm -f %{buildroot}/usr/lib32/libhistory.so
rm -f %{buildroot}/usr/lib32/libreadline.so
rm -f %{buildroot}/usr/lib64/libhistory.so
rm -f %{buildroot}/usr/lib64/libreadline.so
rm -f %{buildroot}/usr/share/doc/readline/CHANGES
rm -f %{buildroot}/usr/share/doc/readline/INSTALL
rm -f %{buildroot}/usr/share/doc/readline/README
rm -f %{buildroot}/usr/share/info/history.info
rm -f %{buildroot}/usr/share/info/readline.info
rm -f %{buildroot}/usr/share/info/rluserman.info
rm -f %{buildroot}/usr/share/man/man3/history.3
rm -f %{buildroot}/usr/share/man/man3/readline.3

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/libhistory.so.7
/usr/lib64/libhistory.so.7.0
/usr/lib64/libreadline.so.7
/usr/lib64/libreadline.so.7.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libhistory.so.7
/usr/lib32/libhistory.so.7.0
/usr/lib32/libreadline.so.7
/usr/lib32/libreadline.so.7.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/compat-readline-soname7/COPYING
