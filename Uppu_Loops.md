```python
odds= [1,3,5,7]
```


```python
print (odds[0])
print (odds[1])
print (odds[2])
print (odds[3])
```

    1
    3
    5
    7



```python
odds=[1,3,5]
print (odds[0])
print (odds[1])
print (odds[2])
print (odds[3])
```

    1
    3
    5



    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-4-3bf8ffe93a24> in <module>
          3 print (odds[1])
          4 print (odds[2])
    ----> 5 print (odds[3])
    

    IndexError: list index out of range



```python
odds = [1,3,5,7,9,11,13,15,17,19]
for num in odds: 
    print(num)
    
```

    1
    3
    5
    7
    9
    11
    13
    15
    17
    19



```python
length =0 
names = ['Curie', 'Darwin','Turing']
for value in names:
    length= length+1
print ('There are', length, 'names in the list.')
```

    There are 3 names in the list.



```python
name = "Rosalind"
for name in ['Curie', 'Darwin','Turing']:
    print (name)
print('after the loop, name is',name)
```

    Curie
    Darwin
    Turing
    after the loop, name is Turing



```python
print (len([0,1,2,3]))
```

    4



```python
name= ['Curie', 'Darwin','Turing']
print (len(name))
```

    3



```python

```
