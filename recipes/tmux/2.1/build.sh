export CFLAGS=-I$PREFIX/include/ncursesw 
# Why are the curses libraries in $PREFIX/include/ncursessw ???
./configure --prefix=$PREFIX
make -j$(getconf _NPROCESSORS_ONLN)
make install
