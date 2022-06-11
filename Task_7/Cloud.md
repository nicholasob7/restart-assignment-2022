# Task 7 - Linux/Cloud - 16 Marks

Set up a 2nd EC2 instance and install the Python httpie library on it.
Using the http command it installed, query one of the routes your API provides.
In the Cloud.md file in your GitHub repository add the following details.

# a. 
The hardware architecture your server uses (e.g. 64-bit x86, 64-bit ARM). [1 mark]

```
"x86_64"
```
# b. 
The Amazon Machine Image (AMI) ID (e.g. ami-052432ead9b0a1234) used. [1 mark]

```
"ami-00af37d1144686454"
```
# c. 
The EC2 instance type (e.g. t3.xlarge) you’re using. [1 mark]

```
"t3.micro"
```
# d. 
The number of vCPUs your instance has. [1 mark]

```
My instance has t3.micro with 2vCPU split between Command Host and Processor from managing storage lab.
So each instance has 1 cpu each with two threadspercore.
```
From the Command Host instance
```
"VirtualizationType": "hvm",
                    "CpuOptions": {
                        "CoreCount": 1,
                        "ThreadsPerCore": 2
```
# e. 
The amount of RAM/memory (GB) your instance has. [1 mark]

```
1 GiB
```
# f. 
The storage size (GB) your instance has. [1 mark]

```
Two volumes of 8GiB each.
```
# g. 
Your VPC network id (e.g. vpc-0784bdc0c0866c695). [1 mark]

```
"vpc-0c27e8f4a56d20f1d"
```
# h. 
Your Public/Elastic IP address (your server’s IP address). [1 mark]

```
"35.88.180.180"
```
# i. 
The Private IP address of your server (begins with 10.0.). [1 mark]

```
"10.5.0.49"
```
# j. 
The Network Address of the subnet your server is using (Hint: Run ip addr). [1 mark]

```
inet 10.5.0.49/24
```
# k. 
The Broadcast Address of the subnet your server is using. [1 mark]

```
brd 10.5.0.255
```
# l. 
The Default Gateway Address configured for your server. (Hint: Run ip route). [1 mark]

```
"default via 10.5.0.1 dev eth0"  
dga is 10.5.0.1

```

# m. 
incomplete

# n.
incomplete


