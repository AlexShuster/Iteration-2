import Train_Model_UI

class trackModelInputs:

    def __init__(self, authority, speedLimit, trackCircuitInput, passengerNumber, routeInformationSystem):
        self.authority = authority
        self.speedLimit = speedLimit
        self.trackCircuitInput = trackCircuitInput
        self.passengerNumber = passengerNumber
        self.routeInformationSystem = routeInformationSystem


class RouteInformationSystem:

    def __init__(self, blockPolarity, blockTravelDirection, grade, elevation, blockSize):
    
        self.blockPolarity = blockPolarity
        self.blockTravelDirection = blockTravelDirection
        self.grade = grade
        self.elevation = elevation
        #beaconData
        self.blockSize = blockSize


class trainControllerInputs:

    def __init__(self, speedCommand, brakeCommand_service, brakeCommand_emergency, temperature, doors_left, doors_right, lights, currentEnginePower):
        self.speedCommand = speedCommand
        self.brakeCommand_service = brakeCommand_service
        self.brakeCommand_emergency = brakeCommand_emergency
        self.temperature = temperature
        self.doors_left = doors_left
        self.doors_right = doors_right
        self.lights = lights
        self.currentEnginePower = currentEnginePower * 1000


class TrainModel:

    decelLimit_service = -1.2
    decelLimit_emergency = -2.73

    #Car weight (Need to caclculate based on number of passengers later)
    weight_empty = 40.9 #Tons
    mass = weight_empty * 907.185 #Kilograms

    #Acceleration Limit
    #Unsure where crew number comes from
    crewNumber = 3


class Engine:

    #Time step
    T = 1/10

    v_n = 90
    force = 0
    accel_n = 0
    currentSpeed = 0

    def EnginePower(self, window, currentEnginePower, brakeCommand_emergency, decelLimit_emergency, brakeCommand_service, decelLimit_service, mass, T, myStrings, myTrackModel, myTrainController, myRIS, myTrain, myLists):

        v_n_1 = self.v_n

        #if v = 0, and P = 0, don't make v > 0 ##big oof on this##
        if self.v_n == 0 and currentEnginePower == 0:
            self.force = 0
            self.accel_n = 0

        #if v = 0, and P > 0, make v > 0 ##big oof on this##
        elif self.v_n == 0 and currentEnginePower > 0:
            self.v_n = 0.01

        #when v > 0
        else:
            self.force = currentEnginePower / self.v_n #Newtons
            accel_n_1 = self.accel_n

            #When braking, engine is off and acceleration = brakes
            if brakeCommand_emergency > 0:
                self.accel_n = decelLimit_emergency/100
            elif brakeCommand_service > 0:
                self.accel_n = brakeCommand_service * decelLimit_service/100
            else:            
                self.accel_n = self.force / mass
            self.v_n = v_n_1 + (T/2) * (self.accel_n + accel_n_1)
        self.currentSpeed = self.v_n * 2.23694 #m/s -> mph
                
        window.after(1000, self.enginePowerFactory(window, currentEnginePower, brakeCommand_emergency, decelLimit_emergency, brakeCommand_service, decelLimit_service, mass, T, myStrings, myTrackModel, myTrainController, myRIS, myTrain, myLists))

    def enginePowerFactory(self, window, currentEnginePower, brakeCommand_emergency, decelLimit_emergency, brakeCommand_service, decelLimit_service, mass, T, myStrings, myTrackModel, myTrainController, myRIS, myTrain, myLists):
        def f(*_):
            self.EnginePower(window, currentEnginePower, brakeCommand_emergency, decelLimit_emergency, brakeCommand_service, decelLimit_service, mass, T, myStrings, myTrackModel, myTrainController, myRIS, myTrain, myLists)
        return f
