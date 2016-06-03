Name:           ros-indigo-logger-binding
Version:        0.0.4
Release:        0%{?dist}
Summary:        ROS logger_binding package

Group:          Development/Libraries
License:        GPLv3
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-indigo-baselib-binding
Requires:       ros-indigo-roscpp
BuildRequires:  boost-devel
BuildRequires:  ros-indigo-baselib-binding
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-roscpp

%description
Includes libraries and headers to provide loose coupling to logging. Provides
loggers that use std streams, or ROS logging (if compiled with catkin).

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Jun 03 2016 Jennifer Buehler <jennifer.e.buehler@gmail.com> - 0.0.4-0
- Autogenerated by Bloom

* Wed Jun 01 2016 Jennifer Buehler <jennifer.e.buehler@gmail.com> - 0.0.3-1
- Autogenerated by Bloom

* Wed Jun 01 2016 Jennifer Buehler <jennifer.e.buehler@gmail.com> - 0.0.3-0
- Autogenerated by Bloom

* Wed Jun 01 2016 Jennifer Buehler <jennifer.e.buehler@gmail.com> - 0.0.2-1
- Autogenerated by Bloom

* Tue May 31 2016 Jennifer Buehler <jennifer.e.buehler@gmail.com> - 0.0.2-0
- Autogenerated by Bloom

* Mon May 30 2016 Jennifer Buehler <jennifer.e.buehler@gmail.com> - 0.0.1-0
- Autogenerated by Bloom

