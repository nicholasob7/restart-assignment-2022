# Lab 179b

```
C:\Users\jabre\Downloads>ssh -i labsuser.pem ec2-user@54.212.33.34
The authenticity of host '54.212.33.34 (54.212.33.34)' can't be established.
ECDSA key fingerprint is SHA256:rYFip2LHwAjbzo5erRQf8RxSkI1BK2UTDXczlwXrKkQ.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '54.212.33.34' (ECDSA) to the list of known hosts.

       __|  __|_  )
       _|  (     /   Amazon Linux 2 AMI
      ___|\___|___|

https://aws.amazon.com/amazon-linux-2/
[ec2-user@ip-10-200-0-33 ~]$ aws ec2 describe-instances \
> --filters "Name=tag:Name,Values= CafeInstance" \
> --query "Reservations[*].Instances[*].[InstanceId,InstanceType,PublicDnsName,PublicIpAddress,Placement.AvailabilityZone,VpcId,SecurityGroups[*].GroupId]"
You must specify a region. You can also configure your region by running "aws configure".
[ec2-user@ip-10-200-0-33 ~]$ aws configure
AWS Access Key ID [None]: AKIA4RFZEPTHTVTB2UOK
AWS Secret Access Key [None]: JABLULzuZWVxZVxzZHg9H/fFyZU6n11ZL4QQlhvQ
Default region name [None]: us-west-2
Default output format [None]: json

```
```
[ec2-user@ip-10-200-0-33 ~]$ aws ec2 describe-instances \
> --filters "Name=tag:Name,Values= CafeInstance" \
> --query "Reservations[*].Instances[*].[InstanceId,InstanceType,PublicDnsName,PublicIpAddress,Placement.AvailabilityZone,VpcId,SecurityGroups[*].GroupId]"
[
    [
        [
            "i-0fbd49c0ce2eff2f2",
            "t3.small",
            "ec2-54-212-33-34.us-west-2.compute.amazonaws.com",
            "54.212.33.34",
            "us-west-2a",
            "vpc-08dcaaf9f03c29b24",
            [
                "sg-07b49e2dcbd7654b5"
            ]
        ]
    ]
]
```
CafeInstance Instance ID: "i-0fbd49c0ce2eff2f2"

CafeInstance Instance Type: t3.small

CafeInstance Public DNS Name: ec2-54-212-33-34.us-west-2.compute.amazonaws.com

http://ec2-54-212-33-34.us-west-2.compute.amazonaws.com/cafe

CafeInstance Public IP Address: 54.212.33.34

CafeInstance Availability Zone: us-west-2a

# Query Availability Zones via Region

```
[ec2-user@ip-10-200-0-33 ~]$ aws ec2 describe-availability-zones \
> --filters "Name=region-name,Values=us-west-2" \
> --query "AvailabilityZones[*].ZoneName"
[
    "us-west-2a",
    "us-west-2b",
    "us-west-2c",
    "us-west-2d"
]

```
CafeInstance VPC ID: "vpc-08dcaaf9f03c29b24"

# Query IPv4 CIDR Block using vpc -id
```
[ec2-user@ip-10-200-0-33 ~]$ aws ec2 describe-vpcs --vpc-ids vpc-08dcaaf9f03c29b24 \
> --filters "Name=tag:Name,Values= Cafe VPC" \
> --query "Vpcs[*].CidrBlock"
[
    "10.200.0.0/20"
]

```
# Query Subnet and Subnet CIDR Block using vpc-id
```
[ec2-user@ip-10-200-0-33 ~]$ aws ec2 describe-subnets \
> --filters "Name=vpc-id,Values=vpc-08dcaaf9f03c29b24" \
> --query "Subnets[*].[SubnetId,CidrBlock]"
[
    [
        "subnet-08fdef7a3bdcce1c1",
        "10.200.0.0/24"
    ]
]

```
# Create Private Subnet 1
```
[ec2-user@ip-10-200-0-33 ~]$ aws ec2 create-subnet \
> --vpc-id vpc-08dcaaf9f03c29b24 \
> --cidr-block 10.200.2.0/23 \
> --availability-zone us-west-2a
{
    "Subnet": {
        "MapPublicIpOnLaunch": false,
        "AvailabilityZoneId": "usw2-az1",
        "AvailableIpAddressCount": 507,
        "DefaultForAz": false,
        "SubnetArn": "arn:aws:ec2:us-west-2:861529210063:subnet/subnet-07c14e88bbbd05f47",
        "Ipv6CidrBlockAssociationSet": [],
        "VpcId": "vpc-08dcaaf9f03c29b24",
        "State": "available",
        "AvailabilityZone": "us-west-2a",
        "SubnetId": "subnet-07c14e88bbbd05f47",
        "OwnerId": "861529210063",
        "CidrBlock": "10.200.2.0/23",
        "AssignIpv6AddressOnCreation": false
    }
}

```
# Create Private Subnet 2
```
[ec2-user@ip-10-200-0-33 ~]$ aws ec2 create-subnet \
> --vpc-id vpc-08dcaaf9f03c29b24 \
> --cidr-block 10.200.10.0/23 \
> --availability-zone us-west-2a
{
    "Subnet": {
        "MapPublicIpOnLaunch": false,
        "AvailabilityZoneId": "usw2-az1",
        "AvailableIpAddressCount": 507,
        "DefaultForAz": false,
        "SubnetArn": "arn:aws:ec2:us-west-2:861529210063:subnet/subnet-0c0b9844029f6029a",
        "Ipv6CidrBlockAssociationSet": [],
        "VpcId": "vpc-08dcaaf9f03c29b24",
        "State": "available",
        "AvailabilityZone": "us-west-2a",
        "SubnetId": "subnet-0c0b9844029f6029a",
        "OwnerId": "861529210063",
        "CidrBlock": "10.200.10.0/23",
        "AssignIpv6AddressOnCreation": false
    }
}

```
aws ec2 create-subnet \
> --vpc-id vpc-08dcaaf9f03c29b24 \
> --cidr-block 10.200.9.0/23 \
> --availability-zone us-west-2b

aws rds create-db-subnet-group \
--db-subnet-group-name "CafeDB Subnet Group" \
--db-subnet-group-description "DB subnet group for Cafe" \
--subnet-ids subnet-07c14e88bbbd05f47 subnet-0c0b9844029f6029a \
--tags "Key=Name,Value= CafeDatabaseSubnetGroup"

CafeSecurityGroup Group ID: "sg-07b49e2dcbd7654b5"

# Create the CafeDatabaseSG security group.  
```
[ec2-user@ip-10-200-0-33 ~]$ aws ec2 create-security-group \
> --group-name CafeDatabaseSG \
> --description "Security group for Cafe database" \
> --vpc-id vpc-08dcaaf9f03c29b24
{
    "GroupId": "sg-012e7a15eac84fd85"
}
```
CafeDatabaseSG Group ID: "sg-012e7a15eac84fd85"
# Set inbound rule for Security group
```
[ec2-user@ip-10-200-0-33 ~]$ aws ec2 authorize-security-group-ingress \
> --group-id sg-012e7a15eac84fd85 \
> --protocol tcp --port 3306 \
> --source-group sg-07b49e2dcbd7654b5

```
# Check inbound rule is set properly
```
[ec2-user@ip-10-200-0-33 ~]$ aws ec2 describe-security-groups \
> --query "SecurityGroups[*].[GroupName,GroupId,IpPermissions]" \
> --filters "Name=group-name,Values='CafeDatabaseSG'"
[
    [
        "CafeDatabaseSG",
        "sg-012e7a15eac84fd85",
        [
            {
                "PrefixListIds": [],
                "FromPort": 3306,
                "IpRanges": [],
                "ToPort": 3306,
                "IpProtocol": "tcp",
                "UserIdGroupPairs": [
                    {
                        "UserId": "861529210063",
                        "GroupId": "sg-07b49e2dcbd7654b5"
                    }
                ],
                "Ipv6Ranges": []
            }
        ]
    ]
]
```
