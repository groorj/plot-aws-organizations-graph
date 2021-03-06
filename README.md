# Plot AWS Organizations Graph

## Table of Contents
- [What does it do ?](https://github.com/groorj/aws-ip-range-api#what-does-it-do)
- [This project uses](https://github.com/groorj/aws-ip-range-api#this-project-uses)
- [Get started](https://github.com/groorj/aws-ip-range-api#get-started)
- [Notes](https://github.com/groorj/aws-ip-range-api#notes)

## What does it do

This Python script will generate a graph with the member accounts of your AWS Organization.

## This project uses

- Python3
- [Graphviz](https://graphviz.readthedocs.io/en/stable/)
- [AWS cli](https://aws.amazon.com/cli/)

## Where does the information comes from

The information that will be used to generate a graph like the example below, will be generated by using the AWS cli.

![AWS Organizations graph example](/aws-map-my-organization-example.png)


## Get started

- [Install AWS Cli](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- Install Graphviz

```bash
pip3 install pygraphviz
```

## How to use it

### Generate a file with dummy data for testing
```bash
python3 generate_output.py > output.json
```

**Result example:**
```json
{
    "Accounts": [

        {
            "Id": "000000000001",
            "Arn": "arn:aws:organizations::999999999999:account/o-0rgan1zat1/000000000001",
            "Email": "account-000000000001@example.com",
            "Name": "Account 000000000001",
            "Status": "ACTIVE",
            "JoinedMethod": "CREATED",
            "JoinedTimestamp": "2019-11-18T19:27:04.322000-05:00"
        },
...
        {
            "Id": "000000000008",
            "Arn": "arn:aws:organizations::999999999999:account/o-0rgan1zat1/000000000008",
            "Email": "account-000000000008@example.com",
            "Name": "Account 000000000008",
            "Status": "ACTIVE",
            "JoinedMethod": "CREATED",
            "JoinedTimestamp": "2009-07-15T04:37:15.196000-04:00"
        }
    ]
}
```
*You can find an output example file [here](output.json-example).*

### Plot an AWS Organizations Graph based on the dummy file you have created
```bash
python3 organizations.py
```

### Get your AWS Organizations information and save to a file

You will need read access to your Root account in order to gather the required information.

```bash
aws organizations list-accounts --output json > output.json
```

**Result example:**
```json
{
    "Accounts": [

        {
            "Id": "100000000001",
            "Arn": "arn:aws:organizations::999999999999:account/o-0rgan1zat1/000000000001",
            "Email": "myawsaccount1@gmail.com",
            "Name": "Account 100000000001",
            "Status": "ACTIVE",
            "JoinedMethod": "CREATED",
            "JoinedTimestamp": "2019-01-29T12:32:01.150000-05:00"
        },
        {
            "Id": "100001000000",
            "Arn": "arn:aws:organizations::999999999999:account/o-0rgan1zat1/100001000000",
            "Email": "my-aws-account2@yahoo.com",
            "Name": "Account 100001000000",
            "Status": "ACTIVE",
            "JoinedMethod": "CREATED",
            "JoinedTimestamp": "2020-03-18T11:06:05.432000-04:00"
        }
    ]
}
```

### Plot an AWS Organizations Graph based on your Organization information
```bash
python3 organizations.py
```

## Files
```
.
????????? LICENSE -> This project's license
????????? README.md -> This file
????????? aws-map-my-organization-example.png -> An example image of the result
????????? generate_output.py -> This file generates random dummy data so you can test it
????????? my-org.gv -> File containing Graphviz information that will be generated
????????? my-org.gv.pdf -> This is the graph result file that will be generated with the data you provide
????????? organizations.py -> Python script that plots the graph
????????? output.json -> This is the source data file that will be used by 'organizations.py'
????????? output.json-example -> Provided data example file that you can use by renaming it to 'output.json' and running 'organizations.py'
```


## Clean up
No AWS resources will be created so no clean up is needed.


## Notes
Make sure you have read access to your AWS Root account so you can generate your AWS Organizations output.json file.