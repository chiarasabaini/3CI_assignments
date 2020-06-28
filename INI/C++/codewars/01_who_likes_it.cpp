#include <iostream>
#include <stdio.h>

std::string __author__ = "ameliexx";
std::string __version__ = "1.0 27-01-2020";

    std::switch (len(names)):
        case 0:
            return "no one likes this";
            break;
        case 1:
            s = names[0] + " likes this";
            return s;
            break;
        case 2:
            s = names[0] + " and " + names[1] + " like this";
            return s;
            break;
        case 3:
            s = names[0] + ", " + names[1] + " and " + names[2] + " like this";
            return s;
            break;
        case >= 4:
            s = names[0] + ", " + names[1] + " and " + len(names) + " others like this";
            return s;
            break;
}