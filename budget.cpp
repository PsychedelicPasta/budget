#include <iostream>
#include <string>
using namespace std;

struct monthBudget{
    //Spending
    float rent; //House
    float carInsurance; //Car
    float electricity; //House
    float otherUtilities; //House
    float wiFi; //House
    float groceries; // House
    float foodEntertainment; //Personal
    float funEntertainment; //Personal
    float gas; //Car
    float debt; //Personal
    float phone; //Personal
    float gym; //Personal
    float emma;
    float savings;
    float income;

    void setIncome(){
        cout << "How much money do you have this month? ";
            cin >> income;
        cout << "What percentage of that would you like to save? (ENTER AS DECIMAL) ";
            cin >> savings;
        cout << endl;
    }

    float setVehicleExpenses(){
        carInsurance = 120.00;

        float milesDrive = (5 * 60) + (2 * 50);
        float mpg = 33.0;
        float gallons = milesDrive / mpg;
        gas = 4 * (gallons * 3.00);

        float totalVehical = carInsurance + gas;
        return totalVehical;
    }

    float setHousingExenses(){ //ANOTHER IDEA: set everything but rent and calculate rent at the end relative to everything else
        electricity = 100.00; //100
        wiFi = 60.00; //60
        otherUtilities = 50.00; //50
        groceries = 500; //Split-ish? //400
        float totalHousing = electricity + wiFi + otherUtilities + groceries;
        return totalHousing;
    }

    float setPersonalExpenses(){
        foodEntertainment = 350; //350
        funEntertainment = 150; //150
        emma = 50;
        debt = 250; //250
        phone = 10.00; //10
        gym = 200; //200
        float totalPersonal = foodEntertainment + funEntertainment + debt + phone + gym + emma;
        return totalPersonal;
    }

    float calcRemainder (float veh, float hou, float per){
        float remainder = income * (1 - savings);
        remainder = remainder - veh - hou - per;
        return remainder;
    }

    void calcRent (float remainder){
        cout << "I can spend up to: " << remainder << " on rent\n"; 
    }
};

int main(){
    monthBudget month;
    month.setIncome();
    float vehicleExpenses = month.setVehicleExpenses();
    float housingExpenses = month.setHousingExenses();
    float personalExpenses = month.setPersonalExpenses();
    float remainder = month.calcRemainder(vehicleExpenses, housingExpenses, personalExpenses);
    month.calcRent(remainder);
    cout << "Saving: $" << (month.income * month.savings) << " per month \n\n";


}