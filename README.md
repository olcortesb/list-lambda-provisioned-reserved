# Lambda Provisioned and Reserved Concurrency Lister

A serverless application that lists all AWS Lambda functions with provisioned or reserved concurrency configurations in a specified AWS region.

## Overview

This tool helps you identify and monitor Lambda functions that have either provisioned concurrency or reserved concurrency configured. This information is valuable for:

- Cost optimization
- Resource allocation planning
- Identifying functions with special concurrency settings
- Auditing Lambda configuration across your AWS account

## Architecture

The application consists of a single Lambda function that:

1. Lists all Lambda functions in the specified AWS region
2. Checks each function for reserved concurrency settings
3. Checks each function for provisioned concurrency settings
4. Outputs the results with function names and their concurrency configurations

## Prerequisites

- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
- AWS credentials configured with appropriate permissions
- Python 3.10 or later

## Deployment

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/list-lambda-provisioned-reserved.git
   cd list-lambda-provisioned-reserved
   ```

2. Update the `samconfig.toml` file with your AWS region and profile:
   ```toml
   region = "your-region"
   profile = "your-aws-profile"
   ```

3. Deploy the application using SAM CLI:
   ```
   sam build
   sam deploy
   ```

## Usage

Once deployed, you can invoke the Lambda function:

```bash
aws lambda invoke --function-name ListLambdaProvisionedReserver-ListFunction-XXXXXXXXXXXX output.txt
```

The function will output a list of Lambda functions with their provisioned or reserved concurrency settings to CloudWatch Logs. You can view these logs in the AWS Console or using the AWS CLI.

## IAM Permissions

The Lambda function requires the following permissions:
- `lambda:GetFunctionConcurrency`
- `lambda:ListFunctions`
- `lambda:ListProvisionedConcurrencyConfigs`

These permissions are automatically configured in the SAM template.

## Output Example

The function outputs information in the following format:

```
Total functions 123
1. Function Name: function-with-reserved, Reserved Concurrency: 10
2. Function Name: function-with-provisioned, Provisioned Concurrency: 5
```

## Customization

You can modify the region by updating the environment variable in the Lambda function or by setting the `AWS_REGION` environment variable.

## License

This project is licensed under the MIT-0 License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## References

- https://repost.aws/knowledge-center/lambda-provisioned-reserved-concurrency 