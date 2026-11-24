#include "pch.h"
#include "CppUnitTest.h"
#include "../LABA-10.1b/student_b.h"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace UnitTest101b
{
    static Student MakeStudent(const std::string& prizv, unsigned kurs, Specialnist spec, int physics, int math, int third)
    {
        Student s;
        s.prizv = prizv;
        s.kurs = kurs;
        s.spec = spec;
        s.physics = physics;
        s.math = math;
        if (spec == KOMP_NAUKY)
            s.programming = third;
        else if (spec == INFORMATYKA)
            s.numericalMethods = third;
        else
            s.pedagogy = third;
        return s;
    }

    TEST_CLASS(UnitTest101b)
    {
    public:
        TEST_METHOD(TestCountPhysicsGrades)
        {
            const int N = 4;
            Student students[N] = {
                MakeStudent("Коваленко", 1, KOMP_NAUKY,  5, 5, 5),
                MakeStudent("Іваненко",  2, INFORMATYKA, 4, 4, 4),
                MakeStudent("Петренко",  1, MAT_EKON,    3, 5, 4),
                MakeStudent("Сидоренко", 3, FIZ_INF,     5, 3, 5)
            };

            int c5 = 0, c4 = 0, c3 = 0;
            CountPhysicsGrades(students, N, c5, c4, c3);

            Assert::AreEqual(2, c5);
            Assert::AreEqual(1, c4);
            Assert::AreEqual(1, c3);
        }

        TEST_METHOD(TestCountPhysicsMathHighGrades)
        {
            const int N = 4;
            Student students[N] = {
                MakeStudent("Коваленко", 1, KOMP_NAUKY,  5, 5, 5),
                MakeStudent("Іваненко",  2, INFORMATYKA, 4, 4, 4),
                MakeStudent("Петренко",  1, MAT_EKON,    3, 5, 4),
                MakeStudent("Сидоренко", 3, FIZ_INF,     5, 3, 5)
            };

            int highCount = CountPhysicsMathHighGrades(students, N);
            Assert::AreEqual(2, highCount);
        }
    };
}
