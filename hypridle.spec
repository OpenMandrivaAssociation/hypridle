Name:           hypridle
Version:        0.1.6
Release:        4
Summary:        Hyprland's idle daemon
License:        BSD-3-Clause
Group:          Hyprland
URL:            https://github.com/hyprwm/hypridle
Source0:        https://github.com/hyprwm/hypridle/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(hyprlang)
BuildRequires:  pkgconfig(hyprutils)
BuildRequires:  pkgconfig(hyprwayland-scanner)
BuildRequires:  pkgconfig(hyprland-protocols)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(sdbus-c++)

%description
%{summary}.

%prep
%autosetup -p1

%build
%cmake -DCMAKE_BUILD_TYPE:STRING=Release
%make_build

%install
%make_install -C build

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_userunitdir}/%{name}.service
%{_datadir}/hypr/hypridle.conf

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%postun
%systemd_user_postun %{name}.service
