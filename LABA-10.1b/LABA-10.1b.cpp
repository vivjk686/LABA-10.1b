#include <iostream>
#include <Windows.h>
#include "student_b.h"

using namespace std;

int main()
{
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);

    int N;
    cout << "Введіть кількість студентів N: ";
    cin >> N;

    Student* p = new Student[N];

    Create(p, N);
    Print(p, N);

    int count5 = 0, count4 = 0, count3 = 0;
    CountPhysicsGrades(p, N, count5, count4, count3);

    cout << "Кількість оцінок з фізики:" << endl;
    cout << "  - «5» (відмінно):   " << count5 << endl;
    cout << "  - «4» (добре):      " << count4 << endl;
    cout << "  - «3» (задовільно): " << count3 << endl;
    cout << endl;

    int highGradesCount = CountPhysicsMathHighGrades(p, N);
    cout << "Кількість студентів, які отримали і з фізики, і з математики оцінки «4» або «5»: "
         << highGradesCount << endl;

    delete[] p;
    return 0;
}
