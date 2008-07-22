%define major 2
%define minor 2

%define realname QGLViewer

%define libname %mklibname %{realname} %{major}
%define libnamedev %mklibname %{realname} -d


Name:		libQGLViewer
Version:	%{major}.%{minor}.6
Release:	%mkrel 4
Summary:	Qt based OpenGL generic 3D viewer library
License:	GPL
Group:		System/Libraries
Source:		http://artis.imag.fr/Members/Gilles.Debunne/QGLViewer/src/%{name}-%{version}-1.tar.gz
URL:		http://artis.imag.fr/Members/Gilles.Debunne/QGLViewer
Buildroot:      %{_tmppath}/%{name}-%{version}-buildroot

BuildRequires: qt3-devel
BuildRequires: MesaGLU-devel

%description
A versatile 3D viewer library for 3D application development.
Features many useful classical functionalities such as a camera trackball,
screenshot savings, stereo display, (hierarchical) frames that can be moved
with the mouse, keyFrame interpolator...

%package -n %libname
Summary:        Qt based OpenGL generic 3D viewer library
License:        GPL
Group:          System/Libraries
Provides:	lib%{realname} = %{version}-%{release}
Obsoletes:	%mklibname %{realname} 1 3
Obsoletes:	lib%{realname} < %{version}

%description  -n %libname
A versatile 3D viewer library for 3D application development.
Features many useful classical functionalities such as a camera trackball,
screenshot savings, stereo display, (hierarchical) frames that can be moved
with the mouse, keyFrame interpolator...

%package -n %libnamedev
Summary: The libQGLViewer header files, documentation and examples
Group: System/Libraries
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Provides: %{realname}-devel = %{version}-%{release}
Obsoletes: %mklibname -d %{realname} 1 3

%description -n %libnamedev
This package contains the header files for libQGLViewer.
Install this package if you want to develop programs that uses 
libQGLViewer. A reference documentation and pedagogical
examples are included. 

%prep
%setup -q -n %{name}-%{version}-1
  
%build
cd %{realname}

%{qt3dir}/bin/qmake LIB_DIR=%{_libdir}
make

%install
rm -rf $RPM_BUILD_ROOT
cd %{realname}
make install INSTALL_ROOT=%{buildroot}

# fwang: remove unused files
rm -f %{buildroot}%{_libdir}/*.prl

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %libname
%defattr(-,root,root)
%doc CHANGELOG LICENCE README
%{_libdir}/*.so.*

%files -n %libnamedev
%defattr(-,root,root)
%dir %{_includedir}/%{realname}
%{_includedir}/%{realname}
%{_libdir}/*.so

%doc %{_docdir}/%{realname}
