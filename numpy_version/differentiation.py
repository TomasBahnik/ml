import sys
from mxnet import autograd, np, npx

npx.set_np()


def f(x):
    # return np.dot(x, x)
    return x.sum()


# manually calculated grad of to f(x)
def grad_f(x):
    # return 2 * x
    return np.ones_like(x)


# x : the point where the gradient
# for the scalar function f(x) is calculated
def grad_f_at(x):
    x.attach_grad()

    print("l2(x) = {}, l2^2(x) = {}".format(np.linalg.norm(x), np.linalg.norm(x) ** 2))
    with autograd.record():
        y = f(x)
    y.backward()
    print("a={}, y(x)|_a = {}".format(x, y))
    print("gradient of f in x={} : {}".format(x, x.grad))
    print("test gradient : {}".format(x.grad == grad_f(x)))


def main():
    x = np.arange(5)
    grad_f_at(x)


if __name__ == '__main__':
    main()
    sys.exit(0)