%define major 0
%define libname %mklibname samplerate %{major}
%define develname %mklibname samplerate -d

Summary:	Audio Sample Rate Converter library
Name:		libsamplerate
Version:	0.1.3
Release:	%mkrel 1
License:	GPLv2+
Group:		Sound
URL:		http://www.mega-nerd.com/SRC/index.html
Source0:	http://www.mega-nerd.com/SRC/%{name}-%{version}.tar.gz
BuildRequires:	libsndfile-devel
BuildRequires:	fftw-devel >= 3
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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

%package -n	%{develname}
Summary:	Audio Sample Rate Converter development files
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{libname}-devel
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
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

%setup -qn %{name}-%{version}

%build
%configure2_5x
%make

%check
make check

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc doc/*
%{_libdir}/*.so
%{_libdir}/*a
%{_libdir}/pkgconfig/samplerate.pc
%{_includedir}/samplerate.h

%files progs
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%{_bindir}/sndfile-resample
