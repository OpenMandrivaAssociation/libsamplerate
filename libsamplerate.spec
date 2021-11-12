# libsamplerate is used by jackit,
# jackit is used by pulseaudio,
# pulseaudio is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%endif

%define major 0
%define libname %mklibname samplerate %{major}
%define devname %mklibname samplerate -d
%define lib32name %mklib32name samplerate %{major}
%define dev32name %mklib32name samplerate -d
%global optflags %{optflags} -O3

%bcond_without pgo

Summary:	Audio Sample Rate Converter library
Name:		libsamplerate
Version:	0.2.2
Release:	1
License:	GPLv2+
Group:		Sound
URL:		https://libsndfile.github.io/libsamplerate/
Source0:	https://github.com/libsndfile/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(fftw3) >= 3
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(alsa)
%if %{with compat32}
BuildRequires:	devel(libfftw3)
BuildRequires:	devel(libsndfile)
BuildRequires:	devel(libasound)
%endif

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

%package -n %{libname}
Summary:	Audio Sample Rate Converter shared library
Group:		System/Libraries

%description -n %{libname}
This package contains the shared library required for running programs
using %{name}.

%package -n %{devname}
Summary:	Audio Sample Rate Converter development files
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
This package contains the C headers and other files needed to compile
programs with %{name}.

%if %{with compat32}
%package -n %{lib32name}
Summary:	Audio Sample Rate Converter shared library (32-bit)
Group:		System/Libraries

%description -n %{lib32name}
This package contains the shared library required for running programs
using %{name}.

%package -n %{dev32name}
Summary:	Audio Sample Rate Converter development files (32-bit)
Group:		Development/C
Requires:	%{devname} = %{version}-%{release}
Requires:	%{lib32name} = %{version}-%{release}

%description -n %{dev32name}
This package contains the C headers and other files needed to compile
programs with %{name}.
%endif

%package progs
Summary:	Audio Sample Rate Converter
Group:		Sound

%description progs
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
export CONFIGURE_TOP="$(pwd)"

%if %{with compat32}
mkdir build32
cd build32
%configure32
%make_build
cd ..
%endif

mkdir build
cd build

%if %{with pgo}
export LLVM_PROFILE_FILE=%{name}-%p.profile.d
export LD_LIBRARY_PATH="$(pwd)"
CFLAGS="%{optflags} -fprofile-instr-generate" \
CXXFLAGS="%{optflags} -fprofile-instr-generate" \
FFLAGS="$CFLAGS" \
FCFLAGS="$CFLAGS" \
LDFLAGS="%{ldflags} -fprofile-instr-generate" \
%configure --disable-static

# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

export LD_LIBRARY_PATH="$(pwd)/src/.libs"
make check
unset LD_LIBRARY_PATH
unset LLVM_PROFILE_FILE
llvm-profdata merge --output=%{name}.profile *.profile.d

make clean

CFLAGS="%{optflags} -fprofile-instr-use=$(realpath %{name}.profile)" \
CXXFLAGS="%{optflags} -fprofile-instr-use=$(realpath %{name}.profile)" \
LDFLAGS="%{ldflags} -fprofile-instr-use=$(realpath %{name}.profile)" \
%endif
%configure --disable-static

# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%check
%if %{with compat32}
cd build32
export LD_LIBRARY_PATH="$(pwd)/src/.libs"
make check
unset LD_LIBRARY_PATH
cd ..
%endif

cd build
export LD_LIBRARY_PATH="$(pwd)/src/.libs"
make check
unset LD_LIBRARY_PATH

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build
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

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libsamplerate.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/libsamplerate.so
%{_prefix}/lib/pkgconfig/samplerate.pc
%endif
