import SwiftUI

struct ContentView: View {
    // Create instances of the subprogram classes
    let lakeshore = LakeShoreController("GPIB::1")
    let keithley = KeithleyController("GPIB::12")
    let ips = IPS120Controller("GPIB::25")

    // Create state variables for user input
    @State var tempSetpoint: String = ""
    @State var currentSetpoint: String = ""
    @State var fieldSetpoint: String = ""

    // Create state variables for displaying the temperature, current, and magnetic field
    @State var temperature: String = ""
    @State var current: String = ""
    @State var magneticField: String = ""

    // Create line series for magnetic field vs resistance and current vs voltage
    let series1 = LineSeries(points: [])
    let series2 = LineSeries(points: [])

    // Define the view
    var body: some View {
        VStack {
            // Create labels and text fields for user input
            HStack {
                Text("Temperature Setpoint (K):")
                TextField("Enter temperature setpoint", text: $tempSetpoint)
                    .textFieldStyle(RoundedBorderTextFieldStyle())
            }
            HStack {
                Text("Current Setpoint (A):")
                TextField("Enter current setpoint", text: $currentSetpoint)
                    .textFieldStyle(RoundedBorderTextFieldStyle())
            }
            HStack {
                Text("Magnetic Field Setpoint (T):")
                TextField("Enter magnetic field setpoint", text: $fieldSetpoint)
                    .textFieldStyle(RoundedBorderTextFieldStyle())
            }

            // Create buttons for each subprogram
            Button("Measure Temperature") {
                // Get the temperature setpoint from the text field
                let tempSetpoint = Double(tempSetpoint) ?? 0.0
                // Call the measure_temperature method of the LakeShoreController
                let temp = lakeshore.measure_temperature(tempSetpoint)
                // Display the temperature in the GUI
                temperature = "Temperature: \(temp) K"
            }
            .padding()
            .foregroundColor(.white)
            .background(Color.blue)
            .cornerRadius(10)

            Button("Measure Current") {
                // Get the current setpoint from the text field
                let currentSetpoint = Double(currentSetpoint) ?? 0.0
                // Call the measure_current method of the KeithleyController
                let current = keithley.measure_current(currentSetpoint)
                // Display the current in the GUI
                self.current = "Current: \(current) A"
            }
            .padding()
            .foregroundColor(.white)
            .background(Color.blue)
            .cornerRadius(10)

            Button("Set Magnetic Field") {
                // Get the magnetic field setpoint from the text field
                let fieldSetpoint = Double(fieldSetpoint) ?? 0.0
                // Call the set_magnetic_field method of the IPS120Controller
                ips.set_magnetic_field(fieldSetpoint)
                // Display the current magnetic field in the GUI
                magneticField = "Magnetic Field: \(fieldSetpoint) T"
            }
            .padding()
            .foregroundColor(.white)
            .background(Color.blue)
            .cornerRadius(10)

            Button("Curve Fitting") {
                // TODO: Implement curve fitting
            }
            .padding()
            .foregroundColor(.white)
            .background(Color.blue)
            .cornerRadius(10)

            Button("Convert Data") {
                // TODO: Implement data conversion
            }
            .padding()
            .foregroundColor(.white
