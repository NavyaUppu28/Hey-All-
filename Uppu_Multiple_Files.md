```python
import glob
```


```python
print (glob.glob('inflammation*.csv'))
```

    ['inflammation-05.csv', 'inflammation-12.csv', 'inflammation-04.csv', 'inflammation-08.csv', 'inflammation-10.csv', 'inflammation-06.csv', 'inflammation-09.csv', 'inflammation-01.csv', 'inflammation-07.csv', 'inflammation-11.csv', 'inflammation-03.csv', 'inflammation-02.csv']



```python
import glob
import numpy
import matplotlib.pyplot

filenames= sorted(glob.glob('inflammation*.csv'))
filenames= filenames[0:3]

for filename in filenames:
    print(filename)
    
    data= numpy.loadtxt(fname=filename, delimiter=',')
    
    fig= matplotlib.pyplot.figure(figsize= (10.0,3.0))
    
    axes1= fig.add_subplot(1,3,1)
    axes2= fig.add_subplot(1,3,2)
    axes3= fig.add_subplot(1,3,3)
    
    axes1.set_ylabel('average')
    axes1.plot(numpy.mean(data, axis=0))
    
    axes2.set_ylabel('max')
    axes2.plot(numpy.amax(data, axis=0))
    
    axes3.set_ylabel('min')
    axes3.plot(numpy.amin(data, axis=0))
    
    fig.tight_layout()
    matplotlib.pyplot.show()
```

    inflammation-01.csv



![png](output_2_1.png)


    inflammation-02.csv



![png](output_2_3.png)


    inflammation-03.csv



![png](output_2_5.png)



```python

```
