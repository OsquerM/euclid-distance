#Variables 
distance = 1
def run(x1: float, y1: float, x2: float, y2: float) -> float:
    # TODO
    global distance
    distance = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
    return distance


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(distance)