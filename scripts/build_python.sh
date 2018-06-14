cp -r ../backend-code temp
pip install -r ./temp/requirements.txt -t ./temp
cd temp
zip -r ../build.zip .
cd ..
rm -rf temp
