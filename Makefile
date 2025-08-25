# Boost library
BOOST = "C:\Program Files\Boost\boost_1_82_0\boost_1_82_0" # Change to your Boost library

# C++ compiler
CXX = g++-11 # Change to your C++ compiler
CXXFLAGS = -lstdc++ -std=c++17 -O2

SOURCES = $(wildcard Code/*.cpp Code/BetweennessApprox/*.cpp)

CBAG: $(SOURCES)
	$(CXX) -I $(BOOST) $(SOURCES) $(CXXFLAGS) -o CBAG

clean:
	rm CBAG
