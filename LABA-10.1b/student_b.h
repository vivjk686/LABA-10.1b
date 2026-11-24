#pragma once
#include <string>

enum Specialnist {
    KOMP_NAUKY,
    INFORMATYKA,
    MAT_EKON,
    FIZ_INF,
    TRUD_NAVCH
};

extern const std::string specialnistStr[];

struct Student {
    std::string prizv;
    unsigned kurs;
    Specialnist spec;
    int physics;
    int math;
    union {
        int programming;      // for KOMP_NAUKY
        int numericalMethods; // for INFORMATYKA
        int pedagogy;         // for others
    };
};

void Create(Student* p, const int N);
void Print(const Student* p, const int N);
void CountPhysicsGrades(const Student* p, const int N, int& count5, int& count4, int& count3);
int CountPhysicsMathHighGrades(const Student* p, const int N);
