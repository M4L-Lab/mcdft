#include "catch2/catch.hpp"
#include "mcdft-structure/mcdft-structure.hpp"

using namespace mcdftstructure;

TEST_CASE("add_one", "[adder]")
{
  REQUIRE(add_one(0) == 1);
  REQUIRE(add_one(123) == 124);
  REQUIRE(add_one(-1) == 0);
}
