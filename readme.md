# Monte Carlo Pi Estimation

This project implements a **Monte Carlo Simulation** to estimate the value of Pi. The Monte Carlo method for estimating pi is based on the idea that if you randomly scatter points inside a square and count the number of points that fall inside a circle inscribed in the square, you can estimate the value of pi.

## **Installation**

To run this project, make sure you have Python installed on your system. You also need to install the required libraries:

```bash
pip install numpy matplotlib

```


## **Usage**

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/MonteCarloPi.git
cd MonteCarloPi

```

Run the Python script to estimate Pi:

```bash
python app.py
```

The script will output the estimated value of Pi and display a plot showing the distribution of the points. Blue points represent those inside the circle, while red points are outside the circle.

## **How it works**

Random Points Generation: The program generates random points with coordinates between -1 and 1, representing a square with a side length of 2.
Distance Check: For each point, the distance from the origin (0, 0) is calculated. If the distance is less than or equal to 1, the point is inside the circle.
Pi Estimation: The ratio of points inside the circle to the total points is calculated and multiplied by 4 to estimate Pi.