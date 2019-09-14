Summary:         A small, flexible, terminal-based text editor
Name:            mle
Version:         1.4.0
Release:         1%{?dist}
License:         ASL 2.0
URL:             https://github.com/adsr/mle
Source:          https://github.com/adsr/mle/archive/v%{version}.tar.gz

BuildRequires:   gcc
BuildRequires:   pcre-devel
BuildRequires:   uthash-devel
BuildRequires:   lua-devel
BuildRequires:   termbox-devel

%description
mle is a small, flexible, terminal-based text editor written in C. 
Notable features include: full Unicode support, syntax highlighting, 
scriptable rc file, macros, search and replace (PCRE), window 
splitting, multiple cursors, and integration with various shell 
commands.

%prep
%setup -q
sed -i 's|-llua5.3|-llua|g' Makefile
sed -i 's|<lua5.3/lua.h>|<lua.h>|g' mle.h
sed -i 's|<lua5.3/lualib.h>|<lualib.h>|g' mle.h
sed -i 's|<lua5.3/lauxlib.h>|<lauxlib.h>|g' mle.h

%build
%make_build

%check
make %{?_smp_mflags} test

%install
%make_install DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix}
install -D -v -m 644 mle.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/mle.1

%files
%{_bindir}/mle
%{_mandir}/man1/mle.1*

%changelog
* Fri Sep 13 2019 Adam Saponara <as@php.net> - 1.4.0-1
- initial spec
