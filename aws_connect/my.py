fanzhiweideMacBook-Pro:~ fzw$ cd DATA/OPSTools/
fanzhiweideMacBook-Pro:OPSTools fzw$ ls
AWS        Archive    Remote     cert.pem   public.pem
Aliyun     Jenkins    XMLDeal    launcher   venv
fanzhiweideMacBook-Pro:OPSTools fzw$ cd AWS
fanzhiweideMacBook-Pro:AWS fzw$ ls
aws_connect.py
fanzhiweideMacBook-Pro:AWS fzw$ vim aws_connect.py
































1 # encoding=utf8
2 import boto3
3 # import sys
4 client = boto3.client('connect')
5
6 # 接收参数输入
7 # print(sys.argv[0])
8 # print(sys.argv[1])
9
10 def getGroupname(uids):
    11     response = client.list_security_profiles(
        12         InstanceId='5378479d-5ad9-4371-b18c-e3dbd8963a7d',
                              13         MaxResults=123
    14     )
    15     securitys=response.get('SecurityProfileSummaryList')
    16     groupname=[]
    17     for y in securitys:
        18         for uid in uids:
        19             if y.get('Id')==uid:
        20                 groupname.append(y.get('Name'))
    21                 break
    22             else:
    23                 continue
    24     return(groupname)
    25
    26 def listUser(group):
        27     response = client.list_users(
        28         InstanceId='5378479d-5ad9-4371-b18c-e3dbd8963a7d',
                              29         MaxResults=123
    30     )
    31     # print (response)
    32     users=response.get('UserSummaryList')
    33     phones = []
    34     for y in users:
        35         responseD = client.describe_user(
        36             UserId=str(y.get('Id')),
                              37             InstanceId='5378479d-5ad9-4371-b18c-e3dbd8963a7d'
    38         )
