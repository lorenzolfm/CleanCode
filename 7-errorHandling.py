def sendShutdown():
    handle = getHandle(device)

    if handle != DeviceHandle.INVALID:
        record = retrieveDeviceRecord(handle)
        if record.getStatus() != "Device Suspended":
            pauseDevice(handle)
            clearDeviceWorkQueue(handle)
            closeDevice(handle)
        else:
            print("Unable to shutdown")
    else:
        print(f"Invalid handle for: {device}")

#vs

def sendShutdown():
    try:
        tryToShutdown()
    except IndexError as e:
        print(e)

def tryToShutdown():
    handle = getHandle(device)
    record = retrieveDeviceRecord(handle)

    pauseDevice(handle)
    clearDeviceWorkQueue(handle)
    closeDevice(handle)

def getHandle(id):
    raise IndexError(f"Invalid handle for: {id}")

#  #====================================================

def tryExceptFinallyBlock():
    try:
        #Tenta executar o código desse bloco
    except EOFError:
        #Caso falhe, executa esse bloco
    finally:
        #Sempre vai executar isso

#====================================================

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Ops. Algo deu Errado")

#vs

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print(f"Você está tentando dividir {a} por 0. Isso é não é possível! Entre com outro valor para b")


#====================================================

def getTotal(dinnerAccount):
    try:
       serviceFee = dinnerAccount.total * 0.05
       total = dinnerAccount.total + serviceFee 
       return total 
    except TypeError:
        return 0

i#vs

class dinnerAccount:
    def __init__(self):
        self.total = 0
        self.serviceFee = total * 0.05

def getTotal(dinnerAcc):
    total = dinnerAcc.total + dinnerAcc.serviceFee
    return total
    

#====================================================

class Employees:
    def __init__(self):
        self.employees = None

def paychecksTotal(employees):
    if employees != null:
        total = 0
        for employee in employees:
            total += employee.salary
        return total

#vs

class Employees:
    def __init__(self):
        self.employees = []

def paychecksTotal(employees):
    total = 0
    for employee in employees:
        total += employee.salary
    return total

#====================================================

def xProjection(a,b):
    if (a or b) == 0:
        raise ValueError("a ou b não pode ser zero")
    else:
        return (a - b)*1.5

def xProjection(a,b):
    assert a != 0, "a não pode ser zero"
    assert b != 0, "b não pode ser zero"
    return (a - b)*1.5


