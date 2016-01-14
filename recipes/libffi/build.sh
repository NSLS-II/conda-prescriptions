./configure --prefix=$PREFIX || exit 1
make || exit 1
make install || exit 1

cd $PREFIX
rm -rf share
mv lib/libffi-*/include include

if [ `uname -m` == x86_64 ]; then
    if [ -d "lib64" ]; then
        mv lib64/* lib/
        rmdir lib64
    fi
fi

sed -i s/'includedir=.*'/'includedir=\${exec_prefix}\/include'/g lib/pkgconfig/libffi.pc
