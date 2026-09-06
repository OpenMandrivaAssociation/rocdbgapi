# AMD GPU debug API (amd-dbgapi). TheRock 10.0.

Name:		rocdbgapi
Version:	10.0.0
Release:	1
Summary:	AMD GPU debug API library
License:	MIT
Group:		Development/Debuggers
URL:		https://github.com/ROCm/rocm-systems
Source0:	https://github.com/ROCm/rocm-systems/releases/download/therock-10.0/rocdbgapi.tar.gz#/rocdbgapi-%{version}.tar.gz

BuildRequires:	rocm-rpm-macros
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	rocm-runtime-devel
BuildRequires:	pkgconfig(libdw)
BuildRequires:	pkgconfig(libelf)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	cmake(amd_comgr)

%description
libamd-dbgapi is the low-level GPU debug API used by ROCgdb and
the ROCr debug agent.

%package devel
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Headers, pkgconfig and CMake package for amd-dbgapi.

%prep
%autosetup -n rocdbgapi -p1

%build
%cmake %{rocm_cmake_fhs} \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DBUILD_SHARED_LIBS=ON \
	-DAPI_TRACING=OFF \
	-DTHE_ROCK_BUILD=ON \
	-DROCM_PATH=%{_prefix} \
	-DCMAKE_PREFIX_PATH=%{_prefix} \
	-G Ninja

%ninja_build

%install
%ninja_install -C build

%files
%license LICENSE.txt
%doc README.md CHANGELOG.md
%{_libdir}/libamd-dbgapi.so.*

%files devel
%{_includedir}/amd-dbgapi/
%{_libdir}/libamd-dbgapi.so
%{_datadir}/pkgconfig/amd-dbgapi.pc
%{_libdir}/cmake/amd-dbgapi/
