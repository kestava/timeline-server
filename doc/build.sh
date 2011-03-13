#!/bin/sh

# This script runs Sphinx to build HTML documentation.

echo Executing sphinx-build from $KESTAVA_TIMELINE_SERVER_SPHINX_BUILD

# Use the directory where this script is located as a starting point.
basedir=`realpath $0`
#echo $basedir
basedir=`dirname $basedir`
echo Base directory: $basedir

sourcedir=$basedir/source
echo Source directory: $sourcedir

builddir=$basedir/build
echo Build directory: $builddir

# Clear away the build directory
if [ -d "$builddir" ]; then
    rm -r $builddir
fi

# sphinx-build is the application that generates output based on the file
# files contained in $sourcedir.
$KESTAVA_TIMELINE_SERVER_SPHINX_BUILD -b html $sourcedir $builddir
