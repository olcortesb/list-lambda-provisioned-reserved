import os
import boto3

def lambda_handler(event, context):
    # Select the region you would like to list function concurrency
    # The default region is the deployment region
    region = os.environ['AWS_REGION']

    lambda_client = boto3.client('lambda', region_name=region)
    count = 0

    # Create a paginator for the 'list_functions' operation.
    paginator = lambda_client.get_paginator('list_functions')
    lambda_iterator = paginator.paginate()

    total_functions = 0

    for page in paginator.paginate():
        # Sumar la cantidad de funciones en la página actual
        total_functions += len(page['Functions'])
    
    print(f" Total functions {total_functions}")

    # For loop to iterate through listed functions and return function name and concurrency response
    for items in lambda_iterator:

        for function in items['Functions']:
            function_name = function['FunctionName']

            try:
                response = lambda_client.get_function_concurrency(
                    FunctionName=function_name
                )

                # If reserved concurrency is configured, print the details
                if 'ReservedConcurrentExecutions' in response:
                    count += 1
                    reserved_concurrency = response['ReservedConcurrentExecutions']
                    print(f"{count}. Function Name: {function_name}, Reserved Concurrency: {reserved_concurrency}")  

            except lambda_client.exceptions.ResourceNotFoundException:
                # If the function is not found, skip it
                pass
            except Exception as e:
                print(f"Error retrieving concurrency for {function_name}: {e}")

            try:
                response = lambda_client.list_provisioned_concurrency_configs(
                    FunctionName=function_name
                )

                # If provisioned concurrency is configured, print the details
                if 'ProvisionedConcurrencyConfigs' in response and response['ProvisionedConcurrencyConfigs']:
                    provisioned_concurrency = response['ProvisionedConcurrencyConfigs'][0]['RequestedProvisionedConcurrentExecutions']
                    count += 1
                    print(f"{count}. Function Name: {function_name}, Provisioned Concurrency: {provisioned_concurrency}")

            except lambda_client.exceptions.ResourceNotFoundException:
                # If the function is not found, skip it
                pass
            except Exception as e:
                print(f"Error retrieving provisioned concurrency for {function_name}: {e}")