package ua.edu.chnu.kkn.solid_violation.lsp;

public class FillingStation {

    public void refuel(Vehicle vehicle) {
        if (vehicle instanceof PetrolCar) {
            vehicle.fillUpWithFuel();
        }
    }

    public void charge(Vehicle vehicle) {
        if (vehicle instanceof ElectricCar) {
            vehicle.chargeBattery();
        }
    }
}
