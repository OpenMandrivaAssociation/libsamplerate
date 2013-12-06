%define	major	0
%define	libname	%mklibname samplerate %{major}
%define	devname	%mklibname samplerate -d

Summary:	Audio Sample Rate Converter library
Name:		libsamplerate
Version:	0.1.8
Release:	10
License:	GPLv2+
Group:		Sound
Url:		http://www.mega-nerd.com/SRC/index.html
Source0:	http://www.mega-nerd.com/SRC/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(fftw3) >= 3
BuildRequires:	pkgconfig(sndfile)

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
This package contains the shared library required for running programs
using %{name}.

%package -n	%{devname}
Summary:	Audio Sample Rate Converter development files
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
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
autoreconf -fi

%build
%configure2_5x --disable-static
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
%{_libdir}/pkgconfig/samplerate.pc
%{_includedir}/samplerate.h

%files progs
%doc AUTHORS ChangeLog
%{_bindir}/sndfile-resample

