%define major 2
%define minor 2

%define realname QGLViewer

%define libname %mklibname %{realname} %{major}_%{minor}
%define libnamedev %mklibname %{realname} %{major}_%{minor} -d


Name:		libQGLViewer
Version:	%{major}.%{minor}.6
Release: %mkrel 1

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

%description  -n %libname
A versatile 3D viewer library for 3D application development.
Features many useful classical functionalities such as a camera trackball,
screenshot savings, stereo display, (hierarchical) frames that can be moved
with the mouse, keyFrame interpolator...

%package -n %libnamedev
Summary: The libQGLViewer header files, documentation and examples
Group: System/Libraries
Requires: %{libname} = %{version}

%description -n %libnamedev
This package contains the header files for libQGLViewer.
Install this package if you want to develop programs that uses 
libQGLViewer. A reference documentation and pedagogical
examples are included. 

%prep
%define docdir %_docdir/QGLViewer
%define includeDir %_includedir/QGLViewer
%define libdir %_libdir
%setup -q -n %{name}-%{version}-1
  
%build
cd QGLViewer

%{qt3dir}/bin/qmake
make

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT%{includeDir}
%{__install} --mode=644 QGLViewer/*.h $RPM_BUILD_ROOT%{includeDir}
%{__install} -d $RPM_BUILD_ROOT%{includeDir}/cwFiles
%{__install} --mode=644 QGLViewer/*.cw $RPM_BUILD_ROOT%{includeDir}/cwFiles
#%{__install} --mode=644 QGLViewer/*.png $RPM_BUILD_ROOT%{includeDir}/cwFiles

%{__install} -d $RPM_BUILD_ROOT%{libdir}
%{__install} --mode=644 QGLViewer/libQGLViewer.so.%{version} $RPM_BUILD_ROOT%{libdir}
ln -s libQGLViewer.so.%{version} $RPM_BUILD_ROOT%{libdir}/libQGLViewer.so.%{major}.%{minor}
ln -s libQGLViewer.so.%{version} $RPM_BUILD_ROOT%{libdir}/libQGLViewer.so.%{major}
ln -s libQGLViewer.so.%{version} $RPM_BUILD_ROOT%{libdir}/libQGLViewer.so

# %{__install} -d $RPM_BUILD_ROOT%{_mandir}/man3
%{__install} -d $RPM_BUILD_ROOT%{docdir}
%{__install} -d $RPM_BUILD_ROOT%{docdir}/refManual
%{__install} -d $RPM_BUILD_ROOT%{docdir}/images
%{__install} -d $RPM_BUILD_ROOT%{docdir}/examples
%{__install} -d $RPM_BUILD_ROOT%{docdir}/examples/contribs
# %{__install} doc/man/man3/QGLViewer.3 $RPM_BUILD_ROOT%{_mandir}/man3/
# %{__install} doc/man/man3/qglviewer_* $RPM_BUILD_ROOT%{_mandir}/man3/
%{__install} --mode=644 doc/*.html doc/*.css $RPM_BUILD_ROOT%{docdir}
%{__install} --mode=644 INSTALL README LICENCE CHANGELOG $RPM_BUILD_ROOT%{docdir}
%{__install} --mode=644 doc/refManual/* $RPM_BUILD_ROOT%{docdir}/refManual
%{__install} --mode=644 doc/images/* $RPM_BUILD_ROOT%{docdir}/images
%{__install} --mode=644 doc/examples/*.html $RPM_BUILD_ROOT%{docdir}/examples
%{__install} --mode=644 examples/examples.pro $RPM_BUILD_ROOT%{docdir}/examples
%{__install} --mode=644 examples/contribs/contribs.pro $RPM_BUILD_ROOT%{docdir}/examples/contribs
for dir in `ls examples`
do
if [[ -d examples/$dir ]] && [[ $dir != "contribs" ]]
  then
    %{__install} -d $RPM_BUILD_ROOT%{docdir}/examples/$dir
    %{__install} --mode=644 examples/$dir/* $RPM_BUILD_ROOT%{docdir}/examples/$dir
  fi
done
for dir in `ls examples/contribs`
do
if [[ -d examples/contribs/$dir ]]
  then
    %{__install} -d $RPM_BUILD_ROOT%{docdir}/examples/contribs/$dir
    %{__install} --mode=644 examples/contribs/$dir/* $RPM_BUILD_ROOT%{docdir}/examples/contribs/$dir
  fi
done

%post -n %libname -p /sbin/ldconfig

%postun -n %libname -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %libname
%defattr(-,root,root)
%{libdir}/*.so*


%files -n %libnamedev
%defattr(-,root,root)
%dir %{includeDir}
%{includeDir}/*.h
%dir %{includeDir}/cwFiles
%{includeDir}/cwFiles/*.cw
#%{includeDir}/cwFiles/*.png

# %doc %{_mandir}/man3/QGLViewer.3.bz2
# %doc %{_mandir}/man3/qglviewer_*

%dir %{docdir}
%doc %{docdir}/*.html
%doc %{docdir}/*.css
%doc %{docdir}/README
%doc %{docdir}/LICENCE
%doc %{docdir}/INSTALL
%doc %{docdir}/CHANGELOG
%dir %{docdir}/refManual
%doc %{docdir}/refManual/*
%dir %{docdir}/images
%doc %{docdir}/images/*
%dir %{docdir}/examples
%doc %{docdir}/examples/*
# %doc %{docdir}/examples/*.html
# %doc %{docdir}/examples/*.pro
