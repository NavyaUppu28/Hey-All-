```python
numbers = [1.5, 2.3, 0.7, 0.001, 4.4]
total = 0.0
for num in numbers:
    assert num > 0.0, 'Data should only contain positive values'
    total += num
print('total is:', total)
```

    total is: 8.901



```python
def normalize_rectangle(rect):
    """Normalizes a rectangle so that it is at the origin and 1.0 units long on its longest axis.
    Input should be of the format (x0, y0, x1, y1).
    (x0, y0) and (x1, y1) define the lower left and upper right corners
    of the rectangle, respectively."""
    assert len(rect) == 4, 'Rectangles must contain 4 coordinates'
    x0, y0, x1, y1 = rect
    assert x0 < x1, 'Invalid X coordinates'
    assert y0 < y1, 'Invalid Y coordinates'

    dx = x1 - x0
    dy = y1 - y0
    if dx > dy:
        scaled = dx / dy
        upper_x, upper_y = 1.0, scaled
    else:
        scaled = dx / dy
        upper_x, upper_y = scaled, 1.0

    assert 0 < upper_x <= 1.0, 'Calculated upper X coordinate invalid'
    assert 0 < upper_y <= 1.0, 'Calculated upper Y coordinate invalid'

    return (0, 0, upper_x, upper_y)
```


```python
print(normalize_rectangle( (0.0, 0.0, 1.0,5.0) ))
```

    (0, 0, 0.2, 1.0)



```python

```
