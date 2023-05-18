```python
import numpy
data = numpy.loadtxt(fname='inflammation-01.csv',delimiter= ',')
```


```python
import matplotlib.pyplot
image= matplotlib.pyplot.imshow(data)
matplotlib.pyplot.show()
```


![png](output_1_0.png)



```python
# Average inflammation over time
ave_inflammation = numpy.mean(data, axis=0)
ave_plot= matplotlib.pyplot.plot(ave_inflammation)
matplotlib.pyplot.show()
```


![png](output_2_0.png)



```python
max_plot = matplotlib.pyplot.plot(numpy.amax(data,axis=0))
matplotlib.pyplot.show()
```


![png](output_3_0.png)



```python
min_plot = matplotlib.pyplot.plot(numpy.amin(data,axis=0))
matplotlib.pyplot.show()
```


![png](output_4_0.png)



```python
fig= matplotlib.pyplot.figure(figsize=(10.0,3.0))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('average')
axes1.plot(numpy.mean(data, axis=0))

axes2.set_ylabel('max')
axes2.plot(numpy.amax(data, axis=0))

axes3.set_ylabel('min')
axes3.plot(numpy.amin(data, axis=0))

matplotlib.pyplot.savefig ('inflammation.png')
matplotlib.pyplot.show()
```


![png](output_5_0.png)



```python

```
