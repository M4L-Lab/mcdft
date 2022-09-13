#include "mcdft-structure/mcdft-structure.hpp"
#include <iostream>

int
main()
{
  int result = mcdftstructure::add_one(1);
  std::cout << "1 + 1 = " << result << std::endl;
}
