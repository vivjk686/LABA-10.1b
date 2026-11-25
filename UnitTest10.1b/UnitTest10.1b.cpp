#include "pch.h"
#include "CppUnitTest.h"
#define UNIT_TEST
#include "../LABA-10.1b/LABA-10.1b.cpp"

using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace UnitTest101b
{
    TEST_CLASS(UnitTest101b)
    {
    public:
        TEST_METHOD(TestCountPhysicsGrades)
        {
            const int N = 4;
            Student p[N];
            p[0].prizv = "Kovalenko"; p[0].kurs = 1; p[0].spec = KN;  p[0].fizyka = 5; p[0].matematyka = 5; p[0].programuvannya = 5;
            p[1].prizv = "Ivanenko";  p[1].kurs = 2; p[1].spec = INF; p[1].fizyka = 4; p[1].matematyka = 4; p[1].chyselni_metody = 4;
            p[2].prizv = "Petrenko";  p[2].kurs = 1; p[2].spec = ME;  p[2].fizyka = 3; p[2].matematyka = 5; p[2].pedagogika = 4;
            p[3].prizv = "Sydorenko"; p[3].kurs = 3; p[3].spec = FI;  p[3].fizyka = 5; p[3].matematyka = 3; p[3].pedagogika = 5;

            int c5 = 0, c4 = 0, c3 = 0;
            CountPhysicsGrades(p, N, c5, c4, c3);
            Assert::AreEqual(2, c5);
            Assert::AreEqual(1, c4);
            Assert::AreEqual(1, c3);
        }

        TEST_METHOD(TestCountPhysicsMathHighGrades)
        {
            const int N = 4;
            Student p[N];
            p[0].prizv = "Kovalenko"; p[0].kurs = 1; p[0].spec = KN;  p[0].fizyka = 5; p[0].matematyka = 5; p[0].programuvannya = 5;
            p[1].prizv = "Ivanenko";  p[1].kurs = 2; p[1].spec = INF; p[1].fizyka = 4; p[1].matematyka = 4; p[1].chyselni_metody = 4;
            p[2].prizv = "Petrenko";  p[2].kurs = 1; p[2].spec = ME;  p[2].fizyka = 3; p[2].matematyka = 5; p[2].pedagogika = 4;
            p[3].prizv = "Sydorenko"; p[3].kurs = 3; p[3].spec = FI;  p[3].fizyka = 5; p[3].matematyka = 3; p[3].pedagogika = 5;

            Assert::AreEqual(2, CountPhysicsMathHighGrades(p, N));
        }
    };
}
