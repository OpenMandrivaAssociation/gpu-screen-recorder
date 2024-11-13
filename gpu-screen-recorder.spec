%undefine _debugsource_packages
#define git 20240603
#define git2 r602.04db56a
%define date 20241105
%define tag 4.6.2

Name: gpu-screen-recorder
Version: %{date}~%{tag}
Release: 1
Summary: This is a screen recorder that has minimal impact on system performance.
Url: https://git.dec05eba.com/gpu-screen-recorder/about/
Group: Video
License: GPL-3.0-only
# Use... git clone --branch 4.2.6 --depth 1 https://repo.dec05eba.com/gpu-screen-recorder
# for now lets choose tag instead of commit, so use 4.2.6
# then create .xz archive gpu-screen-recorder-4.6.2.tar.xz
Source0:  gpu-screen-recorder-%{tag}.tar.xz
#Source0: https://dec05eba.com/snapshot/gpu-screen-recorder.git.%{git2}.tar.gz

BuildRequires: meson
BuildRequires: pkgconfig(libglvnd)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libva)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(libavfilter)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(libcap)
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libswresample)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(appindicator3-0.1)

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


%prep
%autosetup -c -n %{name}-%{tag}

%build
%meson
%meson_build

%install
%meson_install

%files
