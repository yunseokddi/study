from functions import numerical_diff as numerical

def gradient_descent(f, init_x, lr=0.01, step_num = 100):
    x = init_x

    for i in range(step_num):
        grad = numerical.numerical_gradient(f,x)
        x -= lr*grad

    return x