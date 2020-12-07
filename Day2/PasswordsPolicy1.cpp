#include <iostream>
#include <fstream>
#include <vector>

class Passwords
{
    public:
        std::ifstream d_file;
        std::string d_lineContent;
        std::vector<std::string> d_vec;

        uint d_minChar = 0;
        uint d_maxChar = 0;
        std::string d_policy;
        std::string d_password;
        uint d_charCount = 0;
        uint d_matchCount = 0;

    public:
        Passwords(std::string& fileName);
};

Passwords::Passwords(std::string& fileName)
{
    try {
        d_file.open(fileName);
        while (std::getline(d_file, d_lineContent))
        {
            std::string line = d_lineContent;
            auto posMinus = line.find('-');
            auto posColon = line.find(':');
            
            d_minChar = std::stoi(line.substr(0, posMinus));
            d_maxChar = std::stoi(line.substr(posMinus + 1, posColon - 1));
            d_policy = line.substr(posColon - 1, 1);
            d_password = line.substr(posColon + 2);

            // Do the check
            d_charCount = 0;
            for (int idx = 0; idx < d_password.size(); idx++)
            {
                if (d_policy.find(d_password[idx]) != std::string::npos)
                {
                    ++d_charCount;
                }
            }
            if (d_charCount >= d_minChar && d_charCount <= d_maxChar)
            {
                ++d_matchCount;
            }
            std::cout << "Password: " << d_password << " with letter " << d_policy << " and " << d_minChar << " and " << d_maxChar
            << " Found size: " << d_password.size() << " and charcount: " << d_charCount  << " and matchcount: " << d_matchCount << '\n';
        }
    } catch (std::exception& exc)
    {
        std::cout << "Cannot open file: " << exc.what();
    }
}

int main()
{
    std::string filename = "data";
    Passwords passwords(filename);
}