import math

def dnd_to_normal(n, s, m):
    """damage thingees (n d s + m) to normal distribution params"""
    mu = n * (1 + s) / 2 + m
    sigma = math.sqrt(n * (s**2 - 1) / 12)
    return mu, sigma

def convert(n, s, m):
    mean, std_dev = dnd_to_normal(n, s, m)
    minimum = m
    maximum = n*s+m
    print(f"----------------\n| Roll: {n}d{s} +{m}\n----------------")
    print(f"| μ = {mean:.2f}\n| σ = {std_dev:.2f}\n----------------")
    print(f"| Min.: {minimum}\n| Max.: {maximum}\n----------------")


# example usage for 8d8+0
convert(8, 8, 0)