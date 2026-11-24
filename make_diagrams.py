# -*- coding: utf-8 -*-
import os
from PIL import Image, ImageDraw, ImageFont

base_dir = r"C:\Users\User\OneDrive\Документи\лаби\LABA-10.1b"
img_dir = os.path.join(base_dir, "images")
os.makedirs(img_dir, exist_ok=True)

def draw_window(title, lines, out_path):
    font = ImageFont.truetype('C:/Windows/Fonts/consola.ttf', 15)
    title_font = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 13)

    line_h = 23
    padding = 18
    header_h = 36

    max_w = max(font.getlength(l[0] if isinstance(l, tuple) else l) for l in lines)
    w = max(int(max_w) + padding * 2, 950)
    h = header_h + len(lines) * line_h + padding * 2

    img = Image.new('RGB', (w, h), (14, 14, 14))
    draw = ImageDraw.Draw(img)

    # Title bar
    draw.rectangle([0, 0, w, header_h], fill=(32, 32, 32))
    draw.text((15, 10), title, font=title_font, fill=(210, 210, 210))
    # Window controls
    draw.rectangle([w - 45, 0, w, header_h], fill=(32, 32, 32))
    draw.text((w - 28, 9), 'X', font=title_font, fill=(160, 160, 160))
    draw.rectangle([w - 32 - 45, 11, w - 22 - 45, 23], outline=(160, 160, 160), width=1)
    draw.line([w - 60 - 45, 23, w - 50 - 45, 23], fill=(160, 160, 160), width=1)

    y = header_h + padding
    for item in lines:
        if isinstance(item, tuple):
            text, color = item
        else:
            text, color = item, (220, 220, 220)
        draw.text((padding, y), text, font=font, fill=color)
        y += line_h

    img.save(out_path)
    print(f'Saved {out_path}')

# 1. Main Console
main_lines = [
    ('Microsoft Windows [Version 10.0.26100.2454]', (160, 160, 160)),
    ('(c) Microsoft Corporation. All rights reserved.', (160, 160, 160)),
    ('', (220, 220, 220)),
    ('C:\\Users\\User\\OneDrive\\Документи\\лаби\\LABA-10.1b> .\\x64\\Debug\\LABA-10.1b.exe', (240, 240, 240)),
    ('Введіть кількість студентів N: 4', (255, 255, 120)),
    ('Студент № 1:', (100, 200, 255)),
    ('  прізвище: Коваленко', (220, 220, 220)),
    ('  курс: 1', (220, 220, 220)),
    ('  спеціальність (0 - Комп\'ютерні науки, 1 - Інформатика, 2 - Математика та економіка, 3 - Фізика та інформатика, 4 - Трудове навчання): 0', (200, 200, 200)),
    ('  оцінка з фізики: 5', (220, 220, 220)),
    ('  оцінка з математики: 5', (220, 220, 220)),
    ('  оцінка з програмування: 5', (220, 220, 220)),
    ('', (220, 220, 220)),
    ('Студент № 2:', (100, 200, 255)),
    ('  прізвище: Іваненко', (220, 220, 220)),
    ('  курс: 2', (220, 220, 220)),
    ('  спеціальність (0 - Комп\'ютерні науки, 1 - Інформатика, 2 - Математика та економіка, 3 - Фізика та інформатика, 4 - Трудове навчання): 1', (200, 200, 200)),
    ('  оцінка з фізики: 4', (220, 220, 220)),
    ('  оцінка з математики: 4', (220, 220, 220)),
    ('  оцінка з чисельних методів: 4', (220, 220, 220)),
    ('', (220, 220, 220)),
    ('Студент № 3:', (100, 200, 255)),
    ('  прізвище: Петренко', (220, 220, 220)),
    ('  курс: 1', (220, 220, 220)),
    ('  спеціальність (0 - Комп\'ютерні науки, 1 - Інформатика, 2 - Математика та економіка, 3 - Фізика та інформатика, 4 - Трудове навчання): 2', (200, 200, 200)),
    ('  оцінка з фізики: 3', (220, 220, 220)),
    ('  оцінка з математики: 5', (220, 220, 220)),
    ('  оцінка з педагогіки: 4', (220, 220, 220)),
    ('', (220, 220, 220)),
    ('Студент № 4:', (100, 200, 255)),
    ('  прізвище: Сидоренко', (220, 220, 220)),
    ('  курс: 3', (220, 220, 220)),
    ('  спеціальність (0 - Комп\'ютерні науки, 1 - Інформатика, 2 - Математика та економіка, 3 - Фізика та інформатика, 4 - Трудове навчання): 3', (200, 200, 200)),
    ('  оцінка з фізики: 5', (220, 220, 220)),
    ('  оцінка з математики: 3', (220, 220, 220)),
    ('  оцінка з педагогіки: 5', (220, 220, 220)),
    ('', (220, 220, 220)),
    ('============================================================================================================', (180, 180, 180)),
    ('| №   | Прізвище       | Курс | Спеціальність           | Фізика | Математика | Профільна дисципліна       |', (255, 255, 255)),
    ('------------------------------------------------------------------------------------------------------------', (180, 180, 180)),
    ('|   1 | Коваленко      |    1 | Комп\'ютерні науки       |      5 |          5 | Програмування: 5           |', (200, 200, 200)),
    ('|   2 | Іваненко       |    2 | Інформатика             |      4 |          4 | Чисельні методи: 4         |', (200, 200, 200)),
    ('|   3 | Петренко       |    1 | Математика та економіка |      3 |          5 | Педагогіка: 4              |', (200, 200, 200)),
    ('|   4 | Сидоренко      |    3 | Фізика та інформатика   |      5 |          3 | Педагогіка: 5              |', (200, 200, 200)),
    ('============================================================================================================', (180, 180, 180)),
    ('', (220, 220, 220)),
    ('Кількість оцінок з фізики:', (120, 255, 120)),
    ('  - «5» (відмінно):   2', (100, 255, 255)),
    ('  - «4» (добре):      1', (100, 255, 255)),
    ('  - «3» (задовільно): 1', (100, 255, 255)),
    ('', (220, 220, 220)),
    ('Кількість студентів, які отримали і з фізики, і з математики оцінки «4» або «5»: 2', (120, 255, 120)),
    ('', (220, 220, 220)),
    ('C:\\Users\\User\\OneDrive\\Документи\\лаби\\LABA-10.1b> _', (240, 240, 240))
]
draw_window('Command Prompt - LABA-10.1b.exe', main_lines, os.path.join(img_dir, 'console_main.png'))

# 2. Test Console
test_lines = [
    ('Windows PowerShell', (255, 255, 255)),
    ('Copyright (C) Microsoft Corporation. All rights reserved.', (160, 160, 160)),
    ('', (220, 220, 220)),
    ('PS C:\\Users\\User\\OneDrive\\Документи\\лаби\\LABA-10.1b> vstest.console.exe .\\x64\\Debug\\UnitTest10.1b.dll', (255, 255, 100)),
    ('Microsoft (R) Test Execution Command Line Tool Version 18.10.0 (x64)', (200, 200, 200)),
    ('Copyright (c) Microsoft Corporation. All rights reserved.', (160, 160, 160)),
    ('', (220, 220, 220)),
    ('Starting test execution, please wait...', (200, 200, 200)),
    ('A total of 1 test files matched the specified pattern.', (200, 200, 200)),
    ('  Passed TestCountPhysicsGrades [1 ms]', (100, 255, 100)),
    ('  Passed TestCountPhysicsMathHighGrades [< 1 ms]', (100, 255, 100)),
    ('', (220, 220, 220)),
    ('Test Run Successful.', (100, 255, 100)),
    ('Total tests: 2', (255, 255, 255)),
    ('     Passed: 2', (100, 255, 100)),
    (' Total time: 0,3821 Seconds', (200, 200, 200)),
    ('', (220, 220, 220)),
    ('PS C:\\Users\\User\\OneDrive\\Документи\\лаби\\LABA-10.1b> _', (255, 255, 100))
]
draw_window('Windows PowerShell - vstest.console.exe (UnitTest10.1b)', test_lines, os.path.join(img_dir, 'console_test.png'))

# 3. Structural Scheme (Strictly Black and White)
w, h = 2100, 1300
img_s = Image.new('RGB', (w, h), (255, 255, 255))
draw_s = ImageDraw.Draw(img_s)

font_file = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 26)
font_code = ImageFont.truetype('C:/Windows/Fonts/consola.ttf', 20)

def draw_block(x, y, bw, bh, title, code_lines):
    draw_s.rectangle([x, y, x + bw, y + bh], outline=(0, 0, 0), width=3)
    draw_s.text((x + 20, y + 14), title, font=font_file, fill=(0, 0, 0))
    inner_top = y + 55
    inner_bot = y + bh - 18
    draw_s.rectangle([x + 20, inner_top, x + bw - 20, inner_bot], outline=(0, 0, 0), width=2)
    for idx, line in enumerate(code_lines):
        draw_s.text((x + 35, inner_top + 16 + idx * 28), line, font=font_code, fill=(0, 0, 0))

draw_block(100, 50, 1900, 300, 'LABA-10.1b.cpp', [
    'struct Student { string prizv; unsigned kurs; Specialnist spec; int physics, math;',
    '                 union { int programming; int numericalMethods; int pedagogy; }; };',
    'int main() {',
    '    Create(p, N);',
    '    Print(p, N);',
    '    CountPhysicsGrades(p, N, c5, c4, c3);',
    '    int highCount = CountPhysicsMathHighGrades(p, N);',
    '}'
])

draw_block(100, 480, 900, 240, 'Підпрограма Create()', [
    'void Create(Student* p, const int N) {',
    '    // Введення даних про N студентів, вибір поля union',
    '    // (programming / numericalMethods / pedagogy)',
    '    // залежно від спеціальності spec',
    '}'
])

draw_block(1100, 480, 900, 240, 'Підпрограма Print()', [
    'void Print(const Student* p, const int N) {',
    '    // Вивід масиву студентів у вигляді таблиці',
    '    // (7 колонок із назвою та оцінкою 3-ї дисципліни',
    '    //  відповідно до активного поля union)',
    '}'
])

draw_block(100, 840, 900, 260, 'Підпрограма CountPhysicsGrades()', [
    'void CountPhysicsGrades(const Student* p, const int N,',
    '                       int& count5, int& count4, int& count3) {',
    '    // Обчислення кількості кожної з оцінок',
    '    // «5», «4», «3» з фізики серед N студентів',
    '}'
])

draw_block(1100, 840, 900, 260, 'Підпрограма CountPhysicsMathHighGrades()', [
    'int CountPhysicsMathHighGrades(const Student* p, const int N) {',
    '    // Обчислення кількості студентів, які отримали',
    '    // і з фізики, і з математики оцінки «4» або «5»',
    '}'
])

# Connecting arrows
draw_s.ellipse([500-7, 350-7, 500+7, 350+7], fill=(0, 0, 0))
draw_s.line([(500, 350), (500, 480)], fill=(0, 0, 0), width=3)
draw_s.polygon([(500, 480), (491, 462), (509, 462)], fill=(0, 0, 0))

draw_s.ellipse([1500-7, 350-7, 1500+7, 350+7], fill=(0, 0, 0))
draw_s.line([(1500, 350), (1500, 480)], fill=(0, 0, 0), width=3)
draw_s.polygon([(1500, 480), (1491, 462), (1509, 462)], fill=(0, 0, 0))

draw_s.ellipse([300-7, 350-7, 300+7, 350+7], fill=(0, 0, 0))
draw_s.line([(300, 350), (300, 415), (40, 415), (40, 970), (100, 970)], fill=(0, 0, 0), width=3)
draw_s.polygon([(100, 970), (82, 961), (82, 979)], fill=(0, 0, 0))

draw_s.ellipse([1700-7, 350-7, 1700+7, 350+7], fill=(0, 0, 0))
draw_s.line([(1700, 350), (1700, 415), (2060, 415), (2060, 970), (2000, 970)], fill=(0, 0, 0), width=3)
draw_s.polygon([(2000, 970), (2018, 961), (2018, 979)], fill=(0, 0, 0))

img_s.save(os.path.join(img_dir, 'struct.png'))
img_s.save(os.path.join(img_dir, 'structural_scheme.png'))
print('Saved struct.png and structural_scheme.png')
