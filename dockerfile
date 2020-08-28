FROM python:3

ADD ex_main.py /home/codersarts/Downloads/machine-learning-programming-assignments-coursera-andrew-ng-master/machine-learning-ex1/ex1/lin_reg/ex_main.py

ADD ex_main.py /home/codersarts/Downloads/machine-learning-programming-assignments-coursera-andrew-ng-master/machine-learning-ex1/ex1/lin_reg/requirements.txt

ADD ex1data1.txt /home/codersarts/Downloads/machine-learning-programming-assignments-coursera-andrew-ng-master/machine-learning-ex1/ex1/lin_reg

RUN ln -s /usr/include/locale.h /usr/include/xlocale.h

RUN pip install numpy
RUN pip install pandas
RUN pip install matplotlib
RUN pip install scikit-learn

EXPOSE 5000



CMD ["python","/home/codersarts/Downloads/machine-learning-programming-assignments-coursera-andrew-ng-master/machine-learning-ex1/ex1/lin_reg/ex_main.py"]


