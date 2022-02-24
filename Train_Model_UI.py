from tkinter import *


class TrainModelStrings:

    #Train Statistics Strings
    authority_list = ""
    accelLimit = "1.64 ft/s²"
    decelLimit_service_str = "3.94 ft/s²"
    decelLimit_emergency_str = "8.96 ft/s²"
    dimensions = "105.6 ft x 8.69 ft x 11.22 ft"
    maxEnginePower = "360 kW"

    #Non-Essential Car Details Strings
    temperature_list = ""
    lights_str = ""

    #Essential Car Functions Strings
    speedCommand_list = ""
    serviceBrake_list = ""
    eBrake_list = ""
    doors_left_str = ""
    doors_right_str = ""
    currentSpeed_list = ""
    currentEnginePower_list = ""

    #Track Data Strings
    blockTravelDirection_str = ""
    speedLimit_list = ""
    grade_list = ""
    elevation_list = ""
    blockSize_list = ""
    trackCircuitInput_str = ""

    def makeStrings(self, authority, temperature, lights, speedCommand, brakeCommand_service, brakeCommand_emergency, doors_left, doors_right, currentSpeed, currentEnginePower, blockTravelDirection, speedLimit, grade, elevation, blockSize, trackCircuitInput):

        #################
        #String Creation#
        #################

        #Train Statistics Strings
        self.authority_list = str(authority) + " blocks"

        #Non-Essential Car Details Strings
        self.temperature_list = str(temperature) + "° Fahrenheit"

        if lights == 1:
            self.lights_str = "On"
        else:
            self.lights_str = "Off"

        #Essential Car Functions Strings
        self.speedCommand_list = str(speedCommand) + " mph"
        self.serviceBrake_list = str(brakeCommand_service) + "%"
        self.eBrake_list = str(brakeCommand_emergency) + "%"

        if doors_left == 1:
            self.doors_left_str = "Open"
        else:
            self.doors_left_str = "Closed"

        if doors_right == 1:
            self.doors_right_str = "Open"
        else:
            self.doors_right_str = "Closed"

        self.currentSpeed_list = str(currentSpeed) + " mph"
        self.currentEnginePower_list = str(currentEnginePower) + " W"

        #Track Data Strings
        if blockTravelDirection == 1:
            self.blockTravelDirection_str = "Forward"
        else:
            self.blockTravelDirection_str = "Backward"

        self.speedLimit_list = str(speedLimit) + " mph"
        self.grade_list = str(grade) + "%"
        self.elevation_list = str(elevation) + " ft"
        self.blockSize_list = str(blockSize) + " miles"

        if trackCircuitInput == 1:
            self.trackCircuitInput_str = "Block Unoccupied"
        else:
            self.trackCircuitInput_str = "BLOCK OCCUPIED"


class DataLists:
    trainStatistics = []
    nonEssentialCarDetails = []
    essentialCarFunctions = []
    trackData = []

    def listTrainStatistics(self, authority_list, decelLimit_service, decelLimit_emergency, dimensions, maxEnginePower):

        self.trainStatistics = [("Authority", "Deceleration Limit (Service Brake)", "Deceleration Limit (Emergency Brake)", "Train Dimensions", "Max Engine Power"), (authority_list, decelLimit_service, decelLimit_emergency, dimensions, maxEnginePower)]
    
    def listNonEssentialCarDetails(self, temperature_list, lights, crewNumber, passengerNumber):

        self.nonEssentialCarDetails = [("Temperature", "Cabin Lights", "Headlights", "Crew Number", "Passenger Number"), (temperature_list, lights, crewNumber, passengerNumber)]
    
    def listEssentialCarFunctions(self, speedCommand_list, serviceBrake_list, eBrake_list, doors_left, doors_right, trackSignal, currentSpeed_list, currentEnginePower_list):
        self.essentialCarFunctions = [("Commanded Speed", "Service Brake", "Emergency Brake", "Left Doors", "Right Doors", "Track Signal", "Current Speed", "Current Engine Power"), (speedCommand_list, serviceBrake_list, eBrake_list, doors_left, doors_right, trackSignal, currentSpeed_list, currentEnginePower_list)]
    
    def listTrackData(self, blockPolarity, blockTravelDirection, speedLimit_list, grade_list, elevation_list, blockSize_list, trackCircuitInput):
        self.trackData = [("Block Polarity", "Block Travel Direction", "Speed Limit", "Grade", "Elevation", "Station Position", "Block Size", "Track Circuit"), (blockPolarity, blockTravelDirection, speedLimit_list, grade_list, elevation_list, blockSize_list, trackCircuitInput)]


class makeWindow:

    window = Tk()

    def __init__(self, myDataList):
        self.myDataList = myDataList
        self.essentialCarFunctionsSvars = {}

    def update(self, myStrings, myTrackModel, myTrainController, myTrain, myRIS, myEngine):
            
            myStrings.makeStrings(myTrackModel.authority, myTrainController.temperature, myTrainController.lights, myTrainController.speedCommand, myTrainController.brakeCommand_service, myTrainController.brakeCommand_emergency, myTrainController.doors_left, myTrainController.doors_right, myEngine.currentSpeed, myTrainController.currentEnginePower, myRIS.blockTravelDirection, myTrackModel.speedLimit, myRIS.grade, myRIS.elevation, myRIS.blockSize, myTrackModel.trackCircuitInput)

            self.myDataList.listTrainStatistics(myStrings.authority_list, myStrings.decelLimit_service_str, myStrings.decelLimit_emergency_str, myStrings.dimensions, myStrings.maxEnginePower)
            
            self.myDataList.listEssentialCarFunctions(myStrings.speedCommand_list,
                                                        myStrings.serviceBrake_list,
                                                        myStrings.eBrake_list, myStrings.doors_left_str,
                                                        myStrings.doors_right_str,
                                                        myStrings.trackCircuitInput_str,
                                                        myStrings.currentSpeed_list, 
                                                        myStrings.currentEnginePower_list)

            self.myDataList.listNonEssentialCarDetails(myStrings.temperature_list, myStrings.lights_str, myTrain.crewNumber, myTrackModel.passengerNumber)
            self.myDataList.listTrackData(myRIS.blockPolarity, myStrings.blockTravelDirection_str, myStrings.speedLimit_list, myStrings.grade_list, myStrings.elevation_list, myStrings.blockSize_list, myStrings.trackCircuitInput_str) 
            
            for i in range (8):
                if i in self.essentialCarFunctionsSvars.keys():
                    self.essentialCarFunctionsSvars[i].set(self.myDataList.essentialCarFunctions[1][i])

            self.window.after(1000, self.updateFactory(myStrings, myTrackModel, myTrainController, myTrain, myRIS, myEngine))


    def makeGUI(self, myStrings, myTrackModel, myTrainController, myTrain, myRIS, myEngine):

        self.update(myStrings, myTrackModel, myTrainController, myTrain, myRIS, myEngine)

        self.window.title("Port Authority of Allegheny")
        TrainStatistics_label = Label(self.window, text = "Train Statistics", font = 16) .grid(row = 0, column = 0, sticky = W)
        for i in range (5):
            for j in range (2):
                table = Entry(self.window, width = 40)
                table.grid(row = i + 1, column = j)
                table.insert(END, self.myDataList.trainStatistics[j][i])   

        nonEssentialCarDetails_label = Label(self.window, text = "Non-Essential Car Details", font = 16) .grid(row = 9, column = 0, pady = (20, 0), sticky = W)
        for i in range (4):
            for j in range (2):
                table = Entry(self.window, width = 40)
                table.grid(row = i + 10, column = j)
                table.insert(END, self.myDataList.nonEssentialCarDetails[j][i])

        essentialCarFunctions_label = Label(self.window, text = "Essential Car Functions", font = 16) .grid(row = 0, column = 2, padx = (20, 0), sticky = W)
        for i in range (8):
            table = Entry(self.window, width = 40)
            table.grid(row = i + 1, column = 2, padx = (20, 0))
            table.insert(END, self.myDataList.essentialCarFunctions[0][i])
        
        for i in range (8):
            self.essentialCarFunctionsSvars[i] = StringVar(value="temp")
            table = Entry(self.window, width = 40, textvariable=self.essentialCarFunctionsSvars[i])
            table.grid(row = i + 1, column = 3)
            

        trackData_label = Label(self.window, text = "Track Data", font = 16) .grid(row = 9, column = 2, padx = (20, 0), pady = (20, 0), sticky = W)
        for i in range (7):
            table = Entry(self.window, width = 40)
            table.grid(row = i + 10, column = 2, padx = (20, 0))
            table.insert(END, self.myDataList.trackData[0][i])
        for i in range (7):
            table = Entry(self.window, width = 40)
            table.grid(row = i + 10, column = 3)
            table.insert(END, self.myDataList.trackData[1][i])

        self.update(myStrings, myTrackModel, myTrainController, myTrain, myRIS, myEngine)

        self.window.after(1000, self.updateFactory(myStrings, myTrackModel, myTrainController, myTrain, myRIS, myEngine))

    def updateFactory(self, myStrings, myTrackModel, myTrainController, myTrain, myRIS, myEngine):
        def f(*_):
            self.update(myStrings, myTrackModel, myTrainController, myTrain, myRIS, myEngine)
        return f

        
        
            