./build_python.sh
aws lambda update-function-code --function-name backend-lambda --zip-file fileb://build.zip --publish
rm build.zip
