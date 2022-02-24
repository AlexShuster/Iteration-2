import Train_Model
import Train_Model_UI

myStrings = Train_Model_UI.TrainModelStrings()

myEngine = Train_Model.Engine()

myTrain = Train_Model.TrainModel()

myRIS = Train_Model.RouteInformationSystem(1, 1, 0.5, 0.5, 100)

myTrackModel = Train_Model.trackModelInputs(77, 45, 1, 20, myRIS)

myTrainController = Train_Model.trainControllerInputs(45, 0, 100, 69, 0, 0, 0, 300)

myStrings.makeStrings(myTrackModel.authority, myTrainController.temperature, myTrainController.lights, myTrainController.speedCommand, myTrainController.brakeCommand_service, myTrainController.brakeCommand_emergency, myTrainController.doors_left, myTrainController.doors_right, myEngine.currentSpeed, myTrainController.currentEnginePower, myRIS.blockTravelDirection, myTrackModel.speedLimit, myRIS.grade, myRIS.elevation, myRIS.blockSize, myTrackModel.trackCircuitInput)

myLists = Train_Model_UI.DataLists()

myWindow = Train_Model_UI.makeWindow(myLists)

myLists.listTrainStatistics(myStrings.authority_list, myStrings.decelLimit_service_str, myStrings.decelLimit_emergency_str, myStrings.dimensions, myStrings.maxEnginePower)
myLists.listEssentialCarFunctions(myStrings.speedCommand_list, myStrings.serviceBrake_list, myStrings.eBrake_list, myStrings.doors_left_str, myStrings.doors_right_str, myStrings.trackCircuitInput_str, myStrings.currentSpeed_list, myStrings.currentEnginePower_list)
myLists.listNonEssentialCarDetails(myStrings.temperature_list, myStrings.lights_str, myTrain.crewNumber, myTrackModel.passengerNumber)
myLists.listTrackData(myRIS.blockPolarity, myStrings.blockTravelDirection_str, myStrings.speedLimit_list, myStrings.grade_list, myStrings.elevation_list, myStrings.blockSize_list, myStrings.trackCircuitInput_str)



myEngine.EnginePower(myWindow.window, myTrainController.currentEnginePower, myTrainController.brakeCommand_emergency, myTrain.decelLimit_emergency, myTrainController.brakeCommand_service, myTrain.decelLimit_service, myTrain.mass, myEngine.T, myStrings, myTrackModel, myTrainController, myRIS, myTrain, myLists)

myWindow.makeGUI(myStrings, myTrackModel, myTrainController, myTrain, myRIS, myEngine)

myWindow.window.mainloop()




