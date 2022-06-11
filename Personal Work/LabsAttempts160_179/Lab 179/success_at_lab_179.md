# lab 179 aws query

CafeInstance Instance ID: "i-0f424212ef48f1a1c"

CafeInstance Instance Type: t3.small

CafeInstance Public DNS Name: "ec2-54-200-214-183.us-west-2.compute.amazonaws.com"

http://ec2-54-200-214-183.us-west-2.compute.amazonaws.com/cafe

CafeInstance Public IP Address: "54.200.214.183"

CafeInstance Availability Zone: us-west-2a

CafeInstance VPC ID: "vpc-065e843ca26341529"

CafeSecurityGroup Group ID: "sg-03d7c5c918cb54ab5"

CafeDatabaseSG Group ID:"sg-09b818f7317744753"

Cafe VPC IPv4 CIDR block: 10.200.0.0/20

Cafe Public Subnet 1 Subnet ID: subnet-0c8986fe4fe697985
Cafe Public Subnet 1 IPv4 CIDR block: 10.200.0.0/24

Cafe Private Subnet 1 ID: "subnet-08dabb47b3b11bbab"
Cafe Private Subnet 2 ID: "subnet-03e25e58367f2a294"

List of Availability Zones in the region: us-west-2a, us-west-2b, us-west-2c, us-west-2d

RDS Instance Database Endpoint Address: "cafedbinstance.ctfiwhpsvvaj.us-west-2.rds.amazonaws.com"

Number of orders:  1

mysql --user=root --password='Re:Start!9' \
--host=cafedbinstance.ctfiwhpsvvaj.us-west-2.rds.amazonaws.com \
cafe_db

mysql --user=root --password='Re:Start!9' \
--host=cafedbinstance.ctfiwhpsvvaj.us-west-2.rds.amazonaws.com \
< cafedb-backup.sql

aws rds create-db-instance \
--db-instance-identifier CafeDBInstance \
--engine mariadb \
--engine-version 10.5.13 \
--db-instance-class db.t3.micro \
--allocated-storage 20 \
--availability-zone us-west-2a \
--db-subnet-group-name "CafeDB Subnet Group" \
--vpc-security-group-ids "sg-09b818f7317744753" \
--no-publicly-accessible \
--master-username root --master-user-password 'Re:Start!9'



```
aws ec2 describe-vpcs --vpc-ids vpc-065e843ca26341529 \
--filters "Name=tag:Name,Values= Cafe VPC" \
--query "Vpcs[*].CidrBlock"
```

aws ec2 describe-subnets \
--filters "Name=vpc-id,Values=vpc-065e843ca26341529" \
--query "Subnets[*].[SubnetId,CidrBlock]"

aws ec2 describe-availability-zones \
--filters "Name=region-name,Values=us-west-2" \
--query "AvailabilityZones[*].ZoneName"

http://ec2-54-200-214-183.us-west-2.compute.amazonaws.com/cafe

Order History

Order Number: 1     Date: 2022-06-05     Time: 22:05:25     Total Amount: $36.00

Item	Price	Quantity	Amount
Croissant	$1.50	2	$3.00
Donut	$1.00	2	$2.00
Chocolate Chip Cookie	$2.50	2	$5.00
Muffin	$3.00	2	$6.00
Strawberry Blueberry Tart	$3.50	2	$7.00
Strawberry Tart	$3.50	2	$7.00
Coffee	$3.00	2	$6.00

aws ec2 create-security-group \
--group-name CafeDatabaseSG \
--description "Security group for Cafe database" \
--vpc-id vpc-065e843ca26341529

aws ec2 authorize-security-group-ingress \
--group-id sg-09b818f7317744753 \
--protocol tcp --port 3306 \
--source-group sg-03d7c5c918cb54ab5

aws ec2 create-subnet \
--vpc-id vpc-065e843ca26341529 \
--cidr-block 10.200.2.0/23 \
--availability-zone us-west-2a

aws ec2 create-subnet \
--vpc-id vpc-065e843ca26341529 \
--cidr-block 10.200.10.0/23 \
--availability-zone us-west-2b

aws rds create-db-subnet-group \
--db-subnet-group-name "CafeDB Subnet Group" \
--db-subnet-group-description "DB subnet group for Cafe" \
--subnet-ids "subnet-08dabb47b3b11bbab" "subnet-03e25e58367f2a294" \
--tags "Key=Name,Value= CafeDatabaseSubnetGroup"

    "DBSubnetGroup": {
        "Subnets": [
            {
                "SubnetStatus": "Active",
                "SubnetIdentifier": "subnet-08dabb47b3b11bbab",
                "SubnetOutpost": {},
                "SubnetAvailabilityZone": {
                    "Name": "us-west-2a"
                }
            },
            {
                "SubnetStatus": "Active",
                "SubnetIdentifier": "subnet-03e25e58367f2a294",
                "SubnetOutpost": {},
                "SubnetAvailabilityZone": {
                    "Name": "us-west-2b"
                }
            }
        ],
        "VpcId": "vpc-065e843ca26341529",
        "DBSubnetGroupDescription": "DB subnet group for Cafe",
        "SubnetGroupStatus": "Complete",
        "DBSubnetGroupArn": "arn:aws:rds:us-west-2:861529210063:subgrp:cafedb subnet group",
        "DBSubnetGroupName": "cafedb subnet group"

