import time


def productCalc():
    product = 1
    for i in range(1, 100000):
        product = product * i

    return product


start_time = time.time()
res = productCalc()
end_time = time.time()

print('The product is %s digit long.' % (len(str(res))))
print('The operation took %s seconds to calculate.' % (end_time - start_time))
