#include <iostream>
#include <fstream>
#include <numeric>
#include <vector>

class Trees
{
    std::ifstream _file;
    std::string _line;
    std::vector<std::string> _vec;
    size_t _index;
    size_t _maxindex;

    size_t _count;
    std::vector<size_t> _counts;

    public: 
    Trees(std::string const& file)
    :
        _count(0),
        _index(0)
    {
        _file.open(file);
        while (_file >> _line)
        {
            _vec.push_back(_line);
        }
        _maxindex = _line.size();
    }

    void countTrees(size_t const& right, size_t const& down)
    {
        for (size_t idx = 0; idx < _vec.size(); idx += down){
            if (_vec.at(idx).at(_index) == '#')
            {
                _count++;
            }
            _index = ( _index + right ) %= _maxindex;
        }
        std::cout << "Count = " << _count << '\n';
        _counts.push_back(_count);

        _count = 0;
        _index = 0;
    }

    size_t countProduct()
    {
        return std::accumulate(begin(_counts), end(_counts), 1, std::multiplies<size_t>());
    }
};

int main()
{
    Trees trees("data3.txt");
    trees.countTrees(1, 1);
    trees.countTrees(3, 1);
    trees.countTrees(5, 1);
    trees.countTrees(7, 1);
    trees.countTrees(1, 2);
    std::cout << "Multiplied number of trees = " << trees.countProduct() << '\n';
}