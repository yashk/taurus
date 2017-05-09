rm -rf build/tools
virtualenv --clear build
source build/bin/activate

# run installation test
cd build # cd is to make it not find bzt package from sources
pip install --upgrade ../dist/bzt-*.tar.gz
# pip install locustio
cd ..
#rm -rf ~/.bzt

bzt customReportSample.yml