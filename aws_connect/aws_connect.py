# encoding=utf8
import boto3
# import sys
client = boto3.client('connect')

# 接收参数输入
# print(sys.argv[0])
# print(sys.argv[1])

def getGroupname(uids):
    response = client.list_security_profiles(
        InstanceId='5378479d-5ad9-4371-b18c-e3dbd8963a7d',
        MaxResults=123
    )
    securitys=response.get('SecurityProfileSummaryList')
    groupname=[]
    for y in securitys:
        for uid in uids:
            if y.get('Id')==uid:
                groupname.append(y.get('Name'))
                break
            else:
                continue
    return(groupname)

def listUser(group):
    response = client.list_users(
        InstanceId='5378479d-5ad9-4371-b18c-e3dbd8963a7d',
        MaxResults=123
    )
    # print (response)
    users=response.get('UserSummaryList')
    phones = []
    for y in users:
        responseD = client.describe_user(
            UserId=str(y.get('Id')),
            InstanceId='5378479d-5ad9-4371-b18c-e3dbd8963a7d'
        )
        userdetails=responseD.get('User')
        groupnames=getGroupname(userdetails.get('SecurityProfileIds'))
        for groupname in groupnames:
            if groupname==group:
                phones.append(userdetails.get('PhoneConfig').get('DeskPhoneNumber'))
                break
            else:
                continue
    print(phones)
    return phones

def callUser(phone,msg):
    response = client.start_outbound_voice_contact(
        DestinationPhoneNumber=phone,
        ContactFlowId='681f0eeb-f2ef-40a2-bcbd-aae124656282',
        InstanceId='5378479d-5ad9-4371-b18c-e3dbd8963a7d',
        QueueId='1afd0b18-0992-4a78-aae8-7d025ce6fcb3',
        Attributes={
            'btmxmessage': msg
        }
    )
    return response
    
if __name__ == '__main__':
    # 根据aws connect服务配置的用户安全组拿到phone信息，也可以在代码中自定义
    callgroup='mayday'
    phones=listUser(callgroup)
    # 自定义播报的信息，建议重复三遍以上
    message = 'webserver down;'
    messages=message*6
    # for phone in phones:
    #     callUser(phone, messages)