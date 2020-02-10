import uuid

uniqueId = uuid.uuid4()

class uuidRestrained:
    def __init__(self):
         self = uuid.uuid4()
    
    def generateUUID4(self):
        return uuid.uuid4()

restrainedUUID = uuidRestrained()

uniqueId = restrainedUUID.generateUUID4()
