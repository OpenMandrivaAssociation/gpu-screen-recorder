#define git 20240603
#define git2 r602.04db56a
%define date 20250126
%define tag %{version}

%define devname %mklibname -d gpu-screen-recorder

Name: gpu-screen-recorder
Version: 5.9.2
Release: 1
Summary: This is a screen recorder that has minimal impact on system performance.
Url: https://git.dec05eba.com/gpu-screen-recorder/about/
Group: Video
License: GPL-3.0-only
# Use... git clone --branch 5.9.2 --depth 1 https://repo.dec05eba.com/gpu-screen-recorder
# for now lets choose tag instead of commit, so use 5.8.0
# then create .xz archive gpu-screen-recorder-5.1.0.tar.xz
Source0:  gpu-screen-recorder-%{version}.tar.xz
#Source0: https://dec05eba.com/snapshot/gpu-screen-recorder.git.%{git2}.tar.gz

BuildSystem: meson
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(libglvnd)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libva)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(xdamage)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(libavfilter)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(libcap)
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libswresample)
BuildRequires: vulkan-headers

Recommends:    gpu-screen-recorder-gui
%rename %{name}-cli

%description
This is a screen recorder that has minimal impact on system performance 
by recording your monitor using the GPU only, similar to shadowplay on windows. 
This is the fastest screen recording tool for Linux.
This screen recorder can be used for recording your desktop offline, 
for live streaming and for nvidia shadowplay-like instant replay,
where only the last few minutes are saved.
Supported video codecs:

    H264 (default on Intel)
    HEVC (default on AMD and NVIDIA)
    AV1 (not currently supported on NVIDIA if you use GPU Screen Recorder flatpak)
    
%package -n %{devname}
Summary:    Development files for %{name}
Requires:	%{name} = %{EVRD}
Provides:   %{name}-devel = %{EVRD}

%description -n %{devname}
This package contains development files for %{name}.

%files
%{_bindir}/gpu-screen-recorder
%{_bindir}/gsr-kms-server
%{_prefix}/lib/modprobe.d/gsr-nvidia.conf
%{_prefix}/lib/systemd/user/gpu-screen-recorder.service

%files -n %{devname}
%{_includedir}/gsr/plugin.h
