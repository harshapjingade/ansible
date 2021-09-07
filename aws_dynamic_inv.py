#!/bin/python3
import json
import sys
try:
    import boto3
except Exception as e:
    print(e)
    print("Please rectify above exception and then try again")
    sys.exit(1)

def get_hosts(ec2_ob,fv):
    f={"Name":"tag:Env", "Value": [fv]}
    hosts=[]
    for each_in in ec2_ob.inctances.filter(Filters=[f]):
        hosts.append(each_in.private_ip_address)
    return hosts

def main():
    ec2_ob=boto3.resource("ec2","us-east-1")
    db_group=get_hosts(ec2_ob,'db')
    app_group=get_hosts(ec2_ob,'app')
    all_groups={'db': db_group, 'app': app_group}
    print(json.dumps(all_groups))
    return None

if __name__=="__main__":
    main()