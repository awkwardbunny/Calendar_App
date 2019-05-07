.PHONY: clean debug run

CXX = g++
CXXFLAGS = -g -I./inc #-std=c++11 -g #optional flags
LDFLAGS =

SRC=$(wildcard src/*.cpp)
OBJ = $(SRC:.cpp=.o)

#$(info $$SRC is [${SRC}])
#$(info $$OBJ is [${OBJ}])

EXECUTABLE = main

all: $(EXECUTABLE)

$(EXECUTABLE): $(OBJ)
	$(CXX) $(CXX_FLAGS) -o $@ $(OBJ) $(LDFLAGS)

clean:
	rm -rf $(EXECUTABLE) $(OBJ)

run:
	./$(EXECUTABLE)
