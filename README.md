# IMAGE-EDITOR
This is a simple Image Editor which performs a few basic tasks on an input image. They are applying an "Averaging Filter" and performing "Edge Detection" and finding out "Path Of Least Energy" on a given image.

Averaging Filter creates new pixel values at the location by computing the average pixel value of the neighbouring cells of size 3x3. 

In Edge Detection, the idea is to to compute some function of pixel values among neighbouring cells in horizontal and vertical directions. The function approximates how close these pixel values are relative to each other. If pixel values in neighbourhood are similar the nthis function would be very small or 0 where as if there is a significant change in neighbourhood pixel values, then this function would have non-zero values. We detect prescence of an edge by noticing how this function value changes.

Path of least energy involves implementing an algorithm that finds a path from top of the image to the bottom which has least energy.
