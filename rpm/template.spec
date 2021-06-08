%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-pinocchio
Version:        2.6.1
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS pinocchio package

License:        BSD
URL:            https://github.com/stack-of-tasks/pinocchio
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       boost-python3-devel
Requires:       eigen3-devel
Requires:       python3-devel
Requires:       python3-numpy
Requires:       ros-noetic-catkin
Requires:       ros-noetic-eigenpy
Requires:       urdfdom-devel
BuildRequires:  boost-devel
BuildRequires:  boost-python3-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  eigen3-devel
BuildRequires:  git
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  ros-noetic-eigenpy
BuildRequires:  urdfdom-devel
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
A fast and flexible implementation of Rigid Body Dynamics algorithms and their
analytical derivatives.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/noetic

%changelog
* Wed Jun 09 2021 Justin Carpentier <justin.carpentier@inria.fr> - 2.6.1-1
- Autogenerated by Bloom

* Mon Apr 19 2021 Justin Carpentier <justin.carpentier@inria.fr> - 2.6.0-1
- Autogenerated by Bloom

* Sat Apr 03 2021 Justin Carpentier <justin.carpentier@inria.fr> - 2.5.6-2
- Autogenerated by Bloom

* Mon Jan 25 2021 Justin Carpentier <justin.carpentier@inria.fr> - 2.5.6-1
- Autogenerated by Bloom

* Mon Aug 31 2020 Justin Carpentier <justin.carpentier@inria.fr> - 2.5.0-1
- Autogenerated by Bloom

* Sat May 30 2020 Justin Carpentier <justin.carpentier@inria.fr> - 2.4.5-5
- Autogenerated by Bloom

* Tue May 26 2020 Justin Carpentier <justin.carpentier@inria.fr> - 2.4.5-4
- Autogenerated by Bloom

* Sat May 23 2020 Justin Carpentier <justin.carpentier@inria.fr> - 2.4.5-3
- Autogenerated by Bloom

* Fri May 22 2020 Justin Carpentier <justin.carpentier@inria.fr> - 2.4.5-2
- Autogenerated by Bloom

* Fri May 22 2020 Justin Carpentier <justin.carpentier@inria.fr> - 2.4.5-1
- Autogenerated by Bloom

