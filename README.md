The installation is also small

https://www.python.org/

https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python

Your attention to versions and number of processor cores ( -j128432 ;)

-- OpenSSL (3.2.0)
$ curl -O https://www.openssl.org/source/openssl-3.2.0.tar.gz
$ tar xzf openssl-3.2.0.tar.gz
pushd openssl-3.2.0
./config --prefix=/usr/local/custom-openssl --libdir=lib --openssldir=/etc/ssl
make -j1 depend
make -j4
sudo make install_sw
popd

## Python (3.12.1)
wget https://www.python.org/ftp/python/3.12.1/Python-3.12.1.tgz
## Include the source code (Uncomment the terms in your /etc/apt/sources.list)
sudo apt-get update
sudo apt-get build-dep python3
sudo apt-get install pkg-config
sudo apt-get install build-essential gdb lcov pkg-config libbz2-dev libffi-dev \
      libgdbm-dev libgdbm-compat-dev liblzma-dev libncurses5-dev libreadline6-dev \
      libsqlite3-dev libssl-dev lzma lzma-dev tk-dev uuid-dev zlib1g-dev
tar -xf Python-3.12.1.tgz && cd Python-3.12.1
./configure --enable-optimizations
make -j 4
sudo make altinstall
## prefix=/usr/local By default
