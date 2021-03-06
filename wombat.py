
# coding: utf-8

# <img src="images/jupiter.png" width="200" height="200"/>

# # Using Jupyter

# ## Markdown cells
# 
# This is a Markdown (documentation) cell, for adding documentation and comments to a notebook. It uses Markdown, a text styling language, as well as HTML. When a Markdown cell is "run", it converts the contents of the cell into HTML, which is then rendered and displayed.
# 
# Double-click on a Markdown cell to see its source.
# 
# This is **more** _markdown_. Surround text with double asterisk for bold, or single underline for italic.

# ## Code Cells
# 
# Code cells contain Python (or other language) code. When a code cell is run, it executes the code, and shows the output below the cell. The output is retained unless you explicitly clear it. 

# In[ ]:


x = 3
for i in range(3):
    print(i)


# ## It's all one program
# 
# All code is run in the same instance of the Python interpreter, so that objects created in one cell are available to other cells, as long as the first cell has been run.

# In[ ]:


from datetime import date as Date


# In[ ]:


then = Date(2011,5,22)


# In[ ]:


print(then.year)


# In[ ]:


get_ipython().magic('pinfo then')


# ## Getting help
# Putting a ? before (or after) any object displays help for that object. Using ?? will add more detailed help, if available. (The output will be in a separate pane at the bottom of the browser window).

# In[4]:


get_ipython().magic('pinfo i')


# In[ ]:


get_ipython().magic('pinfo2 Date')


# ## Using Python's scientific libraries
# For typical use of Python's scientific libraries, put the following at the top of the notebook in a code cell:
# 
# <pre>
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# </pre>
# 
# Other  modules and packages should be included as needed.
# 

# In[6]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# ## Inline plotting
# After matplotlib is imported, use the **%matplotlib inline** magic to display figures as part of the notebook. Otherwise, they are displayed in popup windows. 

# In[7]:


plt.plot(np.arange(1,25))


# ## Using HTML
# 
# Since Markdown is converted to HTML, any actual HTML in a Markdown cell is used. 
# 
# <ul><li>red</li><li>purple</li><li>orange</li></ul>

# ## Magics
# 
# iPython and Jupyter notebooks have _line magics_, which are line-oriented. Many of them execute commands or turn iPython settings on and off. 
# 
# Jupyter has _cell magics_, which apply to the entire cell. 

# In[ ]:


get_ipython().magic('lsmagic')


# In[ ]:


get_ipython().magic('system hostname')
h = get_ipython().magic('system hostname')
print(h)


# ## Running external Python scripts
# 
# Use the **%run** magic to launch an external Python script

# In[ ]:


get_ipython().magic('run ../EXAMPLES/read_tyger.py')


# ## Using LaTeX
# 
# Markdown cells can render LaTeX via MathJax. Put the LaTeX code inside a pair of dollar signs: **\$\rho\$:**
# 
# $\rho$, $\rho$, $\rho$ your boat

# $\mathbf{V}_1 \times \mathbf{V}_2 =  \begin{vmatrix} \
# \mathbf{i} & \mathbf{j} & \mathbf{k}  \\
# \frac{\partial X}{\partial u} & \frac{\partial Y}{\partial u} & 0\\
# \frac{\partial X}{\partial v} & \frac{\partial Y}{\partial v} & 0\\
# \end{vmatrix}$ 
# 
# $\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)$

# ### A limerick

# 
# $\frac{12 + 144  + 20 + 3\sqrt{4}}{7} + (5 * 11) = 9^2 + 0$ <br/>
# 
# <i>See text of limerick at the bottom of this notebook</i>
# 
# 

# ## Benchmarking
# 
# The **%%timeit** cell magic will execute the code in the cell and report the average time it took to execute it. 

# In[ ]:


fruits = ["pomegranate", "cherry", "apricot", "date", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE" ]


# #### Benchmark with *for* loop

# In[ ]:


get_ipython().run_cell_magic('timeit', '', 'f1 = []\nfor f in fruits:\n    f1.append(f[:3])')


# #### Benchmark with list comprehension

# In[ ]:


get_ipython().run_cell_magic('timeit', '100', 'f2 = [f[:3] for f in fruits]')


# ## Images
# 
# You can insert images into doc cells using the Markdown image tag:
# 
# _The following uses a Markdown table to arrange the images._ 
# 
# | Guido        | Tim          | Wombat  |
# | ------------- |:-------------:| -----:|
# | ![Guido](images/guido.png)|  ![Tim](images/tim.jpg) |![wombat](images/wombat.jpg) |
# 

# ### The limerick
# 
# A dozen, a gross, and a score<br/>
# Plus three times the square root of four<br/>
# Divided by seven<br/>
# Plus five times eleven<br/>
# Is nine squared and not a bit more.<br/>
# 
