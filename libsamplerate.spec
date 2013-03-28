%define	major	0
%define	libname	%mklibname samplerate %{major}
%define	devname	%mklibname samplerate -d

Summary:	Audio Sample Rate Converter library
Name:		libsamplerate
Version:	0.1.8
Release:	3
License:	GPLv2+
Group:		Sound
URL:		http://www.mega-nerd.com/SRC/index.html
Source0:	http://www.mega-nerd.com/SRC/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(fftw3) >= 3

%description
Secret Rabbit Code (aka libsamplerate) is a Sample Rate Converter for
audio. One example of where such a thing would be useful is
converting audio from the CD sample rate of 44.1kHz to the 48kHz
sample rate used by DAT players.

SRC is capable of arbitrary and time varying conversions ; from
downsampling by a factor of 12 to upsampling by the same
factor. Arbitrary in this case means that the ratio of input and
output sample rates can be an irrational number. The conversion ratio
can also vary with time for speeding up and slowing down effects.

SRC provides a small set of converters to allow quality to be traded
off against computation cost. The current best converter provides a
signal-to-noise ratio of 97dB with -3dB passband extending from DC to
96% of the theoretical best bandwidth for a given pair of input and
output sample rates.

%package -n	%{libname}
Summary:	Audio Sample Rate Converter shared library
Group:		System/Libraries

%description -n	%{libname}
Secret Rabbit Code (aka libsamplerate) is a Sample Rate Converter for
audio. One example of where such a thing would be useful is
converting audio from the CD sample rate of 44.1kHz to the 48kHz
sample rate used by DAT players.

SRC is capable of arbitrary and time varying conversions ; from
downsampling by a factor of 12 to upsampling by the same
factor. Arbitrary in this case means that the ratio of input and
output sample rates can be an irrational number. The conversion ratio
can also vary with time for speeding up and slowing down effects.

SRC provides a small set of converters to allow quality to be traded
off against computation cost. The current best converter provides a
signal-to-noise ratio of 97dB with -3dB passband extending from DC to
96% of the theoretical best bandwidth for a given pair of input and
output sample rates.

This package contains the shared library required for running programs
using %{name}.

%package -n	%{devname}
Summary:	Audio Sample Rate Converter development files
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
Secret Rabbit Code (aka libsamplerate) is a Sample Rate Converter for
audio. One example of where such a thing would be useful is
converting audio from the CD sample rate of 44.1kHz to the 48kHz
sample rate used by DAT players.

SRC is capable of arbitrary and time varying conversions ; from
downsampling by a factor of 12 to upsampling by the same
factor. Arbitrary in this case means that the ratio of input and
output sample rates can be an irrational number. The conversion ratio
can also vary with time for speeding up and slowing down effects.

SRC provides a small set of converters to allow quality to be traded
off against computation cost. The current best converter provides a
signal-to-noise ratio of 97dB with -3dB passband extending from DC to
96% of the theoretical best bandwidth for a given pair of input and
output sample rates.

This package contains the C headers and other files needed to compile
programs with %{name}.

%package	progs
Summary:	Audio Sample Rate Converter
Group:		Sound

%description	progs
Secret Rabbit Code (aka libsamplerate) is a Sample Rate Converter for
audio. One example of where such a thing would be useful is
converting audio from the CD sample rate of 44.1kHz to the 48kHz
sample rate used by DAT players.

SRC is capable of arbitrary and time varying conversions ; from
downsampling by a factor of 12 to upsampling by the same
factor. Arbitrary in this case means that the ratio of input and
output sample rates can be an irrational number. The conversion ratio
can also vary with time for speeding up and slowing down effects.

SRC provides a small set of converters to allow quality to be traded
off against computation cost. The current best converter provides a
signal-to-noise ratio of 97dB with -3dB passband extending from DC to
96% of the theoretical best bandwidth for a given pair of input and
output sample rates.

This package contains a command line utility based on %{name}.

%prep
%setup -q

%build
autoreconf -fi
%configure2_5x
%make

%check
make check

%install
%makeinstall_std
rm -rf %{buildroot}%{_datadir}/doc/libsamplerate0-dev

%files -n %{libname}
%{_libdir}/libsamplerate.so.%{major}*

%files -n %{devname}
%doc doc/*
%{_libdir}/libsamplerate.so
%{_libdir}/libsamplerate.a
%{_libdir}/pkgconfig/samplerate.pc
%{_includedir}/samplerate.h

%files progs
%doc AUTHORS ChangeLog
%{_bindir}/sndfile-resample


%changelog
* Mon May 14 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.1.8-3
+ Revision: 798827
- rebuild to get rid of rpmlib(DistEpoch)

* Sun Mar 11 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.1.8-2
+ Revision: 784182
- drop ancient obsoletes
- reenable regression tests
- use pkgconfig() deps for buildrequires
- cleanups

* Wed Aug 17 2011 Götz Waschk <waschk@mandriva.org> 0.1.8-1
+ Revision: 694831
- new version
- remove extra docs

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1.7-5
+ Revision: 661524
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.7-4mdv2011.0
+ Revision: 602604
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.7-3mdv2010.1
+ Revision: 520903
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.1.7-2mdv2010.0
+ Revision: 425704
- rebuild

* Mon Feb 16 2009 Götz Waschk <waschk@mandriva.org> 0.1.7-1mdv2009.1
+ Revision: 340736
- disable checks
- update to new version 0.1.7

* Tue Jan 27 2009 Götz Waschk <waschk@mandriva.org> 0.1.6-1mdv2009.1
+ Revision: 334158
- new version
- drop patch

* Mon Jan 12 2009 Götz Waschk <waschk@mandriva.org> 0.1.5-1mdv2009.1
+ Revision: 328508
- fix checks
- update to new version 0.1.5

* Sun Jul 06 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.4-1mdv2009.0
+ Revision: 232077
- update to new version 0.1.4

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu Apr 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1.3-1mdv2009.0
+ Revision: 195270
- 0.1.3

* Thu Feb 21 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.3-0.pre6.3mdv2008.1
+ Revision: 173759
- new license policy
- rebuild against libsndfile

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Oct 02 2007 Funda Wang <fwang@mandriva.org> 0.1.3-0.pre6.2mdv2008.0
+ Revision: 94725
- fix provides

* Fri Jul 20 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.3-0.pre6.1mdv2008.0
+ Revision: 53953
- new prerelease

* Tue Jun 26 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.3-0.pre5.2mdv2008.0
+ Revision: 44720
- adjust provides

* Sat Jun 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.3-0.pre5.1mdv2008.0
+ Revision: 43354
- new version (prerelease)
- new devel library policy
- spec file clean


* Wed Nov 29 2006 Götz Waschk <waschk@mandriva.org> 0.1.2-3mdv2007.0
+ Revision: 88780
- Import libsamplerate

* Wed Nov 29 2006 G�tz Waschk <waschk@mandriva.org> 0.1.2-3mdv2007.1
- add check section

* Mon Nov 28 2005 Götz Waschk <waschk@mandriva.org> 0.1.2-2mdk
- yearly rebuild

* Tue Nov 09 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.1.2-1mdk
- New release 0.1.2

* Tue Jul 20 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.1.1-1mdk
- reenable unit-at-a-time
- New release 0.1.1

* Tue Jun 15 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.1.0-2mdk
- fix buildrequires
- lower optflags
- reenable libtoolize

* Fri May 07 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.1.0-1mdk
- don't libtoolize
- drop prefix
- add source URL
- new version

