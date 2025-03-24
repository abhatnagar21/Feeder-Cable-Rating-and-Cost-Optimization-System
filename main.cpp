#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

struct Cable {
    string name;
    double price;
    int rating;
};

bool compareByRating(const Cable &a, const Cable &b) {
    return a.rating < b.rating;
}

int main() {
    map<string, Cable> cableMap;
    vector<Cable> cables;
    double feeder_voltage;

    cout << "Enter the feeder voltage (11 or 3.3): ";
    cin >> feeder_voltage;

    if (feeder_voltage != 11.0 && feeder_voltage != 3.3) {
        cout << "Invalid feeder voltage. Please enter 11 or 3.3." << endl;
        return 0;
    }

    vector<string> cableTypes = (feeder_voltage == 11.0) ? vector<string>{"3C-185", "1C-240", "1C-400", "1C-500", "1C-630"} : vector<string>{"3C-150", "1C-150"};

    for (const string &cableName : cableTypes) {
        double price;
        int rating;

        cout << "Enter price of " << cableName << ": ";
        cin >> price;
        cout << "Enter rating of " << cableName << ": ";
        cin >> rating;

        cables.push_back({cableName, price, rating});
        cables.push_back({"2_" + cableName, 2 * price, 2 * rating});
        cables.push_back({"3_" + cableName, 3 * price, 3 * rating});
    }

    sort(cables.begin(), cables.end(), compareByRating);

    cout << "\nAll cables sorted by rating:" << endl;
    for (const auto &cable : cables) {
        cout << cable.name << ": Price = " << cable.price << " per meter, Rating = " << cable.rating << endl;
    }

    while (true) {
        int currentDensity;
        cout << "\nEnter the current density (or type -1 to exit): ";
        cin >> currentDensity;
        if (currentDensity == -1) {
            cout << "Exiting the program." << endl;
            break;
        }

        Cable bestCable = {"", 1e9, 0};
        bool found = false;

        for (const auto &cable : cables) {
            if (cable.rating >= currentDensity && cable.price < bestCable.price) {
                bestCable = cable;
                found = true;
            }
        }

        if (found) {
            cout << "\nBest suitable cable for current density " << currentDensity << ":" << endl;
            cout << bestCable.name << ": Price = " << bestCable.price << " per meter, Rating = " << bestCable.rating << endl;
        } else {
            cout << "No cable meets the required current density." << endl;
        }
    }

    return 0;
}
