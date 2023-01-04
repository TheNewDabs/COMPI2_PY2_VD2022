import base64
import io
import streamlit as st
import urllib
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score
from sklearn.naive_bayes import BernoulliNB, GaussianNB, MultinomialNB
from sklearn.model_selection import train_test_split

from matplotlib import pyplot as plot

def lineal(x_name, y_name, datos):
    x = datos[x_name].values.reshape(-1,1)
    y = datos[y_name].values.reshape(-1,1)
    #plot.clf()
    model = LinearRegression()
    model.fit(x, y)
    y_pred = model.predict(x)
    plot.figure(figsize=(5,4))
    ax = plot.axes()
    ax.scatter(x,y)
    ax.plot(x, y_pred)
    rnse = np.sqrt(mean_squared_error(y,y_pred))
    r2 = r2_score(y,y_pred)
    ax.set_xlabel(x_name)
    ax.set_ylabel(y_name)
    ax.axis('tight')
    plot.plot(x,y_pred,color='r')
    img = io.BytesIO()
    plot.title("RMSE: " + str(rnse) + " R2 " + str(r2))
    plot.suptitle("Grafica Regresión lineal")
    plot.savefig(img, format='png')
    plot_url = base64.b64encode(img.getvalue()).decode()
    plot.clf()
    ax = plot.axes()
    ax.set_xlabel(x_name)
    ax.set_ylabel(y_name)
    plot.scatter(x,y,color='r')
    img2 = io.BytesIO()
    plot.title("Grafica de puntos Regresión lineal")
    plot.savefig(img2, format='png')
    img2.seek(0)
    plot_url2 = base64.b64encode(img2.getvalue()).decode()
    return [plot_url, plot_url2]

def polinomial(x_name, y_name, datos):
    x = datos[x_name].values.reshape(-1,1)
    y = datos[y_name].values.reshape(-1,1)
    #plot.clf()
    poly = PolynomialFeatures(degree=3, include_bias=False)
    x_poly = poly.fit_transform(x)
    model = LinearRegression()
    model.fit(x_poly, y)
    y_pred = model.predict(x_poly)
    plot.figure(figsize=(5,4))
    ax = plot.axes()
    ax.scatter(x,y)
    ax.plot(x, y_pred)
    rnse = np.sqrt(mean_squared_error(y,y_pred))
    r2 = r2_score(y,y_pred)
    ax.set_xlabel(x_name)
    ax.set_ylabel(y_name)
    ax.axis('tight')
    plot.plot(x_poly,y_pred,color='r')
    img = io.BytesIO()
    plot.title("RMSE: " + str(rnse) + " R2 " + str(r2))
    plot.suptitle("Grafica Regresión lineal")
    plot.savefig(img, format='png')
    plot_url = base64.b64encode(img.getvalue()).decode()
    plot.clf()
    ax = plot.axes()
    ax.set_xlabel(x_name)
    ax.set_ylabel(y_name)
    plot.scatter(x,y,color='r')
    img2 = io.BytesIO()
    plot.title("Grafica de puntos Regresión lineal")
    plot.savefig(img2, format='png')
    img2.seek(0)
    plot_url2 = base64.b64encode(img2.getvalue()).decode()
    return [plot_url, plot_url2]

def Gaussiano(x_name, y_name, datos):
    x = datos[x_name].values.reshape(-1,1)
    y = datos[y_name].values.reshape(-1,1)
    GausNB = GaussianNB()
    GausNB.fit(x, y)

def Arboles():
    pass

def Neuronal():
    pass