## Approximating the Goldbach Function with Machine Learning
Goldbach's conjecture is one of the oldest unsolved problems in mathematics. It states that every even number greater than 2 can be written as the sum of two prime numbers. The Goldbach function counts how many pairs of primes can form a given even number. While mathematicians like Hardy and Littlewood have made estimates for this function, machine learning approaches have been less explored. This project uses two machine learning methods to approximate the Goldbach function: a neural network and polynomial fitting.

### deep learing technqiues 
![Neural_networks](https://github.com/user-attachments/assets/a78d425c-6449-4678-ab96-a74d281fa499)
A simple Artificial Neural Network (ANN) was used to predict the number of prime pairs for even numbers. The model achieved an accuracy of about 13%. This shows that neural networks can be applied to this problem, but further improvements are needed for better results.

### Polynomial fit
![ploynomial_fit](https://github.com/user-attachments/assets/516f9ecb-f664-4de4-84dd-dbb770bbfa98)


##### Polynomial Equation
A 26th-degree polynomial was fitted to the data to approximate the Goldbach function. The equation is shown below:
 $$y = 1.60 \times 10^1 + 1.49 \times 10^{-2} x - 2.17 \times 10^{-7} x^2 + 4.26 \times 10^{-12} x^3 - 5.42 \times 10^{-17} x^4 + 4.42 \times 10^{-22} x^5 - 2.31 \times 10^{-27} x^6 + 7.52 \times 10^{-33} x^7 - 1.34 \times 10^{-38} x^8 + 5.89 \times 10^{-45} x^9 + 1.96 \times 10^{-50} x^{10} - 1.65 \times 10^{-56} x^{11} - 3.80 \times 10^{-62} x^{12} + 1.77 \times 10^{-68} x^{13} + 8.40 \times 10^{-74} x^{14} + 2.85 \times 10^{-80} x^{15} - 1.43 \times 10^{-85} x^{16} - 1.97 \times 10^{-91} x^{17} + 8.83 \times 10^{-98} x^{18} + 5.06 \times 10^{-103} x^{19} + 3.49 \times 10^{-109} x^{20} - 7.49 \times 10^{-115} x^{21} - 1.45 \times 10^{-120} x^{22} + 7.66 \times 10^{-127} x^{23} + 3.75 \times 10^{-132} x^{24} - 4.45 \times 10^{-138} x^{25} + 1.42 \times 10^{-144} x^{26}$$


### Reference
1) [Goldbach's conjecture](https://en.wikipedia.org/wiki/Goldbach%27s_conjecture)
2) [Goldbach's Function Approximation Using Deep Learning](https://arxiv.org/abs/1803.09237#:~:text=Goldbach%20conjecture%20is%20one%20of,for%20a%20given%20even%20number.)
3) [Goldbach's comet](https://en.wikipedia.org/wiki/Goldbach%27s_comet)



  
