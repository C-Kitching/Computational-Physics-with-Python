# Computational Physics with Python

A collection of computational physics projects performed in Python.

## Contents

### 1. Bouncing balls

#### Project formulation

The goal of this mini project is to write a program to make a series of calculations regarding a bouncing ball above some minimum height.  
We can calculate the number of bounces analytically using conservation of energy. At height $h$ the ball with have potential energy $mgh$, where the symbols have their usual meanings. After one bounce the ball reaches a height $h\eta$ $(0 \leq \eta \leq 1)$ where $\eta$ takes into account energy lost during each bounce (an efficiency). After a second bounce the ball will reach a height $h\eta^{2}$, and so on.  
We can find the number of bounces above some minimum height, $h_{\text{min}}$, be examining the energy loss:
$$mgh_{\text{min}} = mgh\eta^{n},$$
where $n$ represents the number of bounces.  
Calculate:
1. The number of bounces **over** $h_{\text{min}}$, $n$, where $n \geq 0$.  
2. How many seconds it takes to complete the bounces.

#### Notes on the solution

Here I will outline the methodologies behind the solution (bouncing_balls.py).    
The problem itself is very simple, but there are some interesting technicalities to discuss. There is alot of potential for creativity in this project and we explore this from both a physics and computational viewpoint.  
The code takes an object-orientated approach, defining a class called 'Experiment' which contains variables such as the initial ball height, minimum height and graviational constant.  
Member functions have been created which ask the user to input values for these variables, all of which are checked for bad input such as non-numerical or non-physical.  
For the graviational constant the user can choose to enter their own value or select a an object in the solar system whose gravitaional constant will be used.  
A member function will then solve the scenario by calculating the number of bounces and the time take. Note that all edge cases are handled such as, perhaps the most interesting of which is the case when $h_{min}=0$, the ball will then bounce $\infty$ times but the time it takes to do this is actually finite and can be shown using geometric progression to be
$$t_{h_{min}=0}=\sqrt{\frac{2h}{g}}\left[\frac{1+\sqrt{\eta}}{1-\sqrt{\eta}}\right].$$
Finally, an animated plot is created to display the trajectory of the ball.

### 2. Nuclear decay

### 3. Measuring spreading laws

### 4. Numerical integration of differential equations - The damped harmonic oscillator

### 5. Monte Carlo techniques - Penetration of neutrons through shielding
