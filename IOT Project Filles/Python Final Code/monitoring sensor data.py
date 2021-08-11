import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "jmhx1u",
        "typeId": "SmartDevice",
        "deviceId":"2468"
    },
    "auth": {
        "token": "246810xd"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    btp=round(random.uniform(95.0,102.0), 1)
    plr=random.randint(40,120)
    sbp=random.randint(60,150)
    dbp=random.randint(40,100)
    myData={'body_temperature':btp, 'pulse_rate':plr, 'systolic_blood_pressure':sbp, 'diastolic_blood_pressure':dbp}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
