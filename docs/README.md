# Работа с решением

## Подключение
В файле, в котором планируется использовать решение, необходимо **явно** прописать использование нужных или всех решений в виде: 
```python
import circle
import rectangle
import square
import triangle
```
Или в виде:
```python
from circle import function_name
from rectangle import function_name
from square import function_name
from triangle import function_name
```  
> [!NOTE]  
> `function_name` может принимать значения `area` или `perimetr`  

## Использование и вызов функций
Для вызова функции необходимо **явно** указать, из какого файла решения вызывается функция и название самой функции, разделяя эти значения точкой. В круглые скобки передать **валидные** аргументы. Пример:
```python
# your code

a = rectangle.area(a, b)

# your code
```
> [!CAUTION]  
> Функции каждого решения принимают разное количество аргументов. За этим необходимо следить! Количество принимаемых аргументов приведено ниже.

Функции решений принимают соответствующее количество аргументов:
- circle: 1
- rectangle: 2
- square: 1
- triangle: 3  

Аргументы - определяющие значения для фигуры. Для квадрата, прямугольника и треугольника - длины сторон, для круга - радиус. 

> [!TIP]
> Функции возвращают значения, соответствующие названиям: area - площадь фигуры, perimetr - периметр фигуры.

## Примеры вызова функций
```python
circleArea = circle.area(2)
circlePerimetr = circle.perimetr(3)

rectangleArea = rectangle.area(2, 4)
rectanglePerimetr = rectangle.perimetr(3, 5)

squareArea = square.area(5)
squarePerimetr = square.perimetr(8)

triangleArea = triangle.area(3, 4, 5)
trianglePerimetr = triangle.perimetr(12, 5, 13)
```

# Используемые математические формулы
## Площадь
- Круг: S = πR²
- Прямоугольник: S = ab
- Квадрат: S = a²
- Треугольник: S = ( p(p - a)(p - b)(p - c) )<sup>1/2</sup>

## Периметр
- Круг: P = 2πR
- Прямоугольник: P = 2a + 2b
- Квадрат: P = 4a
- Треугольник: P = a + b + c

# История изменения проекта (коммиты)
- bfa56732de048eab1e822444bcf02ea545ab480d - "File added" (rectangle.py) by Stepan, 12.09.2026
- 2ca60facafe31a6162fc60631741a71cd00730be - "File added" (triangle.py) by Stepan, 12.09.2026
- 8bf3d75518d42d739712619c7462969603c23c11 - "Error terminated" (in file rectangle.py) by Stepan, 12.09.2026
- 00ed2bff87f55e20e006c0f302e51bebdca347f0 - "Comments added" (in all files in project) by Stepan, 13.09.2026