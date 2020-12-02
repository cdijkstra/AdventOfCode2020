#include <iostream>
#include <fstream>
#include <vector>

void calculateProduct(std::vector<size_t> const& vec)
{
    for (size_t idx = 0; idx != vec.size() - 2; ++idx){
        for (size_t idy = idx; idy != vec.size() - 1; ++idy) {
            for (size_t idz = idy; idz != vec.size(); ++idz){
                if (vec.at(idx) + vec.at(idy) + vec.at(idz) == 2020){
                    std::cout << "The multiplied numbers are " << vec.at(idx) * vec.at(idy) * vec.at(idz) << '\n';
                    return;
                }
            }
        }
    }
    std::cout << "No numbers sum up to 2020\n";
}

int main()
{
    std::ifstream file;
    file.open("data");
    size_t expense;
    std::vector<size_t> vec;
    while (file >> expense)
    {
        vec.push_back(expense);
    }
    calculateProduct(vec);
}