./deploy_code.sh
aws lambda create-alias --name prod --function-name backend-lambda --function-version 9 --routing-config AdditionalVersionWeights={"8"=0.5} 
