%undefine _debugsource_packages
%define git 20240603
%define git2 r602.04db56a

Name: gpu-screen-recorder
Version: 1.0.0
Release: 0.%{git}.%{git2}
Summary: This is a screen recorder that has minimal impact on system performance.
Url: https://git.dec05eba.com/gpu-screen-recorder/about/
Group: Video
License: GPL-3.0-only
Source0: https://dec05eba.com/snapshot/gpu-screen-recorder.git.%{git2}.tar.gz
Source1: https://dec05eba.com/snapshot/gpu-screen-recorder-gtk.git.r283.09a288f.tar.gz

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

%package cli
Summary: The cli applitation for %name
Group: Video

%package gtk
Summary: The gui app for %name
Group: Video
Requires: %name-cli

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

%description cli
This package contains cli app for screen recorder

%description gtk
This package contains gui app for screen recorder

%prep
%autosetup -c -n %{name} 
#-a1
#-a1
#autosetup -n gpu-screen-recorder.git.r602.04db56a -p1
#autosetup

%build
#add_optflags %optflags_shared
./build.sh
./gpu-screen-recorder-gtk/build.sh

%install
install -Dm755 "gsr-kms-server" %buildroot%_bindir/gsr-kms-server
install -Dm755 "gpu-screen-recorder" %buildroot%_bindir/gpu-screen-recorder
install -Dm644 "extra/gpu-screen-recorder.service" %buildroot/%_unitdir/gpu-screen-recorder.service

cd gpu-screen-recorder-gtk
install -Dm755 "gpu-screen-recorder-gtk" %buildroot%_bindir/gpu-screen-recorder-gtk
install -Dm644 "gpu-screen-recorder-gtk.desktop" %buildroot%_desktopdir/com.dec05eba.gpu_screen_recorder.desktop
install -Dm644 com.dec05eba.gpu_screen_recorder.appdata.xml %buildroot%_datadir/metainfo/com.dec05eba.gpu_screen_recorder.appdata.xml
install -Dm644 icons/hicolor/64x64/apps/com.dec05eba.gpu_screen_recorder.png %buildroot%_datadir/icons/hicolor/64x64/apps/com.dec05eba.gpu_screen_recorder.png
install -Dm644 icons/hicolor/128x128/apps/com.dec05eba.gpu_screen_recorder.png %buildroot%_datadir/icons/hicolor/128x128/apps/com.dec05eba.gpu_screen_recorder.png

%files cli
%_bindir/gsr-kms-server
%_bindir/gpu-screen-recorder
%_unitdir/gpu-screen-recorder.service

%files gtk
#_bindir/gpu-screen-recorder-gtk
#_desktopdir/com.dec05eba.gpu_screen_recorder.desktop
#_datadir/metainfo/com.dec05eba.gpu_screen_recorder.appdata.xml
#_datadir/icons/hicolor/64x64/apps/com.dec05eba.gpu_screen_recorder.png
#_datadir/icons/hicolor/128x128/apps/com.dec05eba.gpu_screen_recorder.png
