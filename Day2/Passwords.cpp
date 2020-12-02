#include <iostream>
#include <fstream>
#include <vector>

class Passwords
{
    public:
        std::ifstream file;
        std::string lineContent;
        std::vector<std::string> vec;

    public:
        Passwords(std::string& fileName);
        size_t CheckPasswords();
};

Passwords::Passwords(std::string& fileName)
{
    try {
        file.open(fileName);
        while (std::getline(file, lineContent))
        {
            vec.push_back(lineContent);
        }
    } catch (std::exception& exc)
    {
        std::cout << "Cannot open file: " << exc.what();
    }
}

size_t Passwords::CheckPasswords()
{
    for (size_t idx = 0; idx != vec.size(); ++idx) 
    {
        std::cout << "Found: " << vec[idx];
    }
    return 3;
}

int main()
{
    std::string filename = "data";
    Passwords passwords(filename);
    passwords.CheckPasswords();
}