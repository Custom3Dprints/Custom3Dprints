#include <iostream>
#include <fstream>
#include <vector>
#include <numeric>
#include <iomanip>

int main() {
    std::ifstream inputFile("Random.txt");
    if (!inputFile.is_open()) {
        std::cerr << "Unable to open the file.\n";
        return 1;
    }

    std::vector<int> numbers;
    int num;
    while (inputFile >> num) {
        numbers.push_back(num);
    }

    inputFile.close();

    int numOfNumbers = numbers.size();
    int sumOfNumbers = std::accumulate(numbers.begin(), numbers.end(), 0);
    double average = static_cast<double>(sumOfNumbers) / numOfNumbers;

    std::cout << "Number of numbers: " << numOfNumbers << std::endl;
    std::cout << "Sum of the numbers: " << sumOfNumbers << std::endl;
    std::cout << std::fixed << std::setprecision(1);
    std::cout << "Average of the numbers: " << average << std::endl;

    return 0;
}
