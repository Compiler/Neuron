
CXX = g++
C++_VERSION = c++11
CXXFLAGS = -std=$(C++_VERSION) -Wall -w -g -static-libgcc -static-libstdc++

OUT_DIR = bin
LAUNCHER_NAME = Neuron
SRC_DIR = src
ENTRY_POINT = src/main.cpp

#lib
GLM_ROOT = outsourced/glm/

INCLUDES = -I $(GLM_ROOT)

ALL_SETTINGS = $(CXX) $(CXXFLAGS) $(LIBS) $(INCLUDES) 

all: main

main: $(ENTRY_POINT) $(OBJS)
	$(ALL_SETTINGS) -o $(OUT_DIR)/$(LAUNCHER_NAME) $^ 
	./$(OUT_DIR)/$(LAUNCHER_NAME).exe


mainpy:
	python core.py