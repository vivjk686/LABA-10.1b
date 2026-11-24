#include "student_b.h"
#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

const string specialnistStr[] = {
    "Комп'ютерні науки",
    "Інформатика",
    "Математика та економіка",
    "Фізика та інформатика",
    "Трудове навчання"
};

void Create(Student* p, const int N)
{
    int ispec;
    for (int i = 0; i < N; i++)
    {
        cout << "Студент № " << i + 1 << ":" << endl;
        cin.get();
        cin.sync();

        cout << "  прізвище: "; getline(cin, p[i].prizv);
        cout << "  курс: "; cin >> p[i].kurs;
        cout << "  спеціальність (0 - Комп'ютерні науки, 1 - Інформатика, 2 - Математика та економіка, 3 - Фізика та інформатика, 4 - Трудове навчання): ";
        cin >> ispec;
        p[i].spec = (Specialnist)ispec;
        cout << "  оцінка з фізики: "; cin >> p[i].physics;
        cout << "  оцінка з математики: "; cin >> p[i].math;

        switch (p[i].spec)
        {
        case KOMP_NAUKY:
            cout << "  оцінка з програмування: "; cin >> p[i].programming;
            break;
        case INFORMATYKA:
            cout << "  оцінка з чисельних методів: "; cin >> p[i].numericalMethods;
            break;
        default:
            cout << "  оцінка з педагогіки: "; cin >> p[i].pedagogy;
            break;
        }
        cout << endl;
    }
}

void Print(const Student* p, const int N)
{
    cout << "============================================================================================================" << endl;
    cout << "| №   | Прізвище       | Курс | Спеціальність           | Фізика | Математика | Профільна дисципліна       |" << endl;
    cout << "------------------------------------------------------------------------------------------------------------" << endl;
    for (int i = 0; i < N; i++)
    {
        cout << "| " << setw(3) << right << i + 1 << " ";
        cout << "| " << setw(14) << left << p[i].prizv << " ";
        cout << "| " << setw(4) << right << p[i].kurs << " ";
        cout << "| " << setw(23) << left << specialnistStr[p[i].spec] << " ";
        cout << "| " << setw(6) << right << p[i].physics << " ";
        cout << "| " << setw(10) << right << p[i].math << " ";

        string thirdCol;
        switch (p[i].spec)
        {
        case KOMP_NAUKY:
            thirdCol = "Програмування: " + to_string(p[i].programming);
            break;
        case INFORMATYKA:
            thirdCol = "Чисельні методи: " + to_string(p[i].numericalMethods);
            break;
        default:
            thirdCol = "Педагогіка: " + to_string(p[i].pedagogy);
            break;
        }
        cout << "| " << setw(26) << left << thirdCol << " |" << endl;
    }
    cout << "============================================================================================================" << endl;
    cout << endl;
}

void CountPhysicsGrades(const Student* p, const int N, int& count5, int& count4, int& count3)
{
    count5 = 0;
    count4 = 0;
    count3 = 0;
    for (int i = 0; i < N; i++)
    {
        if (p[i].physics == 5)
            count5++;
        else if (p[i].physics == 4)
            count4++;
        else if (p[i].physics == 3)
            count3++;
    }
}

int CountPhysicsMathHighGrades(const Student* p, const int N)
{
    int count = 0;
    for (int i = 0; i < N; i++)
    {
        if ((p[i].physics == 4 || p[i].physics == 5) &&
            (p[i].math == 4 || p[i].math == 5))
        {
            count++;
        }
    }
    return count;
}
